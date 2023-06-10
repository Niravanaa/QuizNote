import os
import re
import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

# Function to format content as code block
def format_code(content):
    return "```" + content + "```"

# Function to save notes to file
def save_notes(filename, content):
    try:
        with open(filename, "a") as file:
            file.write(content + "\n\n")
    except IOError:
        messagebox.showerror("File Error", "Unable to save notes to the file.")

# Function to search for keywords in notes
def search_notes(filename, keyword):
    try:
        with open(filename, "r") as file:
            notes = file.read()
            matches = re.findall(r"\b" + re.escape(keyword) + r"\b", notes, re.IGNORECASE)
            return matches
    except IOError:
        messagebox.showerror("File Error", "Unable to search for notes in the file.")

# Function to open the notes file
def open_notes(filename):
    actualFilename = os.path.join(script_dir, filename)
    if os.path.exists(actualFilename):
        webbrowser.open(actualFilename)
    else:
        messagebox.showerror("File Error", "File does not exist.")

def save_button_click():
    section = section_entry.get()
    content = content_text.get("1.0", tk.END).strip()
    if section == "":
        messagebox.showwarning("Section Error", "Please enter a section name.")
        return
    if content == "":
        messagebox.showwarning("Content Error", "Please enter the content.")
        return

    mode = mode_var.get()
    chapter = chapter_entry.get()

    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    filename = os.path.join(script_dir, f"{mode}_{chapter}_notes.txt")

    if mode == "ethics":
        information = 'Act as though you were a PhD holding Engineer professor teaching a Sustainable Development and Environmental Stewardship course. Teach me the following information of the SECTION section of the CHAPTER chapter of my textbook: '
    elif mode == "datastruct":
        information = 'Act as though you were a PhD holding Computer Science professor teaching a Java Data Structures and Algorithms course. Teach me the following information of the SECTION section of the CHAPTER chapter of my textbook. If your explanations can be supplemented by code, provide me amazing code examples:'
    elif mode == "principle":
        information = 'Act as though you were a PhD holding Computer Science professor teaching a Principles of Programming Languages course. Teach me the following information of the SECTION section of the CHAPTER chapter of my textbook. If your explanations can be supplemented by code, provide me amazing code examples:'
    else:
        return

    information = information.replace("SECTION", section)
    information = information.replace("CHAPTER", chapter)

    # Formatting options
    if format_var.get() == "Code Block":
        content = format_code(content)

    # Replace newlines with spaces
    content = content.replace("\n", " ")

    # Save notes
    save_notes(filename, information + '"' + content + '"')

    section_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)

def search_button_click():
    keyword = search_entry.get()
    if keyword == "":
        messagebox.showwarning("Keyword Error", "Please enter a keyword to search.")
        return

    try:
        matches = search_notes(filename_entry.get(), keyword)
        if matches:
            messagebox.showinfo("Search Results", "Keyword matches found in the following sections:\n\n" + "\n".join(matches))
        else:
            messagebox.showinfo("Search Results", "No matches found.")
    except IOError:
        messagebox.showerror("File Error", "Unable to search for notes in the file.")

def open_button_click():
    try:
        open_notes(filename_entry.get())
    except IOError:
        messagebox.showerror("File Error", "Unable to open the notes file.")

# Create the main window
window = tk.Tk()
window.title("Note Taking App")
window.geometry("500x400")

# Set window background color
window.configure(bg="#f0f0f0")

# Create a style for the widgets
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TScrolledText", font=("Arial", 12))

# Create and pack the title label
title_label = ttk.Label(window, text="Note Taking App", font=("Arial", 16, "bold"), background="#f0f0f0")
title_label.pack(pady=10)

# Create and pack the class mode selection widget
mode_label = ttk.Label(window, text="Class Mode:")
mode_label.pack()
mode_var = tk.StringVar()
mode_combobox = ttk.Combobox(window, textvariable=mode_var, state="readonly")
mode_combobox["values"] = ("ethics", "datastruct", "principle")
mode_combobox.pack(pady=5)

# Create and pack the chapter entry widget
chapter_label = ttk.Label(window, text="Chapter:")
chapter_label.pack()
chapter_entry = ttk.Entry(window)
chapter_entry.pack(pady=5)

# Create and pack the filename entry widget
filename_label = ttk.Label(window, text="Output File:")
filename_label.pack()
filename_entry = ttk.Entry(window)
filename_entry.pack(pady=5)

# Create and pack the format selection widget
format_label = ttk.Label(window, text="Format:")
format_label.pack()
format_var = tk.StringVar()
format_radio_text = ttk.Radiobutton(window, text="Regular Text", variable=format_var, value="Regular Text")
format_radio_text.pack()
format_radio_code = ttk.Radiobutton(window, text="Code Block", variable=format_var, value="Code Block")
format_radio_code.pack(pady=5)

# Create and pack the section entry widget
section_label = ttk.Label(window, text="Section:")
section_label.pack()
section_entry = ttk.Entry(window)
section_entry.pack(pady=5)

# Create and pack the content entry widget
content_label = ttk.Label(window, text="Content:")
content_label.pack()
content_text = ScrolledText(window, height=8)
content_text.pack(pady=5)

# Create and pack the save button
save_button = ttk.Button(window, text="Save", command=save_button_click)
save_button.pack(pady=5)

# Create and pack the search entry widget
search_label = ttk.Label(window, text="Search Keyword:")
search_label.pack()
search_entry = ttk.Entry(window)
search_entry.pack(pady=5)

# Create and pack the search button
search_button = ttk.Button(window, text="Search", command=search_button_click)
search_button.pack(pady=5)

# Create and pack the open button
open_button = ttk.Button(window, text="Open", command=open_button_click)
open_button.pack(pady=5)

# Run the GUI event loop
window.mainloop()
