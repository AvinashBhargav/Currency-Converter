import requests

def convert_currency(amount, from_currency, to_currency):
    # API endpoint for exchange rate data
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    # Make a GET request to the API
    response = requests.get(url)

    # Convert the response to JSON format
    data = response.json()

    # Check if the API request was successful
    if response.status_code == 200:
        # Get the exchange rate from the data
        exchange_rate = data["rates"][to_currency]

        # Convert the amount to the desired currency
        converted_amount = amount * exchange_rate

        return converted_amount
    else:
        # Display an error message if the API request failed
        print("Error:", data["error"])

# Example usage
amount = 100  # Amount to convert
from_currency = "USD"  # Currency to convert from
to_currency = "EUR"  # Currency to convert to

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
