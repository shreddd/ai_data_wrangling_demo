## Instructions
- Download data from https://data.ess-dive.lbl.gov/view/doi%3A10.15485%2F3020155
- Create CLAUDE.md

## Prompts

Session 1 - Checking for errors: 
- read the dd and flmd files to understand the data dictionary and filelevel metadata
(Tries to coerce into different UTF formats - eventually figures it out)
- OK - now validate that all files in the FLMD match the DD

(This catches an error:
"One minor note: the DD row for Number_dry_days_week (row 20) is missing its Data_Type value — the cell is blank. The column exists and is defined, but the type field is empty.")

- can you create the code for doing this validation
- suggest a fix

Session 2 - Updating Data: 
- suggest an alternative to -9999 for invalid data types
- show me the code to make this change first
- apply

- look for other instances of -9999
- update code to look for sentinels in all files

Session 3 - Adding new fields to data:
- Update the data dictionary to include latitude and longitude. Add it to soil_temp_leaf file. Prompt user if you aren't sure.
- Use the latitude and longitude for LBNL in decimal degrees. All plots are the same for now
(Finds missing venv and tries to fix pandas)
