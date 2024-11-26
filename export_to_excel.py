import sqlite3
import pandas as pd

def export_to_excel():
    conn = sqlite3.connect('attendance.db')
    query = 'SELECT * FROM attendance'
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Export to Excel
    df.to_excel('attendance.xlsx', index=False)

export_to_excel()
