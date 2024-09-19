import sqlite3
from datetime import datetime


# This function is for getting the date and time.
# Mainly for identifying on what date the products and prices are extracted from the sim-co API.
def get_datetime():
    now = datetime.now()
    formatted_date_time = now.strftime("%m-%d-%y %H:%M")
    return formatted_date_time


# This function mainly creates the first database if it does not exist. Useless as of 08/09/2024.
def connect():
    # Connect to a database (or create it if it doesn't exist)
    conn = sqlite3.connect('database.db')

    # Create a cursor object using the connection
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS market (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Product TEXT NOT NULL,
        Price INTEGER NOT NULL,
        Date TEXT NOT NULL
    )
    ''')

    # Commit the changes
    conn.commit()
    conn.close()


# This function inserts the data extracted to the database.
def insert_record(product, price, date):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        # Insert a record
        cursor.execute('''
        INSERT INTO market (Product, Price, Date) VALUES (?, ?, ?)
        ''', (product, price, date))

        # Commit the changes
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: A record with Price {price} already exists.")

    conn.close()


# This function fetches all the data from the database then prints it.
def fetch_query(query):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        # Query the database
        cursor.execute(f'SELECT {query} FROM market')
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Exception as e:
        print(f"An error occurred: {e}")

    conn.close()


# This function fetches the most recent price of the product_name and returns it.
def fetch_one(product_name):
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    # Filtering by Product and Price, then extracting the latest data.
    query = '''
    SELECT Product, Price
    FROM market
    WHERE Product = ?
    ORDER BY Date DESC
    LIMIT 1;
    '''

    cursor.execute(query, (product_name,))

    latest_record = cursor.fetchone()

    conn.close()

    # Returns the Price.
    return latest_record[1]


# This function is responsible for tracking and recording all prices of the products in realtime.

