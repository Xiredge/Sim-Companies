import requests


"""
This program handles the scrapping of the data from the sim companies API. It requires the URL then process the data and 
extract the main data needed.
"""


# Gets the data from the API and stores it in a list, then the function returns the list.
def fetch_json(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()
        print("Raw response content:", response.text)

        # Parse the JSON data
        json_data = response.json()

        return json_data

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


# Mostly paired with fetch_json, extract_date(fetch_json(url), data_name).
# This function processes the data and returns the first 10 prices, and returns it as a list.
def extract_price(data, data_name):
    obj = []  # Initialize a list for storing prices.
    if isinstance(data, list):  # Checks if the parameter data is an actual list.
        for item in data:  # Iterates through the data and assign each element to item.
            if data_name in item:  # Checks if data_name is in the item.
                if 'quality' in item:  # Checks if quality is in the item.
                    if int(item['quality']) <= 1:  # Checks if the quality of item is 1 or 0.
                        if len(obj) > 10:  # Only needed the first 10 items in the market of sim-co to get the average.
                            return obj
                        obj.append(int(item[data_name]))  # Appends the price to the list obj.
    else:
        print("Unexpected JSON format. END. ")
    return obj  # Returns the price list.


# This function gets the average price of product in the exchange. Useless as of 08/09/2024.
def get_average(container, data_name, product):
    data = extract_price(container, data_name)
    print(f"Product     : {product}")
    print(f"\nPrice list: {data[0:11]}")
    print(f"Number  of sellers in market: {int(len(data[0:11]))}")
    print(f"Amount  of goods   in market: {int(sum(data[0:11]))}")
    print(f"Average of price   in Market: {int(sum(data[0:11]) / len(data[0:11]))}")
    print(f"________________________________________________________________________________")


def extract_data(data, data_name):
    obj = []  # Initialize a list for storing prices.
    if isinstance(data, list):  # Checks if the parameter data is an actual list.
        if data_name in data:  # Checks if data_name is in the item.
            obj.append(data_name)  # Appends the price to the list obj.
    else:
        print("Unexpected JSON format. END. ")
    return obj  # Returns the price list.
