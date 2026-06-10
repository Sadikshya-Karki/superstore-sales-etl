import sqlite3

def load_data(df):

    conn = sqlite3.connect("superstore.db")

    df.to_sql(
        "sales",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()