import tkinter as tk
import sqlite3

# Establish a connection to the SQLite database and create a cursor
conn = sqlite3.connect('railway_reservation.db')
cursor = conn.cursor()

# Function to execute SQL queries based on user input
def execute_query(query, values=None):
    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    return result

# Function to handle the cancellation of a ticket and confirmation of a waiting passenger
def cancel_ticket():
    passenger_ssn = ssn_entry.get()
    train_number = train_number_entry.get()

    # Remove the canceled ticket record
    delete_query = f"DELETE FROM Booked WHERE Passenger_ssn = ? AND Train_Number = ?"
    execute_query(delete_query, (passenger_ssn, train_number))

    # Find a passenger on the waiting list for that train
    waiting_passenger_query = f"SELECT Passenger_ssn FROM Booked WHERE Train_Number = ? AND Status = 'waiting' LIMIT 1"
    waiting_passenger = execute_query(waiting_passenger_query, (train_number,))

    if waiting_passenger:
        # Update the waiting passenger's status to 'confirmed'
        waiting_passenger_ssn = waiting_passenger[0][0]
        update_query = f"UPDATE Booked SET Status = 'confirmed' WHERE Passenger_ssn = ? AND Train_Number = ?"
        execute_query(update_query, (waiting_passenger_ssn, train_number))

        result_label.config(text=f"Ticket canceled for {passenger_ssn}. Passenger {waiting_passenger_ssn} from the waiting list confirmed.")
    else:
        result_label.config(text=f"No waiting passengers for train {train_number}")

# GUI setup
root = tk.Tk()
root.title("Cancel Ticket and Confirm Waiting Passenger")

# Input fields for Passenger SSN and Train Number
ssn_label = tk.Label(root, text="Enter Passenger SSN:")
ssn_label.pack()
ssn_entry = tk.Entry(root)
ssn_entry.pack()

train_number_label = tk.Label(root, text="Enter Train Number:")
train_number_label.pack()
train_number_entry = tk.Entry(root)
train_number_entry.pack()

# Button to trigger canceling a ticket and confirming a waiting passenger
cancel_button = tk.Button(root, text="Cancel Ticket", command=cancel_ticket)
cancel_button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
