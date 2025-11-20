"""
Main orchestration script: Run all extraction phases in sequence.

Executes:
1. Phase 1: Extract from Excel SurveySummary files
2. Phase 2: Extract from Word diary documents
3. Consolidation: Merge and produce final CSV

Usage:
    cd /path/to/TRAP-WD-2020-04/claude_extraction
    ./venv/bin/python3 scripts/run_extraction.py
"""

import os
import sys
import subprocess
import logging
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))
from utils import setup_logging


LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
SCRIPTS_DIR = os.path.dirname(__file__)


def run_script(script_name, description):
    """
    Run a Python script and report results.
    
    Args:
        script_name: Name of the script file
        description: Human-readable description
        
    Returns:
        True if successful, False otherwise
    """
    logging.info(f"\n{'=' * 80}")
    logging.info(f"Running: {description}")
    logging.info(f"Script: {script_name}")
    logging.info(f"{'=' * 80}\n")
    
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    
    try:
        # Get the venv python path
        venv_python = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'venv', 'bin', 'python3'
        )
        
        result = subprocess.run(
            [venv_python, script_path],
            capture_output=True,
            text=True,
            timeout=600  # 10 minute timeout
        )
        
        # Print output
        if result.stdout:
            print(result.stdout)
        
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        
        if result.returncode == 0:
            logging.info(f"✓ {description} completed successfully")
            return True
        else:
            logging.error(f"✗ {description} failed with exit code {result.returncode}")
            return False
    
    except subprocess.TimeoutExpired:
        logging.error(f"✗ {description} timed out")
        return False
    except Exception as e:
        logging.error(f"✗ {description} failed with error: {e}")
        return False


def main():
    """Main orchestration function."""
    # Setup logging
    os.makedirs(LOG_DIR, exist_ok=True)
    setup_logging(os.path.join(LOG_DIR, 'run_extraction.log'))
    
    logging.info("=" * 80)
    logging.info("TRAP DATA EXTRACTION PIPELINE")
    logging.info("=" * 80)
    logging.info("")
    
    # Track success of each phase
    results = {}
    
    # Phase 1: Excel extraction
    results['phase1'] = run_script('extract_phase1.py', 'Phase 1: Excel SurveySummary Extraction')
    
    if not results['phase1']:
        logging.error("Phase 1 failed. Cannot continue.")
        return
    
    # Phase 2: Diary extraction
    results['phase2'] = run_script('extract_phase2.py', 'Phase 2: Diary Document Extraction')
    
    if not results['phase2']:
        logging.warning("Phase 2 failed. Cannot continue to Phase 3.")
        results['phase3'] = False
    else:
        # Phase 3: Clean noisy extractions
        results['phase3'] = run_script('extract_phase3.py', 'Phase 3: Clean Noisy Extractions with NLP')
        
        if not results['phase3']:
            logging.warning("Phase 3 failed. Continuing with Phase 2 data.")
    
    # Consolidation
    results['consolidation'] = run_script('consolidate.py', 'Consolidation: Merge and Finalize')
    
    if not results['consolidation']:
        logging.error("Consolidation failed.")
        return
    
    # Summary
    logging.info("\n" + "=" * 80)
    logging.info("EXTRACTION PIPELINE COMPLETE")
    logging.info("=" * 80)
    logging.info("\nResults:")
    for phase, success in results.items():
        status = "✓ SUCCESS" if success else "✗ FAILED"
        logging.info(f"  {phase}: {status}")
    
    logging.info("\nOutput files:")
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
    logging.info(f"  - phase1_summary.csv")
    logging.info(f"  - phase2_roles.csv")
    logging.info(f"  - phase3_cleaned.csv")
    logging.info(f"  - final_attribution.csv (MAIN OUTPUT)")
    logging.info(f"\nAll outputs saved to: {output_dir}")
    logging.info("=" * 80)


if __name__ == "__main__":
    main()
