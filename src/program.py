import requests
import sqlite3
from os import path
from tkinter import Button, Entry, Frame, Label, Tk
from ttkwidgets.autocomplete import AutocompleteCombobox

db_path = f'{path.dirname(__file__)}/../db/'
db = sqlite3.connect(f'{db_path}/currencies.db')
cur = db.cursor()


def currency_exchange_rate(input_currency: str, output_currency: str):
    response = requests.get(
        f'https://economia.awesomeapi.com.br/json/last/{input_currency}-{output_currency}'
    )
    if response.ok:
        rate = response.json()[(input_currency +
                                output_currency).upper()]['ask']
    else:
        response = requests.get(
            f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{input_currency}/{output_currency}.json'
        )
        if response.ok:
            rate = response.json()[output_currency.lower()]
        else:
            raise Exception('Request error')

    return float(rate)


class Root(Tk):

    def __init__(self):
        super(Root, self).__init__()

        self.title("Currency Coverter")
        self.minsize(600, 450)

        cur.execute('SELECT name FROM currencies_table')
        dabase_rows = cur.fetchall()
        currencies_names = [row[0] for row in dabase_rows]
        font = ('arial', 13, 'normal')
        frame = Frame(self)
        frame.pack(expand=True)
        l1 = Label(frame, text='Convert from: ', font=font, justify='left')
        e1 = AutocompleteCombobox(frame,
                                  completevalues=currencies_names,
                                  font=font)
        l2 = Label(frame, text='To: ', font=font, justify='left')
        e2 = AutocompleteCombobox(frame,
                                  completevalues=currencies_names,
                                  font=font)
        l3 = Label(frame, text='Value: ', font=font, justify='left')
        btn = Button(frame, text='Calculate', font=font, bg='#b3b3b3')
        e3 = Entry(frame, font=font)
        l4 = Label(frame, text='Result: ', font=font)
        result = Label(frame, font=font)
        l1.grid(row=0, column=0, pady=4)
        e1.grid(row=0, column=1, ipadx=2, ipady=2, pady=4)
        l2.grid(row=1, column=0, pady=4)
        e2.grid(row=1, column=1, ipadx=2, ipady=2, pady=4)
        l3.grid(row=2, column=0, pady=4)
        e3.grid(row=2, column=1, ipadx=2, ipady=2, pady=4)
        btn.grid(row=3, column=1, pady=(10, 4))
        l4.grid(row=4, column=0, pady=(20, 4))
        result.grid(row=4, column=1, pady=(20, 4))


window = Root()

if __name__ == '__main__':
    window.mainloop()
