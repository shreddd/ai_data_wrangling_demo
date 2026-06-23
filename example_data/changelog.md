
## 2026-06-22 — Add Latitude/Longitude to soil temp file

**Files changed:**
- `dd.csv` — added `Latitude` and `Longitude` entries
- `Soil_temp_leaf_colonization_v2.csv` — new versioned file with `Latitude` (37.8758) and `Longitude` (-122.2486) columns prepended; all rows use LBNL site coordinates
- `flmd.csv` — added entry for `Soil_temp_leaf_colonization_v2.csv`

**Scripts:**
- `add_lat_lon.py` — generates v2 file from v1
- `validate_lat_lon.py` — validates row count, column presence, and coordinate values; all checks passed

**Coordinates source:** Lawrence Berkeley National Laboratory (LBNL), 37.8758°N, -122.2486°W; same value applied to all 12 rows (6 plots × 2 seasons).
