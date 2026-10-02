# GROUP-CLAUDE.md: Collective Intelligence Architecture

Master teaching document for the Group Brain—a three-layer system capturing decades of accumulated business wisdom from Dave, Ravi, and incoming partners.

---

## System Identity

**What it is:** A vault of falsifiable business claims, proven frameworks, and collective decisions that AI employees and the group can reference, challenge, and validate.

**Who owns it:** Dave (Brain Keeper), supported by Ravi (Co-Curator)

**How it grows:** Every group session is recorded, claims are extracted, and the brain keeper validates/integrates them into the vault.

**Why it matters:** Without it, every session starts cold. Collective wisdom disappears. Mistakes repeat. With it, Claude agents inherit the group's reasoning patterns, and humans can verify those patterns are still correct.

---

## Layer 1: Shared Context (This Document)

**Contains:**
- Group identity and core values
- Each member's expertise map, reasoning lens, frameworks
- Shared conventions for how claims are written
- Collective hard decisions and reasoning
- Known disagreements and how they're resolved

**Used by:**
- New partners onboarding
- AI employees inheriting group reasoning
- Brain keeper during validation sessions
- Ravi when challenging Dave's assumptions

---

## Layer 2: Knowledge Vault (`/vault/`)

**Structure:**
```
vault/
├── ledger.md              # Dated log of all ingestion sessions & validation
├── members/
│   ├── dave-expertise.md  # Dave's reasoning lens & frameworks
│   ├── ravi-expertise.md  # Ravi's reasoning lens & frameworks
│   └── [future partners]
├── claims/                # Falsifiable business claims (prose-as-title)
├── frameworks/            # Active decision-making frameworks
├── decisions/             # Collective hard decisions with reasoning
└── sessions/              # Ingestion summaries from group meetings
```

**Ledger discipline (load-bearing):**
- **Read before:** Brain keeper reads ledger.md before validating claims
- **Write after:** Every ingestion session appends a dated entry
- **Trust it:** The ledger is where context lives, not the index

**Claim format (prose-as-title):**

Each claim is a falsifiable statement, not a label:
- ✅ `warm-outbound-converts-3x-better-than-cold-when-sequence-mirrors-buyer-language`
- ✅ `product-market-fit-is-measurable-through-nps-trajectory-and-churn-rate`
- ❌ `sales-notes` (too vague)
- ❌ `growth-insights` (not falsifiable)

**Claim structure:**
```markdown
# warm-outbound-converts-3x-better-than-cold-when-sequence-mirrors-buyer-language

**Thesis:** [One sentence statement]

**Evidence:** [Numbers, sources, conditions where this holds]

**When It Applies:** [Boundary conditions]

**Counterargument:** [Known limits or objections]

**Attribution:** [Who holds this view, who validated it]

**Last Updated:** [Date of validation]

**Ledger Reference:** [Link to session where this was last validated]
```

---

## Layer 3: Ingestion Pipeline (`/scripts/`)

**Phase 1: PDF Conversion** (do this first)
- Convert 244+ collected PDFs to searchable Markdown
- Script: `convert-pdfs-to-markdown.py`
- Output: `staging/markdown-output/*.md`

**Phase 2: Claim Extraction** (do this second)
- Review Markdown files for high-signal claims
- Extract and structure as vault notes
- Attribute to Dave, Ravi, or external source

**Phase 3: Session Ingestion** (do this third)
- Convert group session recordings/transcripts to structured knowledge
- Script: `brain-ingest.py` (now with automatic ledger tracking)
- Extracts claims, frameworks, decisions, disagreements
- Auto-appends to ledger, awaits brain keeper validation

---

## Member Expertise Maps

### Dave (Founder, Brain Keeper)

**Core Reasoning Lens:**
- Systems thinking over silos
- First-principles analysis of business problems
- Pattern recognition from 5+ years SaaS experience
- Founder bias: believing product solves the problem

**Proven Frameworks:**

1. **Warm Outbound Buyer Psychology**
   - Personalized warm sequences that mirror buyer's language convert 3x better than cold outreach
   - Evidence: 5+ years SaaS sales, 47 warm sequences vs 120 cold sequences analyzed in 2025
   - Warm response rate: 12%, Win rate: 8%
   - Cold response rate: 4%, Win rate: 1.2%
   - Works when buyer problem is well-defined; breaks when they're already actively shopping

2. **Product-Market Fit Diagnosis**
   - PMF exists when NPS stays 50+ AND churn < 10% annually, maintained for 2+ quarters
   - Churn without NPS drop = wrong ICP, not bad product
   - NPS without retention = good vibes, bad unit economics
   - Both together = PMF signal worth scaling

3. **Team Scaling Culture Codification**
   - Teams break at transitions: 3→5, 10→20, 30+ people
   - Breaks happen when founder's culture only exists in their head
   - Fix: Explicit documentation of decision-making, values, conflict resolution
   - Can't be done retroactively once people are hired wrong

**Known Biases:**
- Pattern recognition overconfidence (sees patterns that aren't there)
- First-principles bias (over-indexes on "what should be true" vs. what is)
- Early-mover assumption (assumes first-mover advantage holds longer than it does)
- Founder lens (assumes product solves the problem, not sales/marketing)

**Collaboration Style:**
- Wants to deep-dive into root causes
- Questions assumptions even when they're working
- Pushes back harder when something feels wrong
- Respects data over vibes, but values Ravi's intuition on things with no data

---

### Ravi (Co-Curator)

**Role:** Challenge Dave's assumptions, contribute complementary expertise, validate frameworks

**To be filled in by Ravi:**
- Core reasoning lens (vs. Dave's systems thinking / first principles)
- Proven frameworks (domains where Ravi leads)
- Known biases
- Collaboration style
- Recent learning cycles

**Template to complete:**

```markdown
# ravi-expertise.md

**Core Reasoning Lens:**
- [What's Ravi's unique perspective?]
- [How does it complement Dave's systems thinking?]

**Proven Frameworks:**
1. [Framework 1]
   - When it works
   - Evidence
   - Known limits

**Known Biases:**
- [Bias 1]
- [Bias 2]

**Collaboration Style:**
- How Ravi prefers to work
- What Ravi values in decisions
- When Ravi pushes back hardest

**Recent Learning Cycles:**
- What Ravi learned last quarter
- How it changed Ravi's thinking
```

---

## Shared Conventions

### Writing Claims

- **Title format:** Prose-as-title, falsifiable statement
- **One sentence thesis:** Can a newcomer understand the claim in 20 seconds?
- **Evidence section:** Numbers, conditions, time period tested
- **Counterargument:** What would prove this wrong? When does it break?
- **Attribution:** Who discovered this? Who validated it?
- **Dating:** Last updated when? Too-old claims get flagged

### Making Decisions

1. **Read the ledger:** What did we decide before on related topics?
2. **Check frameworks:** Which of our proven patterns apply?
3. **Seek member lens:** How would Ravi see this? Any blindspots?
4. **Decide and document:** Write the decision with reasoning, not just the outcome
5. **Log it:** Append to ledger and decisions/ vault folder
6. **Follow up:** 90 days later, is the decision still holding?

### Resolving Disagreements

When Dave and Ravi disagree:
1. **Name the disagreement:** Write it to vault/disagreements/ explicitly
2. **State evidence:** What data/pattern supports each view?
3. **Identify the test:** What would prove one side right?
4. **Defer or decide:** If test is cheap, run it. If expensive, defer to next group session.
5. **Log the outcome:** Update disagreement note with what we learned

---

## Phase 1 Workflow: PDF Conversion

**Why first:** PDFs are raw data; converting to Markdown makes them searchable and extractable.

**Setup (one-time):**
```bash
python3 -m venv ~/group-brain-env
source ~/group-brain-env/bin/activate
pip install pdfplumber
```

**Execution:**
```bash
source ~/group-brain-env/bin/activate
python3 group-brain/scripts/convert-pdfs-to-markdown.py
```

**Troubleshooting:**
- If script doesn't find PDFs: Check ~/group-brain-staging/ exists with .pdf files
- If import fails: Did you `pip install pdfplumber`? Are you using the venv?
- If text extraction is poor: Some PDFs are scanned images without text layer (need manual OCR)

**Performance:** 244 PDFs @ 50 pages average = 2-5 minutes

---

## Phase 2 Workflow: Claim Extraction

**What to do:**
1. Review markdown files from Phase 1 output
2. Scan for high-signal claims (new insights, validated patterns, hard decisions)
3. Extract each claim as a vault note using prose-as-title format
4. Attribute to Dave, Ravi, or external research

**When to extract:**
- Actionable frameworks (used in >1 situation)
- Surprising patterns (contradicts initial assumption)
- Hard-won lessons (cost Dave/Ravi time/money to learn)
- Validated patterns (tested multiple times, still holding)

**When NOT to extract:**
- One-off observations
- Opinions without pattern
- Vague insights ("communicate better")
- Unvalidated ideas

---

## Phase 3 Workflow: Session Ingestion

**Group session capture:**
- Record or transcript every group call (minimum 5-min buffer at end)
- Save as `session-YYYY-MM-DD.txt` or `.md`

**Ingestion workflow:**
```bash
python3 brain-ingest.py session-2026-10-02.txt --participants "Dave,Ravi"
```

**What the script does:**
1. Reads ledger (understands prior sessions)
2. Extracts claims, frameworks, decisions, disagreements from transcript
3. Generates `vault/session-YYYY-MM-DD-ingestion-summary.md`
4. Appends dated entry to `vault/ledger.md` (automatic, no manual step)

**Brain keeper review (Dave):**
1. Open generated summary
2. Validate claims: New vs. reaffirmation vs. disputed?
3. Update ledger entry with decisions (mark decisions with checkboxes)
4. Cross-reference to other frameworks if applicable
5. Commit with message: `brain: session-2026-10-02 validation - 8 new claims, 3 reaffirmed, 2 deferred`

**The ledger discipline ensures:**
- No context loss between sessions
- Every decision is logged with date and reasoning
- Stale claims surface automatically (90+ days untouched)
- AI employees can see exactly why claims are trusted

---

## For AI Employees

**On initialization:**
1. Read this document (GROUP-CLAUDE.md) top to bottom
2. Load member expertise files (members/*.md)
3. Query vault for precedent on decisions you face

**During operation:**
- When facing a decision, ask: "What has the group learned about this?"
- Reference precedent from claims or frameworks
- Flag if your decision contradicts the group's past patterns
- Surface if new data contradicts an existing claim

**After operation:**
- Log your decision to `vault/ai-decisions/` with reasoning
- Brain keeper validates or challenges monthly
- Learnings update member expertise or frameworks

---

## Roadmap

### Immediate (This Week)
- [ ] Convert 244 PDFs to Markdown (Phase 1)
- [ ] Review Markdown for quality
- [ ] Identify high-signal claims

### Short-term (This Month)
- [ ] Extract 50+ key claims (Phase 2)
- [ ] Complete Ravi's expertise file
- [ ] First group session with recording protocol
- [ ] Brain keeper validates claims and updates ledger

### Medium-term (Next Quarter)
- [ ] Phase 3: MCP server integration (Smart-Connections, qmd, Obsidian)
- [ ] Bring in 2 additional partners
- [ ] Begin AI employee development
- [ ] Monthly group validation sessions

### Long-term (Next Year)
- [ ] Integrate vault queries into daily operations
- [ ] AI employees query vault for every major decision
- [ ] Expand to 10+ active frameworks
- [ ] Formalize disagreement resolution process

---

**Last Updated:** 2026-10-02  
**Brain Keeper:** Dave (dave@bespokeoracle.com)  
**Co-Curator:** Ravi (ravi@[email].com)

