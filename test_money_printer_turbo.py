#!/usr/bin/env python3
"""Test MoneyPrinterTurbo integration in agenticSeek"""

import sys
import os
from pathlib import Path

def test_import():
    """Test if MoneyPrinterTurbo can be imported"""
    mpt_path = Path(__file__).parent / "money-printer-turbo"
    sys.path.insert(0, str(mpt_path))

    try:
        from app.services import llm
        from app.config import config
        print("✓ MoneyPrinterTurbo core modules imported successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to import MoneyPrinterTurbo: {e}")
        return False

def test_cli():
    """Test if CLI is accessible"""
    mpt_path = Path(__file__).parent / "money-printer-turbo"
    cli_path = mpt_path / "cli.py"

    if cli_path.exists():
        print(f"✓ CLI script found at {cli_path}")
        return True
    else:
        print(f"✗ CLI script not found at {cli_path}")
        return False

def test_config():
    """Test if config system works"""
    mpt_path = Path(__file__).parent / "money-printer-turbo"
    sys.path.insert(0, str(mpt_path))

    try:
        from app.config.config import config
        print(f"✓ Configuration loaded: {config.app_version}")
        return True
    except Exception as e:
        print(f"✗ Failed to load config: {e}")
        return False

def main():
    print("=" * 60)
    print("MoneyPrinterTurbo Integration Test - agenticSeek")
    print("=" * 60)

    results = {
        "Import Test": test_import(),
        "CLI Test": test_cli(),
        "Config Test": test_config(),
    }

    print("\n" + "=" * 60)
    print("Test Summary:")
    print("=" * 60)
    for test_name, result in results.items():
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")

    all_passed = all(results.values())
    print(f"\nOverall: {'ALL TESTS PASSED ✓' if all_passed else 'SOME TESTS FAILED ✗'}")

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
