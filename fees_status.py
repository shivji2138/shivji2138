import tkinter as tk
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "shivusql",
    database = "students_details"
)

cursor = conn.cursor()

def see_fees_status():
    stu_id = id_entry.get()
    cursor.execute("SELECT * FROM fees_details WHERE stu_id=%s",(stu_id,))
    status = cursor.fetchone()
    if status:
        result_label.config(text=f"{status}")

#tkinter window
root = tk.Tk()
root.title("Fee Status")

#gui components
label_id = tk.Label(root, text="Enter ID:")
label_id.pack()

id_entry = tk.Entry(root)
id_entry.pack()

see_fee_status = tk.Button(root, text="See Status", bg="purple",fg="white",command = see_fees_status)
see_fee_status.pack()

result_label = tk.Label(root,text="")
result_label.pack()

#mainloop
root.mainloop()

#close db connection
conn.close()
    
    
