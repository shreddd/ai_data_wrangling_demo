import csv
from pathlib import Path

DATA_DIR = Path(__file__).parent


def load_dd(dd_path):
    with open(dd_path, newline="", encoding="latin-1") as f:
        reader = csv.DictReader(f)
        return {row["Column_or_Row_Name"]: row for row in reader}


def load_flmd(flmd_path):
    with open(flmd_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def get_file_columns(filepath):
    with open(filepath, newline="") as f:
        reader = csv.reader(f)
        return next(reader)


def validate(data_dir=DATA_DIR):
    dd = load_dd(data_dir / "dd.csv")
    flmd = load_flmd(data_dir / "flmd.csv")

    issues = []
    dd_columns = set(dd.keys())

    for entry in flmd:
        filename = entry["file_name"]

        # Skip non-data files (dd and flmd themselves)
        if filename in ("dd.csv", "flmd.csv"):
            continue

        filepath = data_dir / filename

        if not filepath.exists():
            issues.append(f"MISSING FILE: {filename} listed in flmd.csv but not found on disk")
            continue

        file_columns = get_file_columns(filepath)
        unmatched = [col for col in file_columns if col not in dd_columns]

        if unmatched:
            issues.append(
                f"UNDOCUMENTED COLUMNS in {filename}: {unmatched}"
            )
        else:
            print(f"OK  {filename} ({len(file_columns)} columns all in DD)")

    # Check for DD entries with missing Data_Type
    for col_name, row in dd.items():
        if not row.get("Data_Type", "").strip():
            issues.append(f"MISSING Data_Type in DD for column: {col_name}")

    print()
    if issues:
        print(f"VALIDATION FAILED — {len(issues)} issue(s) found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("VALIDATION PASSED — all files match the DD")

    return issues


if __name__ == "__main__":
    validate()
