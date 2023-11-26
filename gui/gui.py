import tkinter as tk
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('railway_reservation.db')
cursor = conn.cursor()

# Function to execute SQL queries based on user input
def execute_query(query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# # Function to handle user queries
# def handle_query():
#     last_name = last_name_entry.get()
#     first_name = first_name_entry.get()

#     # SQL query to retrieve trains a passenger is booked on based on last name and first name
#     query = f"SELECT dietinct Train.* FROM Train " \
#             f"JOIN Booked ON Train.Train_Number = Booked.Train_Number " \
#             f"JOIN Passenger ON Booked.Passenger_ssn = Passenger.SSN " \
#             f"WHERE Passenger.last_name = '{last_name}' AND Passenger.first_name = '{first_name}'"
    
#     result = execute_query(query)
    
#     # Display the fetched train information in the GUI
#     if result:
#         # Assuming 'result_label' is a label in your GUI to display the fetched data
#         result_label.config(text=str(result))  # Convert the result to string and display in label
#     else:
#         result_label.config(text="No trains found for this passenger")  # If no data found

# # GUI setup
# root = tk.Tk()
# root.title("Retrieve Passenger's Trains")

# # Input fields for last name and first name
# last_name_label = tk.Label(root, text="Enter Last Name:")
# last_name_label.pack()
# last_name_entry = tk.Entry(root)
# last_name_entry.pack()

# first_name_label = tk.Label(root, text="Enter First Name:")
# first_name_label.pack()
# first_name_entry = tk.Entry(root)
# first_name_entry.pack()

# # Button to trigger query execution
# query_button = tk.Button(root, text="Retrieve Trains", command=handle_query)
# query_button.pack()

# # Label to display the query result
# result_label = tk.Label(root, text="")
# result_label.pack()

# Function to handle user queries for passengers on a specific date with confirmed tickets
def handle_query():
    date = date_entry.get()

    # SQL query to retrieve passengers traveling on the entered date with confirmed tickets
    query = f"SELECT distinct Passenger.* FROM Passenger " \
            f"JOIN Booked ON Passenger.SSN = Booked.Passenger_ssn " \
            f"WHERE Passenger.bdate = '{date}' AND Booked.Status = 'Booked'"
    
    result = execute_query(query)
    
    # Display the fetched passenger information in the GUI
    # Display the fetched passenger information in the GUI
    # Display the fetched passenger information in the GUI
    if result:
        # Prepare the result to display each row in a new line
        formatted_result = "\n".join(", ".join(map(str, row)) for row in result)
        
        # Assuming 'result_label' is a label in your GUI to display the fetched data
        result_label.config(text=formatted_result)  # Set the formatted result as the text of the label
    else:
         result_label.config(text="No trains found for this passenger")  # If no data found


# GUI setup
root = tk.Tk()
root.title("Passengers Traveling on a Specific Date")

# Input field for date
date_label = tk.Label(root, text="Enter Date (MM/DD/YY):")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

# Button to trigger query execution
query_button = tk.Button(root, text="Retrieve Passengers", command=handle_query)
query_button.pack()

# Label to display the query result
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
