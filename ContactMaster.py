import tkinter as tk
from tkinter import messagebox
import sqlite3

class ContactMaster:
    def __init__(self, db_name="contacts.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL)
        ''')
        self.conn.commit()

    def add_contact(self, name, phone):
        self.cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
        self.conn.commit()

    def delete_contact(self, name):
        self.cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
        self.conn.commit()

    def search_contact(self, name):
        self.cursor.execute("SELECT name, phone FROM contacts WHERE name = ?", (name,))
        return self.cursor.fetchone()

    def list_contacts(self):
        self.cursor.execute("SELECT name, phone FROM contacts")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


class ContactMasterApp:
    def __init__(self, root):
        self.contact_master = ContactMaster()

        # GUI setup
        self.root = root
        self.root.title("ContactMaster")

        # Name
        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Phone
        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=3, column=0, padx=5, pady=5)

        self.list_button = tk.Button(root, text="List Contacts", command=self.list_contacts)
        self.list_button.grid(row=3, column=1, padx=5, pady=5)

        # Display Area
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contact_master.add_contact(name, phone)
            self.output_text.insert(tk.END, f"Added contact: Name: {name}, Phone: {phone}\n")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name:
            contact = self.contact_master.search_contact(name)
            if contact:
                self.contact_master.delete_contact(name)
                self.output_text.insert(tk.END, f"Deleted contact: Name: {name}\n")
            else:
                self.output_text.insert(tk.END, "Contact not found.\n")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please enter a name.")

    def search_contact(self):
        name = self.name_entry.get()
        if name:
            contact = self.contact_master.search_contact(name)
            if contact:
                self.output_text.insert(tk.END, f"Found contact: Name: {contact[0]}, Phone: {contact[1]}\n")
            else:
                self.output_text.insert(tk.END, "Contact not found.\n")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please enter a name.")

    def list_contacts(self):
        contacts = self.contact_master.list_contacts()
        self.output_text.insert(tk.END, "\n--- Contact List ---\n")
        if not contacts:
            self.output_text.insert(tk.END, "No contacts available.\n")
        else:
            for contact in contacts:
                self.output_text.insert(tk.END, f"Name: {contact[0]}, Phone: {contact[1]}\n")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def on_close(self):
        self.contact_master.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactMasterApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
