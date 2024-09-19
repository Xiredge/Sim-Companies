from Data_Base import insert_record, connect, get_datetime
from Import_JSON import extract_price, fetch_json
import time
import os
import sqlite3


def live_market():
    price_difference('Reinforced Concrete')
    price_difference('Bricks')
    price_difference('Planks')
    price_difference('Construction Units')
    price_difference('Tablet')
    price_difference('Luxury Car')

    input("\nPress any key to continue...\n")

    # Extract and print the prices.

    concrete_url = 'https://www.simcompanies.com/api/v3/market/0/101/'  # Reinforce Concrete API
    concrete_data = fetch_json(concrete_url)
    concrete_price = extract_price(concrete_data, 'price')
    print("Gathering data for reinforced concrete...")
    time.sleep(10)

    bricks_url = 'https://www.simcompanies.com/api/v3/market/0/102/'  # Bricks API
    bricks_data = fetch_json(bricks_url)
    bricks_price = extract_price(bricks_data, 'price')
    print("Gathering data for bricks...")
    time.sleep(10)

    planks_url = 'https://www.simcompanies.com/api/v3/market/0/108/'  # Planks API
    planks_data = fetch_json(planks_url)
    planks_price = extract_price(planks_data, 'price')
    print("Gathering data for planks...")
    time.sleep(10)

    construction_url = 'https://www.simcompanies.com/api/v3/market/0/111/'  # Construction Units API
    construction_data = fetch_json(construction_url)
    construction_price = extract_price(construction_data, 'price')
    print("Gathering data for construction units...")
    time.sleep(10)

    tablet_url = 'https://www.simcompanies.com/api/v3/market/0/25/'  # Tablet API
    tablet_data = fetch_json(tablet_url)
    tablet_price = extract_price(tablet_data, 'price')
    print("Gathering data for tablets...")
    time.sleep(10)

    luxury_url = 'https://www.simcompanies.com/api/v3/market/0/56/'  # Luxury Car API
    luxury_data = fetch_json(luxury_url)
    luxury_price = extract_price(luxury_data, 'price')
    print("Gathering data for luxury cars...")
    time.sleep(10)

    os.system('cls')

    connect()  # Opens and connect to the database

    #  Insert scrapped data from the website.
    concrete_val = float(sum(concrete_price) / len(concrete_price)) if len(concrete_price) > 0 else concrete_price[0]
    insert_record('Reinforced Concrete', round(concrete_val, 2), get_datetime())

    bricks_val = float(sum(bricks_price) / len(bricks_price)) if len(bricks_price) > 0 else bricks_price[0]
    insert_record('Bricks', round(bricks_val, 2), get_datetime())

    planks_val = float(sum(planks_price) / len(planks_price)) if len(planks_price) > 0 else planks_price[0]
    insert_record('Planks', round(planks_val, 2), get_datetime())

    construction_val = (float(sum(construction_price) / len(construction_price))
                        if len(construction_price) > 0 else construction_price[0])
    insert_record('Construction Units', round(construction_val, 2), get_datetime())

    tablet_val = float(sum(tablet_price) / len(tablet_price)) if len(tablet_price) > 0 else tablet_price[0]
    insert_record('Tablet', round(tablet_val, 2), get_datetime())

    luxury_val = float(sum(luxury_price) / len(luxury_price)) if len(luxury_price) > 0 else luxury_price[0]
    insert_record('Luxury Car', round(luxury_val, 2), get_datetime())


# This function simply gets the latest price and previous price from the market database.
# It then displays the changes on the prices
def price_difference(product):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = '''
    SELECT Price FROM market
    Where Product = ?
    ORDER BY Date DESC
    LIMIT 2
    '''

    try:
        # Query the database
        cursor.execute(query, (product,))
        price = cursor.fetchall()

        # price[0][0] is the latest price while price[1][0] is the previous price
        print(f"\n\t\t{product} \nLatest Price : ${price[0][0]} | Previous Price: ${price[1][0]}")
        if price[0][0] > price[1][0]:
            print(f"Increased by: ${round(price[0][0] - price[1][0], 2)}")
            print(f"Percentage  : {round( ( (price[0][0] - price[1][0]) / price[1][0]) * 100, 3)}%")
        elif price[0][0] < price[1][0]:
            print(f"Decreased by: ${round(price[0][0] - price[1][0], 2)}")
            print(f"Percentage  : {round( ( (price[0][0] - price[1][0]) / price[1][0]) * 100, 3)}%")
        else:
            print(f"Price remained: ${round(price[0][0], 2)}")

    except Exception as e:
        print(f"An error occurred: {e}")

    conn.close()


if __name__ == '__main__':
    while True:
        live_market()
