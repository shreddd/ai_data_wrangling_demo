"""
Validate that Soil_temp_leaf_colonization_v2.csv has correct Latitude/Longitude columns.
"""

import pandas as pd
from pathlib import Path
import sys

V1 = Path(__file__).parent / "Soil_temp_leaf_colonization.csv"
V2 = Path(__file__).parent / "Soil_temp_leaf_colonization_v2.csv"

EXPECTED_LAT = 37.8758
EXPECTED_LON = -122.2486

errors = []

# Load both files
df_v1 = pd.read_csv(V1)
df_v2 = pd.read_csv(V2)

# 1. Row count preserved
if len(df_v1) != len(df_v2):
    errors.append(f"Row count mismatch: v1={len(df_v1)}, v2={len(df_v2)}")
else:
    print(f"PASS  row count matches ({len(df_v2)} rows)")

# 2. New columns present
for col in ["Latitude", "Longitude"]:
    if col not in df_v2.columns:
        errors.append(f"Missing column: {col}")
    else:
        print(f"PASS  column '{col}' present")

# 3. Values correct
if "Latitude" in df_v2.columns:
    bad = df_v2[df_v2["Latitude"] != EXPECTED_LAT]
    if not bad.empty:
        errors.append(f"Unexpected Latitude values in {len(bad)} rows")
    else:
        print(f"PASS  all Latitude values == {EXPECTED_LAT}")

if "Longitude" in df_v2.columns:
    bad = df_v2[df_v2["Longitude"] != EXPECTED_LON]
    if not bad.empty:
        errors.append(f"Unexpected Longitude values in {len(bad)} rows")
    else:
        print(f"PASS  all Longitude values == {EXPECTED_LON}")

# 4. Original columns intact
orig_cols = list(df_v1.columns)
v2_orig = [c for c in df_v2.columns if c not in ("Latitude", "Longitude")]
if orig_cols != v2_orig:
    errors.append(f"Original columns changed:\n  expected {orig_cols}\n  got      {v2_orig}")
else:
    print(f"PASS  original columns unchanged")

# Result
if errors:
    print("\nFAIL")
    for e in errors:
        print(f"  ERROR: {e}")
    sys.exit(1)
else:
    print("\nAll checks passed.")
