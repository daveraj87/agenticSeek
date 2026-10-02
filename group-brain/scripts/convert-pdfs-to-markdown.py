#!/usr/bin/env python3
"""
Group Brain PDF-to-Markdown Converter
Converts all PDFs in staging directory to searchable Markdown format
"""

import os
import sys
from pathlib import Path
from datetime import datetime

def try_import_pdfplumber():
    """Try to import pdfplumber; provide helpful error if it fails."""
    try:
        import pdfplumber
        return pdfplumber
    except ImportError:
        print("❌ ERROR: pdfplumber not installed")
        print("\nFix: Use a virtual environment to install dependencies:")
        print("  python3 -m venv ~/group-brain-env")
        print("  source ~/group-brain-env/bin/activate")
        print("  pip install pdfplumber")
        print("\nThen re-run this script:")
        print("  ~/group-brain-env/bin/python3 convert-pdfs-to-markdown.py")
        sys.exit(1)

def convert_pdfs():
    """Convert all PDFs in staging directory to Markdown."""
    pdfplumber = try_import_pdfplumber()

    # Determine paths
    script_dir = Path(__file__).parent
    group_brain_dir = script_dir.parent
    pdf_dir = group_brain_dir / "staging"
    output_dir = pdf_dir / "markdown-output"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Find all PDFs
    pdf_files = sorted(pdf_dir.glob("*.pdf"))

    if not pdf_files:
        print(f"⚠️  No PDFs found in {pdf_dir}")
        print("   Make sure PDFs are in ~/group-brain-staging/")
        return

    print(f"📄 Converting {len(pdf_files)} PDFs to Markdown...\n")
    print(f"Input:  {pdf_dir}")
    print(f"Output: {output_dir}\n")

    successful = 0
    failed = 0

    for i, pdf_path in enumerate(pdf_files, 1):
        try:
            with pdfplumber.open(pdf_path) as pdf:
                # Create markdown header
                md_content = f"# {pdf_path.stem}\n\n"
                md_content += f"**Source PDF:** {pdf_path.name}\n"
                md_content += f"**Total Pages:** {len(pdf.pages)}\n"
                md_content += f"**Converted:** {datetime.now().isoformat()}\n\n"
                md_content += "---\n\n"

                # Extract text from each page
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    if text:
                        md_content += f"## Page {page_num}\n\n{text}\n\n"
                    else:
                        md_content += f"## Page {page_num}\n\n*[No extractable text]*\n\n"

                # Write to markdown file
                output_path = output_dir / f"{pdf_path.stem}.md"
                output_path.write_text(md_content, encoding='utf-8')

                print(f"✓ {i:3d}/{len(pdf_files)} - {pdf_path.name}")
                successful += 1

        except Exception as e:
            print(f"✗ {i:3d}/{len(pdf_files)} - {pdf_path.name}")
            print(f"       └─ Error: {str(e)[:80]}")
            failed += 1

    print(f"\n{'='*60}")
    print(f"✅ Conversion Complete!")
    print(f"{'='*60}")
    print(f"✓ Successful:  {successful}/{len(pdf_files)}")
    print(f"✗ Failed:      {failed}/{len(pdf_files)}")
    print(f"\n📁 Output Directory: {output_dir}")
    print(f"📊 Markdown files are ready for claim extraction.\n")

    # Print next steps
    print("Next Steps:")
    print("  1. Review markdown files for quality")
    print("  2. Extract key claims with prose-as-title format")
    print("  3. Organize by domain and attribution")
    print("  4. Ingest into vault with group validation")

if __name__ == "__main__":
    convert_pdfs()
