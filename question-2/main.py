

from __future__ import annotations
import os
import glob
import re
from typing import Dict, List, Tuple
import pandas as pd
import numpy as np

# ------------------------------
# Configuration / constants
# ------------------------------
TEMPERATURES_FOLDER = "temperatures"


# ------------------------------
# Helper functions
# ------------------------------
def find_csv_files(folder: str) -> List[str]:
    """
    Return list of CSV file paths in the given folder. Uses glob to match *.csv.
    """
    pattern = os.path.join(folder, "*.csv")
    files = sorted(glob.glob(pattern))
    return files


def main():

    files = find_csv_files(TEMPERATURES_FOLDER)


if __name__ == "__main__":
    main()
