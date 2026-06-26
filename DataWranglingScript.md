## Instructions
- Download data from https://data.ess-dive.lbl.gov/view/doi%3A10.15485%2F3020155
- Create CLAUDE.md

## Prompts

### Session 1 - Checking for errors: 
- read the dd and flmd files to understand the data dictionary and filelevel metadata
(Tries to coerce into different UTF formats - eventually figures it out)

- OK - now validate that all files in the FLMD match the DD

(This catches an error:
"One minor note: the DD row for Number_dry_days_week (row 20) is missing its Data_Type value — the cell is blank. The column exists and is defined, but the type field is empty.")

- can you create the code for doing this validation
- suggest a fix

- are all the DD files correct / Check the DD definitions with data in the files. 
Example Output:
```
Issue 1 — Inconsistent Treatment codes (DD vs data)

DD defines: C = control, H = warmed, N/A = warming not active
Fungal_mat_surface_area_growth.csv uses x (plots 6, spring) where the DD says it should be N/A
Leaf_colonization_time.csv correctly uses N/A for the same plots
Verdict: x in the growth file is a data error — should be N/A
Issue 2 — Relative_Growth_Rate_Weekly formula is wrong in the DD

DD definition says: Difference / Initial_Area * 100 — this gives ~2025% for GJ-01 (clearly wrong)
Measurement technique description says: (ln(Final) - ln(Initial)) / time — this gives ~0.51 (also doesn't match)
Actual values match: Raw_Growth / (Total_Weeks × 7) — i.e., raw growth per day, not per week
Verdict: DD formula definition is incorrect; the column appears to be cm²/day, not a percentage
Issue 3 — Depth column embeds units in the value

DD says unit = cm, data_type = text
All values are "0.5 cm" (unit repeated inside the cell)
Minor inconsistency, but technically the value should be 0.5 with the unit in the DD
Verdict: Minor — worth noting but not a blocker
Issue 4 — Colonization_Status=0 with Time_to_Colonization ≠ -9999
DD says -9999 = no colonization occurred, and Colonization_Status=0 = not colonized
Three MC rows (MC-04, MC-06, MC-09 — all plot 2 or 4, warmed, spring) have status=0 but time=6
These should either have time=-9999, or status=1 with the time recording when partial attachment was observed
Verdict: Data inconsistency — needs clarification from data authors
```

- Can you validate that the data dictionary doesn't have any issues?
Example Output:
```
Script saved at scripts/validate_dd.py. Found 8 issues across 6 checks:
Check	Row	Issue
Encoding	—	File is latin-1, not UTF-8 — the ° in °C breaks UTF-8 readers
Blank Data_Type	20	Number_dry_days_week is missing its Data_Type entirely
Unit format	7, 8, 10	Initial_Area, Final_Area, Raw_Growth use cm2 — should be cm²
RGR formula	11	Definition says Difference / Initial_Area * 100 but data actually matches Raw_Growth / (Total_Weeks × 7)
Depth mismatch	16	Data_Type=text with unit=cm contradicts each other; data embeds "0.5 cm" in the cell
Treatment codes	5	Definition doesn't document the x code found in the growth file
```

### Session 2 - Updating Data: 
- suggest an alternative to -9999 for invalid data types
- show me the code to make this change first
- apply

- look for other instances of -9999
- update code to look for sentinels in all files

### Session 3 - Adding new fields to data:
- Update the data dictionary to include latitude and longitude. Add it to soil_temp_leaf file. Prompt user if you aren't sure.
- Use the latitude and longitude for LBNL in decimal degrees. All plots are the same for now
(Finds missing venv and tries to fix pandas)

### Session 4 - Skills
- Create a Skill for general validation of DDs, FLMDs and csv files against these