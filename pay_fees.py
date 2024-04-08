import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shivusql",
    database="students_details"
)

cursor = conn.cursor()

def see_stu_fee_detail():
    stu_id = id_entry.get()
    amount_paid = float(money_entry.get())
    cursor.execute("SELECT balance_fees, paid_fees FROM fees_details WHERE stu_id=%s", (stu_id,))
    row = cursor.fetchone()
    if row:
        balance = row[0] - amount_paid
        total_paid_fee = row[1] + amount_paid
        result_label.config(text=f"Balance: {balance}")
        # Update the balance and total paid fees in the fees_details table
        sql = "UPDATE fees_details SET balance_fees = %s, paid_fees = %s WHERE stu_id = %s"
        val = (balance, total_paid_fee, stu_id)
        cursor.execute(sql, val)
        conn.commit()
    else:
        messagebox.showerror("Error", "Student ID not found")

#create tkinter window
root = tk.Tk()
root.title("Pay Fees")

#create gui components
id_label =tk.Label(root, text="Enter Student ID")
id_label.pack()

id_entry = tk.Entry(root)
id_entry.pack()

money_label = tk.Label(root, text="Enter the Amount:")
money_label.pack()

money_entry = tk.Entry(root)
money_entry.pack()

pay_button = tk.Button(root, text="Pay Now",command=see_stu_fee_detail)
pay_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

#mainloop
root.mainloop()

#close the db connection
conn.close()
