"""
csv_processor.py
Simple methods for loading/saving a CSV
"""

def load_csv(fname):
    "Opens a CSV named fname in the CWD"
    with open(fname, 'r') as f:
        csv_raw = f.read()
        csv = csv_raw.split("\n")
        for i in range(len(csv)):
            csv[i] = csv[i].split(',')
        return csv

def save_csv(csv, fname):
    "Saves a CSV named fname in the CWD"
    csv_joinRows = []
    for row in csv:
        csv_joinRows.append(','.join(row))
    csvRebuilt = "\n".join(csv_joinRows)
    with open(fname, "w") as f:
        f.seek(0)
        f.write(csvRebuilt)
        f.truncate()