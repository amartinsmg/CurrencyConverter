from os import mkdir, path
import requests
import sqlite3
import xmltodict


def main():
	db_path = f'{path.dirname(__file__)}/../db/'
	mkdir(db_path)
	db = sqlite3.connect(f'{db_path}/currencies.db')
	cur = db.cursor()
	cur.execute('''CREATE TABLE currencies_table(
	id        INTEGER PRIMARY KEY AUTOINCREMENT,
	name      TEXT,
	code      TEXT
	);''')
	query = "INSERT INTO currencies_table(name, code) VALUES('{}', '{}');"
	response = requests.post(
		'https://supply-xml.booking.com/hotels/xml/currencies')
	currencies = xmltodict.parse(response.content)['currencies']['currency']

	for currency in currencies:
		current_query = query.format(currency['@name'], currency['@currencycode'])
		cur.execute(current_query)

	db.commit()

if __name__ == '__main__':
	main()
