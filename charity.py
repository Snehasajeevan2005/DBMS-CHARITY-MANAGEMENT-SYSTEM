import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from PIL import Image, ImageTk
import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sneha@200",
    database="charity_management2"
)
cursor = db.cursor()

# Function to check login credentials
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    # Simulate login check (replace with actual validation)
    if username == "admin" and password == "secret":
        # Login successful, open home window
        login_window.destroy()  # Close login window
        open_home_page()
    else:
        error_label.config(text="Invalid username or password!", fg="red")

# Function to open the home page
def open_home_page():
    global home_window
    home_window = tk.Tk()
    home_window.title("Charity Management System - Home")

    # Load background image for home screen
    home_background_image = Image.open("home5.jpg")  # Replace with your image path
    resized_home_image = home_background_image.resize((1400, 650))
    home_background_image = ImageTk.PhotoImage(resized_home_image)
    
    # Keep a reference to the image object
    home_window.home_background_image = home_background_image

    # Create a label for the home screen background image
    home_background_label = tk.Label(home_window, image=home_background_image)
    home_background_label.place(relwidth=1, relheight=1)

    # Create buttons for donor, receiver, and logout
    donor_button = tk.Button(home_window, text="Donor", command=open_donor_page, font=("Helvetica", 16), width=15, height=2)
    donor_button.place(x=150, y=150)

    receiver_button = tk.Button(home_window, text="Receiver", command=open_receiver_page, font=("Helvetica", 16), width=15, height=2)
    receiver_button.place(x=150, y=230)

    logout_button = tk.Button(home_window, text="Logout", command=logout_function, font=("Helvetica", 16), width=15, height=2)
    logout_button.place(x=150, y=310)

    home_window.mainloop()

# Function to open the donor detail page
def open_donor_page():
    donor_window = tk.Toplevel()
    donor_window.title("Donor Details")

    # Load background image for donor detail page
    donor_background_image = Image.open("home5.jpg")  # Replace with your image path
    resized_donor_image = donor_background_image.resize((1400, 650))
    donor_background_image = ImageTk.PhotoImage(resized_donor_image)

    # Keep a reference to the image object
    donor_window.donor_background_image = donor_background_image

    # Create a label for the donor detail page background image
    donor_background_label = tk.Label(donor_window, image=donor_background_image)
    donor_background_label.place(relwidth=1, relheight=1)

    # Donor name label and entry
    donor_name_label = tk.Label(donor_window, text="Donor Name:", font=("Helvetica", 12))
    donor_name_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    donor_name_entry = tk.Entry(donor_window, font=("Helvetica", 12), width=30)
    donor_name_entry.grid(row=0, column=1, padx=10, pady=10)

    # Contact number label and entry
    donor_contact_label = tk.Label(donor_window, text="Contact Number:", font=("Helvetica", 12))
    donor_contact_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    donor_contact_entry = tk.Entry(donor_window, font=("Helvetica", 12), width=30)
    donor_contact_entry.grid(row=1, column=1, padx=10, pady=10)

    # Email label and entry
    donor_email_label = tk.Label(donor_window, text="Email:", font=("Helvetica", 12))
    donor_email_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    donor_email_entry = tk.Entry(donor_window, font=("Helvetica", 12), width=30)
    donor_email_entry.grid(row=2, column=1, padx=10, pady=10)

    # Address label and entry
    address_label = tk.Label(donor_window, text="Address:", font=("Helvetica", 12))
    address_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    address_entry = tk.Entry(donor_window, font=("Helvetica", 12), width=30)
    address_entry.grid(row=3, column=1, padx=10, pady=10)

    # Donation item label and entry
    donation_item_label = tk.Label(donor_window, text="Donating Item:", font=("Helvetica", 12))
    donation_item_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    donation_item_entry = tk.Entry(donor_window, font=("Helvetica", 12), width=30)
    donation_item_entry.grid(row=4, column=1, padx=10, pady=10)

    # Date label and entry
    date_label = tk.Label(donor_window, text="Date:", font=("Helvetica", 12))
    date_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    date_entry = tk.Entry(donor_window, font=("Helvetica", 12), width=30)
    date_entry.grid(row=5, column=1, padx=10, pady=10)

    # Save button
    save_button = tk.Button(donor_window, text="Save", command=lambda: save_details("donor", donor_name_entry.get(), donor_contact_entry.get(), donor_email_entry.get(), address_entry.get(), donation_item_entry.get(), date_entry.get()), font=("Helvetica", 12))
    save_button.grid(row=6, column=0, padx=10, pady=10)

    # View button
    view_button = tk.Button(donor_window, text="View", command=view_donor_details, font=("Helvetica", 12))
    view_button.grid(row=6, column=1, padx=10, pady=10)

    # Modify button
    modify_button = tk.Button(donor_window, text="Modify", command=lambda: ask_and_modify_donor(donor_name_entry.get(), donor_contact_entry.get(), donor_email_entry.get(), address_entry.get(), donation_item_entry.get(), date_entry.get()), font=("Helvetica", 12))
    modify_button.grid(row=7, column=0, padx=10, pady=10)

    # Delete button
    delete_button = tk.Button(donor_window, text="Delete", command=lambda: ask_and_delete_donor(donor_name_entry.get()), font=("Helvetica", 12))
    delete_button.grid(row=7, column=1, padx=10, pady=10)

# Function to open the receiver detail page
def open_receiver_page():
    receiver_window = tk.Toplevel()
    receiver_window.title("Receiver Details")

    # Load background image for receiver detail page
    receiver_background_image = Image.open("home5.jpg")  # Replace with your image path
    resized_receiver_image = receiver_background_image.resize((1400, 650))
    receiver_background_image = ImageTk.PhotoImage(resized_receiver_image)

    # Keep a reference to the image object
    receiver_window.receiver_background_image = receiver_background_image

    # Create a label for the receiver detail page background image
    receiver_background_label = tk.Label(receiver_window, image=receiver_background_image)
    receiver_background_label.place(relwidth=1, relheight=1)

    # Receiver name label and entry
    receiver_name_label = tk.Label(receiver_window, text="Receiver Name:", font=("Helvetica", 12))
    receiver_name_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    receiver_name_entry = tk.Entry(receiver_window, font=("Helvetica", 12), width=30)
    receiver_name_entry.grid(row=0, column=1, padx=10, pady=10)

    # Contact number label and entry
    receiver_contact_label = tk.Label(receiver_window, text="Contact Number:", font=("Helvetica", 12))
    receiver_contact_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    receiver_contact_entry = tk.Entry(receiver_window, font=("Helvetica", 12), width=30)
    receiver_contact_entry.grid(row=1, column=1, padx=10, pady=10)

    # Email label and entry
    receiver_email_label = tk.Label(receiver_window, text="Email:", font=("Helvetica", 12))
    receiver_email_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    receiver_email_entry = tk.Entry(receiver_window, font=("Helvetica", 12), width=30)
    receiver_email_entry.grid(row=2, column=1, padx=10, pady=10)

    # Address label and entry
    address_label = tk.Label(receiver_window, text="Address:", font=("Helvetica", 12))
    address_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    address_entry = tk.Entry(receiver_window, font=("Helvetica", 12), width=30)
    address_entry.grid(row=3, column=1, padx=10, pady=10)

    # Received item label and entry
    received_item_label = tk.Label(receiver_window, text="Received Item:", font=("Helvetica", 12))
    received_item_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    received_item_entry = tk.Entry(receiver_window, font=("Helvetica", 12), width=30)
    received_item_entry.grid(row=4, column=1, padx=10, pady=10)

    # Date label and entry
    date_label = tk.Label(receiver_window, text="Date:", font=("Helvetica", 12))
    date_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    date_entry = tk.Entry(receiver_window, font=("Helvetica", 12), width=30)
    date_entry.grid(row=5, column=1, padx=10, pady=10)

    # Save button
    save_button = tk.Button(receiver_window, text="Save", command=lambda: save_details("receiver", receiver_name_entry.get(), receiver_contact_entry.get(), receiver_email_entry.get(), address_entry.get(), received_item_entry.get(), date_entry.get()), font=("Helvetica", 12))
    save_button.grid(row=6, column=0, padx=10, pady=10)

    # View button
    view_button = tk.Button(receiver_window, text="View", command=view_receiver_details, font=("Helvetica", 12))
    view_button.grid(row=6, column=1, padx=10, pady=10)

    # Modify button
    modify_button = tk.Button(receiver_window, text="Modify", command=lambda: ask_and_modify_receiver(receiver_name_entry.get(), receiver_contact_entry.get(), receiver_email_entry.get(), address_entry.get(), received_item_entry.get(), date_entry.get()), font=("Helvetica", 12))
    modify_button.grid(row=7, column=0, padx=10, pady=10)

    # Delete button
    delete_button = tk.Button(receiver_window, text="Delete", command=lambda: ask_and_delete_receiver(receiver_name_entry.get()), font=("Helvetica", 12))
    delete_button.grid(row=7, column=1, padx=10, pady=10)

# Function to save donor or receiver details
def save_details(user_type, name, contact, email, address, item, date):
    try:
        if user_type == "donor":
            cursor.execute("INSERT INTO donors (name, contact, email, address, donation_item, date) VALUES (%s, %s, %s, %s, %s, %s)", (name, contact, email, address, item, date))
        else:
            cursor.execute("INSERT INTO receivers (name, contact, email, address, received_item, date) VALUES (%s, %s, %s, %s, %s, %s)", (name, contact, email, address, item, date))
        db.commit()
        messagebox.showinfo("Success", f"{user_type.capitalize()} details saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to view donor details
def view_donor_details():
    view_window = tk.Toplevel()
    view_window.title("View Donor Details")

    cursor.execute("SELECT * FROM donors")
    rows = cursor.fetchall()

    tree = ttk.Treeview(view_window, columns=("ID", "Name", "Contact", "Email", "Address", "Donation Item", "Date"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Contact", text="Contact")
    tree.heading("Email", text="Email")
    tree.heading("Address", text="Address")
    tree.heading("Donation Item", text="Donation Item")
    tree.heading("Date", text="Date")
    
    for row in rows:
        tree.insert("", tk.END, values=row)
    
    tree.pack(fill=tk.BOTH, expand=True)

# Function to view receiver details
def view_receiver_details():
    view_window = tk.Toplevel()
    view_window.title("View Receiver Details")

    cursor.execute("SELECT * FROM receivers")
    rows = cursor.fetchall()

    tree = ttk.Treeview(view_window, columns=("ID", "Name", "Contact", "Email", "Address", "Received Item", "Date"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Contact", text="Contact")
    tree.heading("Email", text="Email")
    tree.heading("Address", text="Address")
    tree.heading("Received Item", text="Received Item")
    tree.heading("Date", text="Date")
    
    for row in rows:
        tree.insert("", tk.END, values=row)
    
    tree.pack(fill=tk.BOTH, expand=True)

# Function to ask for donor ID and modify donor details
def ask_and_modify_donor(name, contact, email, address, donation_item, date):
    donor_id = simpledialog.askinteger("Input", "Enter Donor ID to Modify:")
    if donor_id:
        modify_donor_details(donor_id, name, contact, email, address, donation_item, date)

# Function to modify donor details
def modify_donor_details(donor_id, name, contact, email, address, donation_item, date):
    cursor.execute("UPDATE donors SET name=%s, contact=%s, email=%s, address=%s, donation_item=%s, date=%s WHERE id=%s", (name, contact, email, address, donation_item, date, donor_id))
    db.commit()
    messagebox.showinfo("Success", "Donor details updated successfully!")
    view_donor_details()

# Function to ask for donor ID and delete donor details
def ask_and_delete_donor(name):
    donor_id = simpledialog.askinteger("Input", "Enter Donor ID to Delete:")
    if donor_id:
        delete_donor_details(donor_id)

# Function to delete donor details
def delete_donor_details(donor_id):
    cursor.execute("DELETE FROM donors WHERE id=%s", (donor_id,))
    db.commit()
    messagebox.showinfo("Success", "Donor details deleted successfully!")
    view_donor_details()

# Function to ask for receiver ID and modify receiver details
def ask_and_modify_receiver(name, contact, email, address, received_item, date):
    receiver_id = simpledialog.askinteger("Input", "Enter Receiver ID to Modify:")
    if receiver_id:
        modify_receiver_details(receiver_id, name, contact, email, address, received_item, date)

# Function to modify receiver details
def modify_receiver_details(receiver_id, name, contact, email, address, received_item, date):
    cursor.execute("UPDATE receivers SET name=%s, contact=%s, email=%s, address=%s, received_item=%s, date=%s WHERE id=%s", (name, contact, email, address, received_item, date, receiver_id))
    db.commit()
    messagebox.showinfo("Success", "Receiver details updated successfully!")
    view_receiver_details()

# Function to ask for receiver ID and delete receiver details
def ask_and_delete_receiver(name):
    receiver_id = simpledialog.askinteger("Input", "Enter Receiver ID to Delete:")
    if receiver_id:
        delete_receiver_details(receiver_id)

# Function to delete receiver details
def delete_receiver_details(receiver_id):
    cursor.execute("DELETE FROM receivers WHERE id=%s", (receiver_id,))
    db.commit()
    messagebox.showinfo("Success", "Receiver details deleted successfully!")
    view_receiver_details()

# Function to handle logout
def logout_function():
    home_window.destroy()
    open_login_page()

# Function to open the login page
def open_login_page():
    global login_window
    login_window = tk.Tk()
    login_window.title("Charity Management System - Login")

    # Load background image
    background_image = Image.open("charity.jpg")  # Replace with your image path
    resized_image = background_image.resize((1400, 650))
    background_image = ImageTk.PhotoImage(resized_image)
    
    # Keep a reference to the image object
    login_window.background_image = background_image

    # Create a label for the background image
    background_label = tk.Label(login_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Create login form
    login_frame = tk.Frame(login_window, bg="white", padx=20, pady=20)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    username_label = tk.Label(login_frame, text="Username:", font=("Helvetica", 14))
    username_label.grid(row=0, column=0, pady=10)
    global username_entry
    username_entry = tk.Entry(login_frame, font=("Helvetica", 14))
    username_entry.grid(row=0, column=1, pady=10)

    password_label = tk.Label(login_frame, text="Password:", font=("Helvetica", 14))
    password_label.grid(row=1, column=0, pady=10)
    global password_entry
    password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 14))
    password_entry.grid(row=1, column=1, pady=10)

    login_button = tk.Button(login_frame, text="Login", command=check_login, font=("Helvetica", 14), width=10)
    login_button.grid(row=2, columnspan=2, pady=10)

    global error_label
    error_label = tk.Label(login_frame, text="", font=("Helvetica", 12))
    error_label.grid(row=3, columnspan=2)

    login_window.mainloop()

# Start the application
open_login_page()