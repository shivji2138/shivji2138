import mysql.connector
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Establish database connection
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shivusql",
        database="students_details"
    )
except mysql.connector.Error as err:
    print("ERROR:", err)
    messagebox.showerror("Error", f"Database connection error: {err}")
    exit()

# Create the main window
root = tk.Tk()
root.title("Student BioData Entry Form")

# Function to insert data into the database
def insert_data():
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO biodata(stu_id, stu_name, dob, age, std, blood_group, aadhaar_num, father_name, mother_name, fathers_occupation, mothers_occupation, annual_income, residential_address, mobile_num, parent_email, student_email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (
            int(student_id_entry.get()),
            name_entry.get(),
            datetime.strptime(dob_entry.get(), "%Y-%m-%d").date(),
            int(age_entry.get()),
            std_entry.get(),
            blood_group_entry.get(),
            int(aadhaar_num_entry.get()),
            father_name_entry.get(),
            mother_name_entry.get(),
            fathers_occupation_entry.get(),
            mothers_occupation_entry.get(),
            annual_income_entry.get(),
            residential_address_entry.get(),
            mobile_num_entry.get(),
            parent_email_entry.get(),
            student_email_entry.get()
        )
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Success", "Successfully added data.")
    except mysql.connector.Error as err:
        print("ERROR:", err)
        messagebox.showerror("Error", f"Error: {err}")

# Function to handle button click event
def submit_button_click():
    insert_data()

# Create labels and entry fields
tk.Label(root, text="Student ID:").grid(row=0, column=0, padx=10, pady=5)
student_id_entry = tk.Entry(root)
student_id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Date Of Birth:").grid(row=2, column=0, padx=10, pady=5)
dob_entry = tk.Entry(root)
dob_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Blood Group:").grid(row=3, column=0, padx=10, pady=5)
blood_group_entry = tk.Entry(root)
blood_group_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Standard:").grid(row=4, column=0, padx=10, pady=5)
std_entry = tk.Entry(root)
std_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Aadhaar Number:").grid(row=5, column=0, padx=10, pady=5)
aadhaar_num_entry = tk.Entry(root)
aadhaar_num_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=6, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Father Name:").grid(row=7, column=0, padx=10, pady=5)
father_name_entry = tk.Entry(root)
father_name_entry.grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="Mother Name:").grid(row=8, column=0, padx=10, pady=5)
mother_name_entry = tk.Entry(root)
mother_name_entry.grid(row=8, column=1, padx=10, pady=5)

tk.Label(root, text="Father's Occupation:").grid(row=9, column=0, padx=10, pady=5)
fathers_occupation_entry = tk.Entry(root)
fathers_occupation_entry.grid(row=9, column=1, padx=10, pady=5)

tk.Label(root, text="Mother's Occupation:").grid(row=10, column=0, padx=10, pady=5)
mothers_occupation_entry = tk.Entry(root)
mothers_occupation_entry.grid(row=10, column=1, padx=10, pady=5)

tk.Label(root, text="Annual Income:").grid(row=11, column=0, padx=10, pady=5)
annual_income_entry = tk.Entry(root)
annual_income_entry.grid(row=11, column=1, padx=10, pady=5)

tk.Label(root, text="Residential Address:").grid(row=12, column=0,padx=10,pady=5)
residential_address_entry = tk.Entry(root)
residential_address_entry.grid(row=12, column=1, padx=10, pady=5)

tk.Label(root, text="Mobile Number:").grid(row=13, column=0,padx=10,pady=5)
mobile_num_entry = tk.Entry(root)
mobile_num_entry.grid(row=13,column=1,padx=10,pady=5)

tk.Label(root, text="Parent's Email:").grid(row=14, column=0,padx=10,pady=5)
parent_email_entry = tk.Entry(root)
parent_email_entry.grid(row=14, column=1, padx=10, pady=5)

tk.Label(root,text="Student's Email:").grid(row=15,column=0,padx=10,pady=5)
student_email_entry = tk.Entry(root)
student_email_entry.grid(row=15, column=1,padx=10,pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_button_click, bg="green", fg="white")
submit_button.grid(row=16, column=0, columnspan=2, pady=10)

root.mainloop()
