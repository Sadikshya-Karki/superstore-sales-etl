import sqlite3

def run_sql():

    conn = sqlite3.connect("superstore.db")
    cursor = conn.cursor()

    with open("sql/analysis.sql", "r") as file:
        sql_script = file.read()

    # CLEAN STEP 1: remove comments
    lines = sql_script.split("\n")
    cleaned_lines = []

    for line in lines:
        line = line.strip()
        if not line.startswith("--") and line != "":
            cleaned_lines.append(line)

    cleaned_sql = " ".join(cleaned_lines)

    # STEP 2: split queries properly
    queries = cleaned_sql.split(";")

    print("Running SQL queries...\n")

    for query in queries:
        query = query.strip()

        if not query:
            continue

        print("\nExecuting:")
        print(query[:100], "...")

        try:
            cursor.execute(query)

            results = cursor.fetchall()

            for row in results:
                print(row)

        except Exception as e:
            print("Error:", e)

    conn.close()


if __name__ == "__main__":
    run_sql()