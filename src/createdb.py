import requests
import sqlite3

# This function creates a database to store the names and codes of the currencies.

def main(db_path: str):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE tb_currencies(
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT NOT NULL,
        name TEXT NOT NULL
    );''')
    query = "INSERT INTO tb_currencies(code, name) VALUES('{}', '{}');"
    response = requests.get(
        'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json'
    )
    currencies = response.json()

    for currency in currencies:
        current_query = query.format(currency, currencies[currency])
        cur.execute(current_query)

    conn.commit()
    conn.close()
