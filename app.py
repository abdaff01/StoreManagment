import sqlite3
import tkinter as tk

import tkinter as tk
from tkinter import ttk


###############################################3
import sqlite3

# Connect to the database
conn = sqlite3.connect("store.db")

# Create a cursor
cursor = conn.cursor()

# Create the "products" table
# query = """
# CREATE TABLE products (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     type TEXT NOT NULL,
#     size INTEGER NOT NULL,
#     date DATE NOT NULL
# );
# """
# cursor.execute(query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

################################################################
# Connect to the database
conn = sqlite3.connect('store.db')

# Create a cursor object to execute queries
cursor = conn.cursor()

# Create the main window
window = tk.Tk()
window.title("Store Management")

# Create the display window
display_frame = tk.Frame(window)
display_frame.pack()

# Create the products table
table = ttk.Treeview(window)
table["columns"] = ("id", "name", "type", "size", "date")
table.column("id", width=50)
table.column("name", width=150)
table.column("type", width=100)
table.column("size", width=100)
table.column("date", width=100)
table.heading("id", text="ID")
table.heading("name", text="Name")
table.heading("type", text="Type")
table.heading("size", text="Size")
table.heading("date", text="Date")
table.pack()

# Define a function to load the products table
def load_table():
    # Clear the current rows in the table
    for i in table.get_children():
        table.delete(i)

    # Execute a SELECT query to retrieve all products
    query = "SELECT * FROM products"
    cursor.execute(query)

    # Loop through the results and add them to the table
    for row in cursor:
        table.insert("", "end", values=row)

# Add a search field
search_label = tk.Label(display_frame, text="Search:")
search_label.pack()
search_entry = tk.Entry(display_frame)
search_entry.pack()

# Create the search button
search_button = tk.Button(window, text="Search")
search_button.pack()



# Define the logic for the "Choosing type " button
def open_window_types():
    # Open a new window
    new_window = tk.Toplevel(window)
    new_window.title("Please choose the type you wanna add")

    # Create the first button
    button1 = tk.Button(new_window, text="Type S")
    button1.pack()

    # Create the second button
    button2 = tk.Button(new_window, text="Type R")
    button2.pack()
    # Assign the "Add" button logic to the button
    button1.config(command=add_product)


# Define the logic for the search button
def search_products():
    # Retrieve the search query from the search field
    query = search_entry.get()

    # Clear the current rows in the table
    for i in table.get_children():
        table.delete(i)

    # Execute a SELECT query to search for products
    search_query = "SELECT * FROM products WHERE name LIKE ? OR type LIKE ? OR size LIKE ? OR date LIKE ?"
    search_values = ("%" + query + "%", "%" + query + "%", "%" + query + "%", "%" + query + "%")
    cursor.execute(search_query, search_values)

    # Loop through the results and add them to the table
    for row in cursor:
        table.insert("", "end", values=row)

# Assign the search button logic to the button
search_button.config(command=search_products)

# Add a filter icon
filter_label = tk.Label(display_frame, text="Filter:")
filter_label.pack()
filter_entry = tk.Entry(display_frame)
filter_entry.pack()

# Add a button to add a new product
# add_button = tk.Button(window, text="Open Window", command=open_window_types)
# add_button.pack()

# Add a button to add a new product
modify_button = tk.Button(display_frame, text="Add", command=open_window_types)
modify_button.pack()

# Add a button to modify a selected product
modify_button = tk.Button(display_frame, text="Modify")
modify_button.pack()

# Add a button to delete a selected product
delete_button = tk.Button(display_frame, text="Delete")
delete_button.pack()

# Add a button to display the details of a selected product
details_button = tk.Button(display_frame, text="Details")
details_button.pack()


# Define the logic for the "Add" button
def add_product():
    # Open a new window to add a new product
    add_window = tk.Toplevel(window)
    add_window.title("Add Product")

    # Add a field for the product name
    name_label = tk.Label(add_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()

    # Add a field for the product type
    type_label = tk.Label(add_window, text="Type:")
    type_label.pack()
    type_entry = tk.Entry(add_window)
    type_entry.pack()

    # Add a field for the product size
    size_label = tk.Label(add_window, text="Size:")
    size_label.pack()
    size_entry = tk.Entry(add_window)
    size_entry.pack()

    # Add a field for the product date
    date_label = tk.Label(add_window, text="Date:")
    date_label.pack()
    date_entry = tk.Entry(add_window)
    date_entry.pack()

    # Add a button to save the new product
    save_button = tk.Button(add_window, text="Save",
                            command=lambda: save_product(add_window, name_entry.get(), type_entry.get(),
                                                         size_entry.get(), date_entry.get()))
    save_button.pack()

    # Define the logic for the "Save" button in the "Add" window
    def save_product(add_window, name, product_type, size, date):
        # Insert the new product into the database
        query = "INSERT INTO products (name, type, size, date) VALUES (?, ?, ?, ?)"
        values = (name, product_type, size, date)
        cursor.execute(query, values)
        conn.commit()

        # Close the "Add" window
        add_window.destroy()

        # Reload the table in the main window
        load_table()

    # Create the "Save" button in the "Add" window
    save_button = tk.Button(add_window, text="Save")
    save_button.pack()

    # Assign the "Save" button logic to the button
    save_button.config(command=lambda: save_product(add_window, name_entry.get(), type_entry.get(), size_entry.get(),
                                                    date_entry.get()))


# Define the logic for the "Save" button in the "Add" window
def save_product(add_window, name, product_type, size, date):
    # Insert the new product into the database
    query = "INSERT INTO products (name, type, size, date) VALUES (?, ?, ?, ?)"
    values = (name, product_type, size, date)
    cursor.execute(query, values)
    conn.commit()

    # Close the "Add" window
    add_window.destroy()

    # Reload the table in the main window
    load_table()

# Define a function to load the products table
def load_table():
    # Clear the current rows in the table
    for i in table.get_children():
        table.delete(i)

    # Execute a SELECT query to retrieve all products
    query = "SELECT * FROM products"
    cursor.execute(query)

    # Loop through the results and add them to the table
    for row in cursor:
        table.insert("", "end", values=row)
    #
    # # Assign the "Save" button logic to the button
    # save_button.config(command=lambda: save_product(add_window, name_entry.get(), type_entry.get(), size_entry.get(), date_entry.get()))





# Define the logic for the "Modify" button
def modify_product():
    # Open a new window to modify a selected product
    modify_window = tk.Toplevel(window)
    modify_window.title("Modify Product")

    # Add a field for the product name
    name_label = tk.Label(modify_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(modify_window)
    name_entry.pack()

    # Add a field for the product type
    type_label = tk.Label(modify_window, text="Type:")
    type_label.pack()
    type_entry = tk.Entry(modify_window)
    type_entry.pack()

    # Add a field for the product size
    size_label = tk.Label(modify_window, text="Size:")
    size_label.pack()
    size_entry = tk.Entry(modify_window)
    size_entry.pack()

    # Add a field for the product date
    date_label = tk.Label(modify_window, text="Date:")
    date_label.pack()
    date_entry = tk.Entry(modify_window)
    date_entry.pack()

    # Add a button to save the modified product
    save_button = tk.Button(modify_window, text="Save",
                            command=lambda: save_modified_product(name_entry.get(), type_entry.get(), size_entry.get(),
                                                                  date_entry.get()))
    save_button.pack()

# Assign the "Modify" button logic to the button
modify_button.config(command=modify_product)

# Define the logic for the "Save" button in the "Modify" window
def save_modified_product(name, product_type, size, date):
    # Update the modified product in the database
    query = "UPDATE products SET name=?, type=?, size=?, date=? WHERE id=?"
    values = (name, product_type, size, date, selected_product_id)
    cursor.execute(query, values)
    conn.commit()

    # Close the "Modify" window
    modify_window.destroy()


# Define the logic for the "Delete" button
def delete_product():
    # Delete the selected product from the database
    query = "DELETE FROM products WHERE id=?"
    values = (selected_product_id,)
    cursor.execute(query, values)
    conn.commit()

# Assign the "Delete" button logic to the button
delete_button.config(command=delete_product)

# Define the logic for the "Details" button
def display_details():
    # Open a new window to display the details of a selected product
    details_window = tk.Toplevel(window)
    details_window.title("Product Details")

    # Query the database to retrieve the details of the selected product
    query = "SELECT * FROM products WHERE id=?"
    values = (selected_product_id,)
    cursor.execute(query, values)
    result = cursor.fetchone()

    # Extract the product details from the result
    name = result[1]
    product_type = result[2]
    size = result[3]
    date = result[4]

    # Display the product details in the "Details" window
    name_label = tk.Label(details_window, text=f"Name: {name}")
    name_label.pack()
    type_label = tk.Label(details_window, text=f"Type: {product_type}")
    type_label.pack()
    size_label = tk.Label(details_window, text=f"Size: {size}")
    size_label.pack()
    date_label = tk.Label(details_window, text=f"Date: {date}")
    date_label.pack()

# Assign the "Details" button logic to the button
details_button.config(command=display_details)

# Start the main loop
window.mainloop()

# Close the connection to the database
conn.close()
