# Group Brain: Collective Intelligence System

A three-layer system for capturing, organizing, and leveraging decades of accumulated business wisdom from the mastermind group.

**Current Members:** Dave (Founder, Brain Keeper), Ravi (Co-Curator)  
**Status:** Phase 1 (PDF Conversion) - Infrastructure Ready with Ledger Tracking

---

## System Overview

### Layer 1: Shared Context (`GROUP-CLAUDE.md`)
Master teaching document explaining:
- Group's collective intelligence architecture
- Each member's expertise maps, reasoning patterns, core frameworks
- Shared conventions (prose-as-title format for claims)
- Active disagreements and resolution process
- Collective hard decisions and their reasoning

### Layer 2: Knowledge Vault (`/vault/`)
Obsidian-compatible markdown vault organized as:
- `ledger.md` - Dated log of all ingestion sessions and validations
- `members/` - Individual expertise profiles (Dave, Ravi, incoming partners)
- `claims/` - Falsifiable business claims in prose-as-title format
- `frameworks/` - Active decision-making frameworks
- `decisions/` - Collective decisions with full reasoning
- `sessions/` - Summaries from group session ingestion

### Layer 3: Ingestion Pipeline (`/scripts/`)
Automated tools to convert raw input into vault knowledge:
1. **PDF-to-Markdown:** Convert collected research PDFs to searchable markdown
2. **Brain Ingest:** Process group session recordings/transcripts into structured claims, frameworks, and decisions (with automatic ledger tracking)

---

## Quick Start

### Phase 1: Convert PDFs to Markdown (Current)

**Prerequisites:** Python 3.7+, pdfplumber library

**Setup (once):**
```bash
# Create a virtual environment to avoid PEP 668 conflicts
python3 -m venv ~/group-brain-env

# Activate it
source ~/group-brain-env/bin/activate

# Install pdfplumber
pip install pdfplumber
```

**Usage:**
```bash
# Place PDFs in ~/group-brain-staging/
# Then run:
source ~/group-brain-env/bin/activate
python3 group-brain/scripts/convert-pdfs-to-markdown.py
```

**Output:** Markdown files in `staging/markdown-output/` - one per PDF, with full text extracted per page.

### Phase 2: Extract Claims & Organize (Next)

Once PDFs are converted:
1. Review markdown files for quality
2. Identify high-signal claims (new insights, validated patterns, hard decisions)
3. Restructure each claim as a vault note with:
   - **Title:** Falsifiable claim in prose format
   - **Thesis:** One sentence statement
   - **Evidence:** From group experience or data
   - **Counterargument:** Known limitations
   - **Attribution:** Who holds this view
   - **Last Updated:** Date of validation

**Example claim note:**

```markdown
# warm-outbound-converts-3x-better-than-cold-when-sequence-mirrors-buyer-language

**Thesis:** Personalized warm outbound sequences that mirror the buyer's own language around their problem convert 3x better than cold generic outreach.

**Evidence:**
- 5+ years of SaaS sales experience (Dave)
- 47 warm sequences vs 120 cold sequences analyzed in 2025
- Warm: 12% response rate; Cold: 4% response rate
- Win rate for warm follow-ups: 8%; Cold: 1.2%

**When This Works:**
- When you have genuine context about the buyer's business
- When their problem is well-defined (doesn't work for awareness campaigns)
- When sequence timing aligns with their decision cycle

**Counterargument:**
- Breaks down if buyer is already actively shopping (comparing vendors)
- Requires domain expertise; fake specificity actually hurts

**Attribution:** Dave (primary), Validated by Ravi

**Last Updated:** 2026-09-28

**Ledger Reference:** [Link to session where validated]
```

### Phase 3: Ingest into Vault (After Phase 2)

Set up MCP server integration so Claude agents can query the vault:
- Smart-Connections MCP (for semantic search)
- Obsidian MCP (for direct vault access)
- qmd MCP (for markdown querying)

This enables:
- New AI agents to inherit group's decision frameworks
- Claude to reference group wisdom in decisions
- Agent decisions to be logged back for group validation

---

## Directory Structure

```
group-brain/
├── GROUP-CLAUDE.md           # Master teaching document
├── README.md                 # This file
│
├── members/                  # Expertise profiles
│   ├── dave-expertise.md     # Dave's frameworks & reasoning
│   └── ravi-expertise.md     # Ravi's frameworks & reasoning
│
├── vault/                    # Obsidian-compatible vault
│   ├── ledger.md             # Dated log of all sessions & validations
│   ├── sessions/             # Ingested group sessions
│   ├── claims/               # Falsifiable business claims
│   ├── frameworks/           # Active decision frameworks
│   └── decisions/            # Collective decisions
│
├── scripts/                  # Ingestion pipeline
│   ├── convert-pdfs-to-markdown.py    # Phase 1: PDF conversion
│   ├── brain-ingest.py                # Phase 3: Session ingestion with ledger tracking
│   └── README.md                      # Detailed script docs
│
└── staging/                  # Temporary working area
    └── markdown-output/      # Phase 1 output directory
```

---

## Usage Patterns

### For Dave (Brain Keeper)

**After each group session:**
1. Save transcript (auto-generated or manual)
2. Run: `python3 scripts/brain-ingest.py transcript.txt --participants "Dave,Ravi"`
3. Brain-ingest automatically appends to vault/ledger.md with extraction metadata
4. Review generated summary in vault/
5. Update ledger entry with your validation decisions
6. Validate claims and update member expertise files
7. Commit changes with session attribution

**Weekly:**
- Scan vault for low-confidence or outdated claims (90+ days untouched)
- Mark ones ready for next group discussion
- Update GROUP-CLAUDE.md with new patterns

**The Ledger Discipline:**
- Read ledger BEFORE reviewing claims
- Write dated entry AFTER validating
- This ensures context never gets lost between sessions

### For Ravi & Incoming Partners

**Read once:**
- GROUP-CLAUDE.md (understand collective reasoning)
- members/dave-expertise.md (Dave's frameworks)

**During group sessions:**
- Contribute expertise and challenge assumptions
- Help identify new claims worth capturing
- Highlight where frameworks need refinement

**Quarterly:**
- Update your member expertise file
- Validate claims attributed to you
- Document new frameworks you're developing

### For AI Employees

**On initialization:**
1. Read GROUP-CLAUDE.md
2. Load member expertise files via MCP query
3. Inherit group's decision frameworks as reference points

**During operation:**
- When facing decisions, query vault for precedent
- Apply member reasoning patterns as alternatives
- Flag decisions that deviate from group frameworks

**Post-operation:**
- Summary of decision logged to vault/ai-decisions/
- Group reviews and validates (monthly)
- Learnings incorporated into member expertise or frameworks

---

## Conventions & Standards

### Prose-as-Title Format
Every claim note starts with a falsifiable claim as its title:
- ✅ `warm-outbound-converts-3x-better-than-cold-when-sequence-mirrors-buyer-language`
- ✅ `product-market-fit-is-measurable-through-nps-trajectory-and-churn-rate`
- ❌ `sales-notes` (too vague)
- ❌ `growth-insights` (not falsifiable)

### Claim Structure
Each claim note includes:
1. **Thesis** (one sentence)
2. **Evidence** (numbers, sources, conditions)
3. **When It Applies** (boundary conditions)
4. **Counterargument** (known limits)
5. **Attribution** (who holds this view)
6. **Last Updated** (date)
7. **Ledger Reference** (link to session where validated)

### Git Conventions
- Commit message format: `brain: [PHASE] [ACTION] - description`
- Example: `brain: phase-2 claim-extraction - warm-outbound converts 3x better (Dave)`
- Include session date if from group session
- One commit per major change (new framework, validated claim, new member)

---

## The Ledger: Load-Bearing Architecture

The vault/ledger.md is not just documentation—it's the system's memory:

**Read Before Work:**
- Brain keeper reads ledger.md before validating new claims
- Shows prior sessions, decisions already made, patterns established
- Prevents re-deciding or forgetting context

**Write After Work:**
- Every ingestion session auto-appends a dated entry with extraction metadata
- Brain keeper updates entry with validation decisions
- This preserves why a claim was accepted/rejected/deferred

**Why it matters:**
- Without it, every session starts cold
- Silent index degradation happens (claims lose relevance but nothing warns you)
- Context loss kills collective wisdom

---

## Troubleshooting

### "PEP 668: externally-managed-environment" Error

**Problem:** Can't pip install pdfplumber on system Python

**Solution:** Use a virtual environment
```bash
python3 -m venv ~/group-brain-env
source ~/group-brain-env/bin/activate
pip install pdfplumber
```

### "No PDFs found" When Running Conversion

**Problem:** Script says there are PDFs in staging but can't find them

**Solution:** Check that PDFs are in the right location
```bash
ls -la ~/group-brain-staging/
```

Make sure the convert script is finding the right path in its code.

### Vault Sync Issues

**When using Git sync:**
```bash
cd group-brain/vault
git status  # Check for conflicts
git add .
git commit -m "brain: vault sync - session 2026-10-02"
git push
```

---

## What's Next

### Immediate (This Week)
- [ ] Move 244 PDFs to staging directory
- [ ] Run Phase 1 conversion
- [ ] Review markdown quality
- [ ] Identify high-signal claims for Phase 2

### Short-term (This Month)
- [ ] Phase 2: Extract and structure 50+ key claims
- [ ] Complete Ravi's expertise file
- [ ] Set up first group session with recording + ingestion protocol
- [ ] Brain keeper validates and updates ledger

### Medium-term (Next Quarter)
- [ ] Phase 3: Vault ingestion + MCP server integration
- [ ] Bring in 2 additional partners
- [ ] Begin AI employee development
- [ ] Monthly group validation of ingested claims

### Long-term (Next Year)
- [ ] Integrate vault queries into daily business operations
- [ ] AI employees query vault for every major decision
- [ ] Expand to 10+ active frameworks
- [ ] Formalize disagreement resolution process

---

## Questions?

Refer to GROUP-CLAUDE.md for system philosophy and principles.  
Refer to member expertise files for reasoning patterns and frameworks.  
See scripts/README.md for detailed script documentation.

---

**Last Updated:** 2026-10-02  
**Vault Status:** Phase 1 Infrastructure Ready with Ledger Tracking  
**Brain Keeper:** Dave (dave@bespokeoracle.com)

