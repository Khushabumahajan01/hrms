import sys
from utils.db import get_db, release_db

conn, cur = get_db(True)
try:
    cur.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'hrms_employees'
    """)
    for row in cur.fetchall():
        print(row)
finally:
    release_db(conn, cur)
