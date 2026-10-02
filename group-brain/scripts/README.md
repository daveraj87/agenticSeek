# Group Brain Scripts

Automated tools for the ingestion pipeline.

---

## convert-pdfs-to-markdown.py

**Purpose:** Phase 1 - Convert all PDFs in staging directory to searchable Markdown

**Handles:**
- All PDFs in `~/group-brain-staging/`
- Extracts text from every page
- Preserves page boundaries for reference
- Handles PDFs with no extractable text gracefully

**Setup (one-time):**
```bash
# Create virtual environment to avoid PEP 668 errors
python3 -m venv ~/group-brain-env

# Activate
source ~/group-brain-env/bin/activate

# Install dependency
pip install pdfplumber
```

**Usage:**
```bash
source ~/group-brain-env/bin/activate
python3 group-brain/scripts/convert-pdfs-to-markdown.py
```

**Output:**
```
staging/markdown-output/
├── book-1.md
├── book-2.md
├── research-paper-1.md
└── ...
```

Each markdown file includes:
- Title from PDF filename
- Source PDF name
- Total page count
- Extracted text per page (with page boundaries marked)

**Troubleshooting:**
- If script doesn't find PDFs: Check that `~/group-brain-staging/` exists and contains `.pdf` files
- If import fails: Did you `pip install pdfplumber`? Are you using the venv?
- If text extraction is poor: Some PDFs are scanned images without text layer - these will need manual review or OCR

**Performance:**
- ~244 PDFs @ ~50 pages average = should complete in 2-5 minutes
- Large PDFs (500+ pages) may take longer but should work fine

---

## brain-ingest.py

**Purpose:** Phase 3 - Convert group session recordings/transcripts into vault-ready knowledge with automatic ledger tracking

**Extracts:**
- **Claims:** Moments where group discovered or validated something ("we learned that...", "the pattern is...")
- **Frameworks:** Mentioned methodologies and processes
- **Decisions:** Collective decisions made during session ("we decided to...", "we're going to...")
- **Disagreements:** Open questions and areas of tension ("I disagree", "but what about...", "need to validate")

**Key Feature: Automatic Ledger Tracking**
- Reads vault/ledger.md BEFORE extracting (so you know prior context)
- Generates ingestion summary
- Automatically appends dated entry to ledger.md with extraction metadata
- Brain keeper reviews and updates ledger entry with validation decisions

**Usage:**
```bash
python3 brain-ingest.py transcript.txt \
  --session-date 2026-10-02 \
  --participants "Dave,Ravi"
```

**Input:** Transcript (plain text or markdown) from group session

**Output:** 
```
vault/session-2026-10-02-ingestion-summary.md
vault/ledger.md (automatically updated with dated entry)
```

Summary includes:
- List of extracted claims (10 best matches + total count)
- Frameworks identified
- Decisions made
- Open questions and disagreements
- Next steps for brain keeper review

Ledger entry includes:
- Session date and participants
- Counts of extracted claims, frameworks, decisions, disagreements
- Status: "Awaiting brain keeper validation"
- Link to generated summary for review

**Workflow:**

1. **Record session** (or get transcript from recording service)
2. **Run ingest:** `python3 brain-ingest.py session-2026-10-02.txt --participants "Dave,Ravi"`
3. **Ledger auto-appends** with extraction metadata
4. **Brain keeper reviews:** Open the generated summary
5. **Brain keeper updates ledger:** Mark which claims are new vs. reaffirmations
6. **Create vault notes:** Move each validated claim to `vault/claims/` as individual note
7. **Update member expertise:** Reflect new frameworks in member files
8. **Commit:** `git add . && git commit -m "brain: phase-3 session-2026-10-02 ingestion - [8 new] [3 reaffirmed]"`

**Claim Validation Checklist:**
- [ ] Is claim falsifiable? (can we test if it's wrong?)
- [ ] Is it new or confirming existing knowledge?
- [ ] Who in the group holds this view most strongly?
- [ ] What's the evidence for it?
- [ ] What could prove it wrong?
- [ ] Should this be a vault claim or just member expertise refinement?

**Ledger Entry Checklist (Brain Keeper):**
After reviewing the ingestion summary, update the ledger entry:

```markdown
## 2026-10-02

**Participants:** Dave, Ravi

**Extracted:**
- Claims: 12
- Frameworks: 3
- Decisions: 2
- Open questions: 1

**Brain Keeper Actions:**
- [x] Reviewed summary
- [x] Validated 8 new claims
- [x] Reaffirmed 3 existing claims
- [ ] Deferred 1 claim (reason: needs Ravi's data)
- [ ] Disputed 0 claims

**Cross-references:**
- Linked 4 claims to PMF framework
- Updated Dave expertise file with warm-outbound observation
- No new frameworks (all previously documented)

**Next Session Prep:**
- Follow up on deferred claim about team scaling
- Validate warm-outbound with Ravi's sales data
- Update decision on GTM strategy

---
```

---

## Future Scripts (Planned)

### claim-extractor.py
Extract claims from markdown files with NLP-assisted quality ranking.

### vault-validator.py
Check vault for:
- Outdated claims (> 90 days without validation)
- Conflicting claims
- Unsourced claims
- Orphaned frameworks (not referenced in claims or decisions)

### ai-decision-logger.py
Log AI agent decisions back to vault with reasoning, enabling group to learn from agent behavior.

---

## Script Guidelines for Developers

When adding new scripts:

1. **Single responsibility:** Each script does one thing well
2. **Error handling:** Graceful failures with helpful error messages
3. **Python 3.7+ compatible:** No fancy syntax that breaks on older versions
4. **Virtual environment ready:** Document `pip install` requirements
5. **Progress reporting:** User knows what's happening during long operations
6. **Next steps:** Script tells user what to do with its output
7. **Ledger awareness:** For ingestion scripts, read ledger before and write after

Example script template:
```python
#!/usr/bin/env python3
"""Script description."""

import sys
from pathlib import Path

def main():
    print("🔄 Starting operation...")
    
    try:
        # Do work
        print("✅ Success!")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nNext steps: ...")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

**Last Updated:** 2026-10-02

