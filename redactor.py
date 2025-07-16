import re
import os
from docx import Document
import fitz  # PyMuPDF

def build_redaction_patterns(name, email, phone):
    patterns = []

    # Escape name and email, case-insensitive
    if name:
        patterns.append(re.compile(re.escape(name), re.IGNORECASE))
    if email:
        patterns.append(re.compile(re.escape(email), re.IGNORECASE))

    # Normalize phone: remove all non-digits
    digits = re.sub(r"\D", "", phone)
    if digits:
        # Build a pattern that allows optional spaces or dashes between digits
        spaced_phone_regex = re.compile(
            r"[\+]?[\(]?\d{1,3}[\)]?[\s\-]?" + r"[\d\s\-]{7,15}",
            flags=re.IGNORECASE,
        )
        # Add exact digits string (in case no spacing in text)
        patterns.append(re.compile(re.escape(digits), re.IGNORECASE))
        patterns.append(spaced_phone_regex)

    return patterns

def redact_text(text, patterns):
    for pattern in patterns:
        if isinstance(pattern, str):
            text = re.sub(re.escape(pattern), "[REDACTED]", text, flags=re.IGNORECASE)
        elif isinstance(pattern, re.Pattern):
            text = pattern.sub("[REDACTED]", text)
    return text

def redact_docx(input_path, output_path, patterns):
    doc = Document(input_path)
    for para in doc.paragraphs:
        for i, run in enumerate(para.runs):
            run.text = redact_text(run.text, patterns)
    doc.save(output_path)

def redact_pdf(input_path, output_path, patterns):
    doc = fitz.open(input_path)
    redacted_text = ""
    
    for page in doc:
        text = page.get_text()
        redacted = redact_text(text, patterns)
        redacted_text += redacted + "\n\n"

    # Save redacted output as a new PDF (basic layout lost)
    redacted_doc = fitz.open()
    for chunk in redacted_text.split("\n\n"):
        page = redacted_doc.new_page()
        page.insert_text((50, 50), chunk, fontsize=10)
    redacted_doc.save(output_path)
