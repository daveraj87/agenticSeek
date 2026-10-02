# Group Brain Ledger

**Purpose:** Track every ingestion session, validation decision, and claim lifecycle. This ledger ensures context is never lost between sessions.

**How it works:**
1. Before brain-keeper work: Read this ledger to understand prior sessions
2. During ingestion: `brain-ingest.py` extracts claims automatically
3. After ingestion: Brain-keeper reviews and updates this ledger with decisions
4. Each dated entry tracks what was extracted, validated, deferred, or disputed

---

## Ledger Structure

Each session entry follows this format:

```
## YYYY-MM-DD

**Participants:** Name1, Name2

**Extracted:**
- Claims: N
- Frameworks: N
- Decisions: N
- Open questions: N

**Brain Keeper Actions:**
- [x] Reviewed summary
- [x] Validated X new claims
- [x] Reaffirmed Y existing claims
- [ ] Deferred Z claims (reason: ...)
- [ ] Disputed A claims (reason: ...)

**Cross-references:**
- Linked X claims to PMF framework
- Updated Y member expertise files
- Created Z new vault claims

**Next Session Prep:**
- Follow up on deferred items
- Validate disputed claims with Ravi
- Update [specific framework]

---
```

## Current Status

Ledger created: 2026-10-02
First ingestion: Awaiting first group session transcript

**To run Phase 1 ingestion:**
```bash
python3 brain-ingest.py <transcript.txt> --participants "Dave,Ravi"
```

This automatically appends a dated entry to this ledger with extraction metadata.

**To update with brain keeper decisions:**

Edit this file after each ingestion, adding your validation notes to the dated entry.

---

## Session Entries

(Entries will appear below as sessions are ingested)

