import requests

def currency_converter(input_currency, output_currency):
	response = requests.get(f'https://economia.awesomeapi.com.br/json/last/{input_currency}-{output_currency}')
	response_dict = response.json()
	return response_dict["bid"]


def main():
	return 0


if __name__ == "__main__":
	main()
