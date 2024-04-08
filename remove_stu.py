import tkinter as tk
import mysql.connector
from tkinter import messagebox

#connect to MySQL db
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shivusql",
    database="students_details"
)
cursor = conn.cursor()

def remove_student():
    stu_id = int(id_entry.get())
    cursor.execute("DELETE FROM stu_general_details where stu_id=%s", (stu_id,))
    conn.commit()
    messagebox.showinfo("Succes","Student Removed from the Data")
    
#tkinter window
root = tk.Tk()
root.title("Remove Student")

#labels and buttons
id_label = tk.Label(root,text="Enter Student Id to remove:")
id_label.pack()

id_entry = tk.Entry(root, text="Enter Student ID")
id_entry.pack()

remove_button = tk.Button(root, text="Remove Student", command=remove_student)
remove_button.pack()

#mainloop
root.mainloop()

#close the db connection
conn.close()
