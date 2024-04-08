import tkinter as tk
import mysql.connector

def view_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shivusql",
        database="students_details"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM stu_general_details")
    table = cursor.fetchall()

    cursor.close()
    conn.close()

    if table:
        # Clear existing table
        for widget in table_frame.winfo_children():
            widget.destroy()

        # Display table headers with separate sizes for different columns
        headers = [('ID', 5), ('Name', 50), ('Gender', 10), ("%",8), ("STD",8), ("Section",8), ("Age",8)]  # (Column name, Column width)
        for i, (header, width) in enumerate(headers):
            header_label = tk.Label(table_frame, text=header, borderwidth=1, relief="solid", width=width)
            header_label.grid(row=0, column=i)

        # Display table data
        for row_index, row_data in enumerate(table, start=1):
            for col_index, col_data in enumerate(row_data):
                width = headers[col_index][1]  # Get width for this column
                data_label = tk.Label(table_frame, text=col_data, borderwidth=1, relief="solid", width=width)
                data_label.grid(row=row_index, column=col_index)

root = tk.Tk()
root.title("View tables")

table_frame = tk.Frame(root)
table_frame.pack()

view_button = tk.Button(root, text="View Students", command=view_table)
view_button.pack()

root.mainloop()

