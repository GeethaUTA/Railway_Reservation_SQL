import sqlite3
import csv

# Create a connection to the SQLite database
conn = sqlite3.connect('railway_reservation.db')
cursor = conn.cursor()

# Create tables for Train, Train_Status, Passenger, and Booked
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Train (
        Train_Number INTEGER PRIMARY KEY,
        Train_Name TEXT,
        Premium_Fair REAL,
        General_Fair REAL,
        Source_Station TEXT,
        Destination_Station TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Train_Status (
        TrainDate TEXT,
        TrainName TEXT,
        PremiumSeatsAvailable INTEGER,
        GenSeatsAvailable INTEGER,
        PremiumSeatsOccupied INTEGER,
        GenSeatsOccupied INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Passenger (
        first_name TEXT,
        last_name TEXT,
        address TEXT,
        city TEXT,
        county TEXT,
        phone TEXT,
        SSN TEXT PRIMARY KEY,
        bdate TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Booked (
        Passenger_ssn TEXT,
        Train_Number INTEGER,
        Ticket_Type TEXT,
        Status TEXT
    )
''')

# Function to insert data from CSV into the database
def insert_data_from_csv(file_name, table_name):
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            placeholders = ','.join('?' * len(row))
            query = f"INSERT OR REPLACE INTO {table_name} VALUES ({placeholders})"
            cursor.execute(query, row)

# Replace 'Train.csv', 'Train_Status.csv', 'Passenger.csv', 'Booked.csv' with actual file names
insert_data_from_csv(r'C:\Users\DELL\Desktop\Foundations_Of_Computing\RRS\Train.csv', 'Train')
insert_data_from_csv(r'C:\Users\DELL\Desktop\Foundations_Of_Computing\RRS\Train_Status.csv', 'Train_Status')
insert_data_from_csv(r'C:\Users\DELL\Desktop\Foundations_Of_Computing\RRS\Passenger.csv', 'Passenger')
insert_data_from_csv(r'C:\Users\DELL\Desktop\Foundations_Of_Computing\RRS\booked.csv', 'Booked')

# Commit changes and close the connection
conn.commit()
conn.close()

