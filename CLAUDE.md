# Dataset Workflows

## Metadata Files
- `dd.csv` — data dictionary: documents every column name with its unit, definition, and data type
- `flmd.csv` — file-level metadata: one row per data file describing its contents and format

## Notes
- Always create a plan before making updates and ask user to confirm
- Ask the user for any additional information instead of guessing
- For any changes to data files always generate code, and save it so that it can be reused
- Create validation scripts to test any changes that are created
- Create new versions of data files to maintain history 
- Track successful changes and updates in a log
- Save session memories

## Python
- Create a new local .venv if you need to install new libraries
- Always use this .venv if it exists