#!/usr/bin/env python3
"""
Group Brain Ingest Pipeline with Ledger Tracking
Converts group session recordings/transcripts into structured knowledge
Maintains a dated ledger of all ingestion sessions and brain keeper decisions

Usage:
  python3 brain-ingest.py <transcript.txt> [--session-date 2026-09-28] [--participants "Dave,Ravi"]

Output:
  Creates vault notes with:
  - Extracted claims (prose-as-title format)
  - Frameworks discussed
  - Collective decisions
  - Disagreements and open questions
  - Automatic ledger entry with session metadata
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List

class BrainIngestSession:
    """Process a group session into vault-ready knowledge with ledger tracking."""

    def __init__(self, transcript_path: str, session_date: str = None, participants: str = None):
        self.transcript_path = Path(transcript_path)
        self.session_date = session_date or datetime.now().isoformat()
        self.participants = [p.strip() for p in (participants or "").split(",") if p.strip()]

        if not self.transcript_path.exists():
            print(f"❌ Transcript file not found: {self.transcript_path}")
            sys.exit(1)

        self.transcript = self.transcript_path.read_text()
        self.vault_dir = Path(__file__).parent.parent / "vault"
        self.vault_dir.mkdir(exist_ok=True)

        self.ledger_path = self.vault_dir / "ledger.md"

    def read_ledger(self) -> str:
        """Read existing ledger to understand prior sessions."""
        if not self.ledger_path.exists():
            return ""
        return self.ledger_path.read_text()

    def extract_claims(self) -> List[Dict]:
        """
        Extract falsifiable claims from transcript.

        Look for patterns like:
        - "We learned that..."
        - "The pattern is..."
        - "What we discovered..."
        - "This works when..."
        """
        claims = []

        claim_indicators = [
            "we learned that",
            "the pattern is",
            "what we discovered",
            "this works when",
            "we found that",
            "the insight is",
            "our observation",
            "it turns out that",
        ]

        lines = self.transcript.split("\n")
        for i, line in enumerate(lines):
            lower_line = line.lower()

            for indicator in claim_indicators:
                if indicator in lower_line:
                    claim_text = line.strip()

                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        if next_line and not any(next_line.startswith(ind) for ind in ["DAVE:", "RAVI:", "**"]):
                            claim_text += " " + next_line

                    claims.append({
                        "text": claim_text,
                        "line_number": i + 1,
                        "indicator": indicator,
                    })
                    break

        return claims

    def extract_frameworks(self) -> List[Dict]:
        """Extract mentioned frameworks and methodologies."""
        frameworks = []

        framework_keywords = [
            "framework",
            "methodology",
            "process",
            "sequence",
            "model",
            "approach",
        ]

        lines = self.transcript.split("\n")
        for i, line in enumerate(lines):
            lower_line = line.lower()

            for keyword in framework_keywords:
                if keyword in lower_line and any(verb in lower_line for verb in ["use", "follow", "apply", "work", "design"]):
                    frameworks.append({
                        "text": line.strip(),
                        "keyword": keyword,
                        "line_number": i + 1,
                    })
                    break

        return frameworks

    def extract_decisions(self) -> List[Dict]:
        """Extract major collective decisions."""
        decisions = []

        decision_indicators = [
            "we decided",
            "we're going to",
            "we will",
            "decision:",
            "let's commit to",
            "we decided to",
        ]

        lines = self.transcript.split("\n")
        for i, line in enumerate(lines):
            lower_line = line.lower()

            for indicator in decision_indicators:
                if indicator in lower_line:
                    decisions.append({
                        "text": line.strip(),
                        "indicator": indicator,
                        "line_number": i + 1,
                    })
                    break

        return decisions

    def extract_disagreements(self) -> List[Dict]:
        """Extract areas of disagreement or open questions."""
        disagreements = []

        disagreement_indicators = [
            "i disagree",
            "that's not quite right",
            "but what about",
            "the challenge is",
            "the risk is",
            "we haven't figured out",
            "open question",
            "need to validate",
        ]

        lines = self.transcript.split("\n")
        for i, line in enumerate(lines):
            lower_line = line.lower()

            for indicator in disagreement_indicators:
                if indicator in lower_line:
                    disagreements.append({
                        "text": line.strip(),
                        "type": indicator,
                        "line_number": i + 1,
                    })
                    break

        return disagreements

    def generate_vault_summary(self) -> str:
        """Generate a summary vault note for this session."""
        claims = self.extract_claims()
        frameworks = self.extract_frameworks()
        decisions = self.extract_decisions()
        disagreements = self.extract_disagreements()

        summary = f"""# Group Session: {self.session_date}

**Participants:** {', '.join(self.participants) if self.participants else '[See transcript]'}

---

## Key Claims ({len(claims)} found)

Claims extracted that follow prose-as-title format:

"""

        for claim in claims[:10]:
            summary += f"- **Claim:** {claim['text']}\n"
            summary += f"  - Line: {claim['line_number']}\n"

        if len(claims) > 10:
            summary += f"\n*... and {len(claims) - 10} more claims found*\n"

        summary += f"""

---

## Frameworks Discussed ({len(frameworks)} found)

"""

        for framework in frameworks[:10]:
            summary += f"- {framework['text']}\n"

        if len(frameworks) > 10:
            summary += f"\n*... and {len(frameworks) - 10} more frameworks mentioned*\n"

        summary += f"""

---

## Collective Decisions ({len(decisions)} found)

"""

        for decision in decisions[:10]:
            summary += f"- **Decision:** {decision['text']}\n"
            summary += f"  - Line: {decision['line_number']}\n"

        if len(decisions) > 10:
            summary += f"\n*... and {len(decisions) - 10} more decisions made*\n"

        summary += f"""

---

## Disagreements & Open Questions ({len(disagreements)} found)

"""

        for disagreement in disagreements[:10]:
            summary += f"- **{disagreement['type'].title()}:** {disagreement['text']}\n"

        if len(disagreements) > 10:
            summary += f"\n*... and {len(disagreements) - 10} more open items*\n"

        summary += f"""

---

## Next Steps for Brain Keeper (Dave)

1. **Validate Claims:** Review extracted claims; mark which are new vs. reaffirmation of existing
2. **Attribute Framework:** Link mentioned frameworks to existing vault notes or member expertise
3. **Document Decisions:** Move decisions to Decisions/ directory with full reasoning
4. **Resolve Disagreements:** Schedule follow-up on any open questions; update member expertise files
5. **Merge into Vault:** Consolidate learnings into main vault structure
6. **Update Ledger:** Record final decisions and cross-references in vault/ledger.md

---

**Session Recording:** [Link to recording if available]
**Transcript:** {self.transcript_path.name}
**Ingested:** {datetime.now().isoformat()}
**Status:** ⏳ Awaiting Brain Keeper Review

---

## Raw Extraction Stats

- Total claims detected: {len(claims)}
- Frameworks identified: {len(frameworks)}
- Decisions made: {len(decisions)}
- Open items: {len(disagreements)}
"""

        return summary, len(claims), len(frameworks), len(decisions), len(disagreements)

    def append_to_ledger(self, claims_count: int, frameworks_count: int, decisions_count: int, disagreements_count: int):
        """
        Append a dated entry to the ledger.

        This is called automatically at the end of ingestion to track:
        - What was extracted
        - When it was processed
        - Who participated
        - Status awaiting brain keeper review
        """
        safe_date = self.session_date.split("T")[0]  # YYYY-MM-DD

        ledger_entry = f"""
## {safe_date}

**Participants:** {', '.join(self.participants) if self.participants else '[Unknown]'}

**Extracted:**
- Claims: {claims_count}
- Frameworks: {frameworks_count}
- Decisions: {decisions_count}
- Open questions/disagreements: {disagreements_count}

**Summary:** {self.transcript_path.name}

**Ingestion Status:** Awaiting brain keeper validation

**Next Action:** Review vault/session-{safe_date}-ingestion-summary.md, validate claims, and update this ledger with decisions

---
"""

        # Append to ledger
        with open(self.ledger_path, 'a') as f:
            f.write(ledger_entry)

    def ingest(self):
        """Run the full ingestion pipeline."""
        print(f"📥 Ingesting session from {self.session_date}...")
        print(f"   Participants: {', '.join(self.participants) if self.participants else '[Unknown]'}")
        print()

        # STAGE 1: Read ledger (understand context before starting)
        prior_context = self.read_ledger()
        if prior_context:
            print("📋 Previous sessions found in ledger:")
            print("   (Run `cat group-brain/vault/ledger.md` to review)")
        else:
            print("📋 Starting new ledger (no prior sessions)")
        print()

        # STAGE 2: Extract from transcript
        summary, claims_count, frameworks_count, decisions_count, disagreements_count = self.generate_vault_summary()

        # STAGE 3: Write summary to vault
        safe_date = self.session_date.split("T")[0]  # YYYY-MM-DD
        output_filename = f"session-{safe_date}-ingestion-summary.md"
        output_path = self.vault_dir / output_filename

        output_path.write_text(summary)

        # STAGE 4: Append to ledger (automatic session tracking)
        self.append_to_ledger(claims_count, frameworks_count, decisions_count, disagreements_count)

        print(f"✅ Ingestion Complete!")
        print(f"   Summary: {output_path.name}")
        print(f"\n📋 Extracted:")
        print(f"   - Claims: {claims_count} high-confidence extractions")
        print(f"   - Frameworks: {frameworks_count} framework references")
        print(f"   - Decisions: {decisions_count} group decisions")
        print(f"   - Open questions: {disagreements_count} items for validation")
        print(f"\n📝 Ledger Updated:")
        print(f"   Dated entry appended to {self.ledger_path.name}")
        print(f"\n⏳ Brain Keeper Workflow:")
        print(f"   1. Review: {output_path.name}")
        print(f"   2. Validate: Which claims are new vs. reaffirmation?")
        print(f"   3. Update ledger: Record your decisions")
        print(f"   4. Cross-reference: Link claims across domains")
        print(f"   5. Commit: git add . && git commit -m 'brain: session-{safe_date} validation - [summary]'")
        print(f"\n📁 Vault: {self.vault_dir}")
        print(f"📁 Ledger: {self.ledger_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 brain-ingest.py <transcript.txt> [--session-date DATE] [--participants 'Name1,Name2']")
        print("\nExample:")
        print("  python3 brain-ingest.py session-2026-10-02.txt --participants 'Dave,Ravi'")
        sys.exit(1)

    transcript_path = sys.argv[1]
    session_date = None
    participants = None

    # Parse optional arguments
    for i in range(2, len(sys.argv), 2):
        if sys.argv[i] == "--session-date" and i + 1 < len(sys.argv):
            session_date = sys.argv[i + 1]
        elif sys.argv[i] == "--participants" and i + 1 < len(sys.argv):
            participants = sys.argv[i + 1]

    ingester = BrainIngestSession(transcript_path, session_date, participants)
    ingester.ingest()

if __name__ == "__main__":
    main()
