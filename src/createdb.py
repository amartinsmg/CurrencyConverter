from os import mkdir, path
import requests
import sqlite3


def main():
	db_path = f'{path.dirname(__file__)}/../db/'
	mkdir(db_path)
	db = sqlite3.connect(f'{db_path}/currencies.db')
	cur = db.cursor()
	cur.execute('''CREATE TABLE currencies_table(
		id   INTEGER PRIMARY KEY AUTOINCREMENT,
		code TEXT,
		name TEXT
	);''')
	query = "INSERT INTO currencies_table(code, name) VALUES('{}', '{}');"
	response = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json')
	currencies = response.json()

	for currency in currencies:
		current_query = query.format(currency, currencies[currency])
		cur.execute(current_query)

	db.commit()


if __name__ == '__main__':
	main()
