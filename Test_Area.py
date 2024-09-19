import sqlite3


# Connect to the database
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
        cursor.execute(query, (product, ))
        price = cursor.fetchall()

        print(f"\nLatest Price :{price[0][0]} | Previous Price: {price[1][0]}")
        if price[0][0] > price[1][0]:
            print(f"{product} increased by: {round(price[0][0] - price[1][0], 2)}")
        elif price[0][0] < price[1][0]:
            print(f"{product} decreased by: {round(price[0][0] - price[1][0], 2)}")

    except Exception as e:
        print(f"An error occurred: {e}")

    conn.close()


price_difference('Reinforced Concrete')
