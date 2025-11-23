import sqlite3

conn = sqlite3.connect("lab_results.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(test_results);")
columns = cursor.fetchall()

if not any(col[1] == "execution_time" for col in columns):
    cursor.execute("ALTER TABLE test_results ADD COLUMN execution_time REAL;")
    print("✔ Colonne execution_time ajoutée")

if not any(col[1] == "campaign_id" for col in columns):
    cursor.execute("ALTER TABLE test_results ADD COLUMN campaign_id INTEGER;")
    print("✔ Colonne campaign_id ajoutée")

conn.commit()
conn.close()

print("✔ Modifications terminées.")
