import mysql.connector
import csv
import json
from datetime import datetime

def clean_record(record):
    # Ejemplo de limpieza
    if record["quantity"] < 0:
        record["quantity"] = 0
    record["name"] = record["name"].strip().title()
    return record

conn = mysql.connector.connect(
    host="localhost", user="root", password="password", database="gym_inventory"
)
cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT * FROM inventory_raw")
raw_data = cursor.fetchall()

cleaned_data = [clean_record(dict(row)) for row in raw_data]

# Backup
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
with open(f"backups/raw_{timestamp}.csv", "w", newline="") as raw_file:
    writer = csv.DictWriter(raw_file, fieldnames=raw_data[0].keys())
    writer.writeheader()
    writer.writerows(raw_data)

with open(f"backups/cleaned_{timestamp}.csv", "w", newline="") as clean_file:
    writer = csv.DictWriter(clean_file, fieldnames=cleaned_data[0].keys())
    writer.writeheader()
    writer.writerows(cleaned_data)

# Insertar en tabla CLEANED
cursor.execute("DELETE FROM inventory_cleaned")
for item in cleaned_data:
    cursor.execute(
        "INSERT INTO inventory_cleaned (id, name, quantity) VALUES (%s, %s, %s)",
        (item["id"], item["name"], item["quantity"])
    )

# Log
log = {
    "timestamp": timestamp,
    "records_read": len(raw_data),
    "records_cleaned": len(cleaned_data),
    "raw_backup": f"backups/raw_{timestamp}.csv",
    "cleaned_backup": f"backups/cleaned_{timestamp}.csv"
}
with open(f"backups/log_{timestamp}.json", "w") as log_file:
    json.dump(log, log_file, indent=4)

conn.commit()
cursor.close()
conn.close()
