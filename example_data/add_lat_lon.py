"""
Add Latitude and Longitude columns to Soil_temp_leaf_colonization.csv.
Site: Lawrence Berkeley National Laboratory (LBNL)
Coordinates apply to all plots equally.
Produces a versioned output file (v2).
"""

import pandas as pd
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "Soil_temp_leaf_colonization.csv"
OUTPUT_FILE = Path(__file__).parent / "Soil_temp_leaf_colonization_v2.csv"

LATITUDE = 37.8758   # LBNL, decimal degrees N
LONGITUDE = -122.2486  # LBNL, decimal degrees W

df = pd.read_csv(INPUT_FILE)

df.insert(0, "Latitude", LATITUDE)
df.insert(1, "Longitude", LONGITUDE)

df.to_csv(OUTPUT_FILE, index=False)

print(f"Input rows : {len(df)}")
print(f"Columns    : {list(df.columns)}")
print(f"Output     : {OUTPUT_FILE}")
