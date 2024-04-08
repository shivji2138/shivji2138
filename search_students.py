import tkinter as tk
import mysql.connector

def search_student():
    stu_id = id_entry.get()
    cursor.execute("SELECT * FROM stu_general_details WHERE stu_id=%s", (stu_id,))
    student = cursor.fetchone()
    if student:
        result_label.config(text=f"Student found: {student}")
    else:
        result_label.config(text="Student not found.")

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shivusql",
    database="students_details"
)
cursor = conn.cursor()

# Create Tkinter window
root = tk.Tk()
root.title("Student Search")
root.configure(bg='pink')
root.geometry('300x150')

# Create GUI components
label_name = tk.Label(root, text="Enter ID to search:", bg='pink')
label_name.pack()

id_entry = tk.Entry(root)
id_entry.pack()

search_button = tk.Button(root, text="Search", command=search_student,bg="blue",fg="white")
search_button.pack(pady=10)

result_label = tk.Label(root, text="", bg='pink')
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

# Close the database connection
conn.close()
