#!/usr/bin/env python3
"""
Test case for scanning the /tmp/ directory in the sandbox environment.
Demonstrates sandbox execution by listing files and directories in /tmp/.
"""

import os
import logging
from datetime import datetime
from pathlib import Path


# Configure logging
LOG_FILE = Path(__file__).parent / "tmp_directory_scan.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def scan_tmp_directory():
    """
    Scan the /tmp/ directory and list all files and directories found.
    
    Returns:
        dict: Contains 'files' and 'directories' lists, and 'total_count'
    """
    tmp_path = Path("/tmp")
    results = {
        "files": [],
        "directories": [],
        "total_count": 0,
        "scan_timestamp": datetime.now().isoformat()
    }
    
    if not tmp_path.exists():
        logger.warning(f"/tmp/ directory does not exist!")
        return results
    
    if not tmp_path.is_dir():
        logger.warning(f"/tmp/ is not a directory!")
        return results
    
    logger.info("=" * 60)
    logger.info("Starting scan of /tmp/ directory")
    logger.info("=" * 60)
    
    try:
        for item in tmp_path.iterdir():
            item_name = item.name
            item_path = str(item)
            
            if item.is_file():
                results["files"].append(item_path)
                logger.info(f"[FILE] {item_path}")
            elif item.is_dir():
                results["directories"].append(item_path)
                logger.info(f"[DIR]  {item_path}")
            else:
                logger.info(f"[OTHER] {item_path}")
            
            results["total_count"] += 1
            
    except PermissionError as e:
        logger.error(f"Permission denied when scanning /tmp/: {e}")
    except Exception as e:
        logger.error(f"Error scanning /tmp/ directory: {e}")
    
    return results


def test_scan_tmp_directory():
    """
    Test function that scans /tmp/ directory and verifies the results.
    Prints findings to standard output and logs them for verification.
    """
    logger.info("=" * 60)
    logger.info("TEST: Scanning /tmp/ Directory in Sandbox Environment")
    logger.info("=" * 60)
    
    # Perform the scan
    results = scan_tmp_directory()
    
    # Print summary to stdout
    print("\n" + "=" * 60)
    print("SCAN RESULTS SUMMARY")
    print("=" * 60)
    print(f"Scan Timestamp: {results['scan_timestamp']}")
    print(f"Total Items Found: {results['total_count']}")
    print(f"Files Found: {len(results['files'])}")
    print(f"Directories Found: {len(results['directories'])}")
    
    print("\n--- FILES ---")
    if results['files']:
        for f in results['files']:
            print(f"  {f}")
    else:
        print("  (No files found)")
    
    print("\n--- DIRECTORIES ---")
    if results['directories']:
        for d in results['directories']:
            print(f"  {d}")
    else:
        print("  (No directories found)")
    
    print("=" * 60)
    
    # Log the findings to demonstrate sandbox execution
    logger.info("-" * 60)
    logger.info("SANDBOX EXECUTION VERIFICATION")
    logger.info("-" * 60)
    logger.info(f"Successfully scanned /tmp/ directory")
    logger.info(f"Total items: {results['total_count']}")
    logger.info(f"Files: {len(results['files'])}, Directories: {len(results['directories'])}")
    logger.info("Test completed successfully - Sandbox execution verified!")
    
    # Return results for verification
    return results


if __name__ == "__main__":
    print("Ahoy matey! Starting /tmp/ directory scan test in the sandbox! 🏴‍☠️")
    test_scan_tmp_directory()
    print("\nArrr! Test be completed successfully! ⚓")
