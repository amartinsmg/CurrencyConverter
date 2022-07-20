import requests
import sqlite3
from createdb import main as createdb
from os import path
from tkinter import Button, Entry, font as tkFont, Frame, Label, StringVar, Tk
from ttkwidgets.autocomplete import AutocompleteCombobox


class Program(Tk):

    def __init__(self):
        super(Program, self).__init__()
        self.title("Currency Coverter")
        self.minsize(600, 450)
        def_font = tkFont.nametofont('TkDefaultFont')
        def_font.config(size=13)
        self.option_add('*Font', def_font)
        db_path = path.join(path.abspath('.'), 'currencies.db')
        db = sqlite3.connect(db_path)
        self.cur = db.cursor()
        try:
            self.cur.execute('SELECT name FROM currencies_table')
        except:
            createdb(db_path)
            self.cur.execute('SELECT name FROM currencies_table')
        dabase_rows = self.cur.fetchall()
        currencies_names = [row[0] for row in dabase_rows]
        frame = Frame(self)
        frame.pack(expand=True)
        self.input_currency = StringVar()
        self.output_currency = StringVar()
        self.input = StringVar()
        l1 = Label(frame, text='Convert from: ')
        e1 = AutocompleteCombobox(frame,
                                  textvariable=self.input_currency,
                                  completevalues=currencies_names)
        l2 = Label(frame, text='To: ')
        e2 = AutocompleteCombobox(frame,
                                  textvariable=self.output_currency,
                                  completevalues=currencies_names)
        l3 = Label(frame, text='Value: ')
        btn = Button(frame,
                     text='Calculate',
                     bg='#b3b3b3',
                     command=self.calculate)
        e3 = Entry(frame, textvariable=self.input)
        l4 = Label(frame, text='Result: ', font=(def_font.name, 13, 'bold'))
        self.result = Label(frame)
        l1.grid(row=0, column=0, pady=4)
        e1.grid(row=0, column=1, ipadx=2, ipady=2, pady=4)
        l2.grid(row=1, column=0, pady=4)
        e2.grid(row=1, column=1, ipadx=2, ipady=2, pady=4)
        l3.grid(row=2, column=0, pady=4)
        e3.grid(row=2, column=1, ipadx=2, ipady=2, pady=4)
        btn.grid(row=3, column=1, pady=(15, 4))
        l4.grid(row=4, column=0, pady=(25, 4))
        self.result.grid(row=4, column=1, pady=(25, 4))

    def currency_exchange_rate(self, input_currency: str,
                               output_currency: str):
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

    def calculate(self):
        input_currency_name = self.input_currency.get()
        output_currency_name = self.output_currency.get()
        self.cur.execute(
            f"SELECT code FROM currencies_table WHERE name LIKE '{input_currency_name}'"
        )
        input_currency = self.cur.fetchall()[0][0]
        self.cur.execute(
            f"SELECT code FROM currencies_table WHERE name LIKE '{output_currency_name}'"
        )
        output_currency = self.cur.fetchall()[0][0]
        input = float(self.input.get())
        try:
            rate = self.currency_exchange_rate(input_currency, output_currency)
            output = f'{(input * rate):.2f}'
        except Exception as e:
            output = str(e)
        self.result['text'] = output


window = Program()

if __name__ == '__main__':
    window.mainloop()
