import csv
from pathlib import Path

DATA_DIR = Path(__file__).parent
DD_FILE = DATA_DIR / "dd.csv"
SENTINEL = "-9999"
# Metadata files that should not be scanned for sentinel values
SKIP_FILES = {"dd.csv", "flmd.csv"}


def fix_sentinel_values():
    data_files = [
        p for p in DATA_DIR.glob("*.csv") if p.name not in SKIP_FILES
    ]

    for csv_file in sorted(data_files):
        with open(csv_file, newline="") as f:
            rows = list(csv.DictReader(f))

        if not rows:
            continue

        changed = 0
        for row in rows:
            for col, val in row.items():
                if val == SENTINEL:
                    row[col] = ""
                    changed += 1

        if changed:
            with open(csv_file, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
            print(f"Replaced {changed} sentinel value(s) in {csv_file.name}")
        else:
            print(f"No sentinel values found in {csv_file.name}")

    # Update DD definition for Time_to_Colonization
    with open(DD_FILE, newline="", encoding="latin-1") as f:
        dd_rows = list(csv.DictReader(f))

    for row in dd_rows:
        if row["Column_or_Row_Name"] == "Time_to_Colonization":
            row["Definition"] = (
                "weeks it took for the fungal mat to colonize the recently senesced "
                "leaf of Swietenia mahogoni. Empty = no leaf colonization occurred."
            )
            break

    fieldnames = dd_rows[0].keys()
    with open(DD_FILE, "w", newline="", encoding="latin-1") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dd_rows)

    print(f"Updated Time_to_Colonization definition in {DD_FILE.name}")


if __name__ == "__main__":
    fix_sentinel_values()
