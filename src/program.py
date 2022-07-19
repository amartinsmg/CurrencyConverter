import requests
from tkinter import Button, Entry, Frame, Label, Tk


def currency_exchange(input_currency, output_currency):
	response = requests.get(
		f'https://economia.awesomeapi.com.br/json/last/{input_currency}-{output_currency}'
	)
	response_dict = response.json()
	return float(response_dict["ask"])


class Root(Tk):

	def __init__(self):
		super(Root, self).__init__()

		self.title("Currency Coverter")
		self.minsize(600, 450)

		font = ('arial', 13, 'normal')
		frame = Frame(self)
		frame.pack(expand=True)
		l1 = Label(frame, text='Convert from: ', font=font)
		e1 = Entry(frame, font=font)
		l2 = Label(frame, text='To: ', font=font)
		e2 = Entry(frame, font=font)
		l3 = Label(frame, text='Value: ', justify='left', font=font)
		btn = Button(frame, text='Calculate', font=font, bg='#00d7ff')
		e3 = Entry(frame, font=font)
		l4 = Label(frame, text='Result: ', font=font)
		result = Label(frame, font=font)
		result['text'] = str(5+5)
		result['text'] = str(5+7)
		l1.grid(row=0, column=0, pady=4)
		e1.grid(row=0, column=1, ipadx=2, ipady=2, pady=4)
		l2.grid(row=1, column=0, pady=4)
		e2.grid(row=1, column=1, ipadx=2, ipady=2, pady=4)
		l3.grid(row=2, column=0, pady=4)
		e3.grid(row=2, column=1, ipadx=2, ipady=2, pady=4)
		btn.grid(row=3, column=1, pady=(10, 4))
		l4.grid(row=4,column=0, pady=(20, 4))
		result.grid(row=4,column=1, pady=(20, 4))


window = Root()

if __name__ == "__main__":
	window.mainloop()
