 import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
import os
from PIL import Image, ImageTk
import tempfile
import webbrowser

def search_orders(query):
    try:
        with open("OrderDetail.txt", "r") as f:  # Replace "orders.txt" with your file
            orders = f.readlines()
    except FileNotFoundError:
        return "Error: orders.txt not found."

    results = []
    for order in orders:
        if re.search(query, order, re.IGNORECASE):  # Case-insensitive search
            results.append(order.strip())

    if results:
        return "\n".join(results)
    else:
        return "No matching orders found."


def print_output(output_text):
    try:
        # Create a temporary HTML file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
            temp_file_path = temp_file.name
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Print Output</title>
                <script>
                    window.onload = function() {{
                        window.print();
                    }};
                </script>
            </head>
            <body>
                <pre style="font-family: Arial, sans-serif; font-size: 14px; white-space: pre-wrap;">
{output_text}
                </pre>
            </body>
            </html>
            """
            temp_file.write(html_content.encode('utf-8'))

        #Open the temporary HTML file in the default web browser
        webbrowser.open(f"file://{temp_file_path}")

    except Exception as e:
        messagebox.showerror("Print Error", f"An error occurred while trying to print: {e}")


def on_search():
    query = entry.get()
    output = search_orders(query)
    output_text.delete("1.0", tk.END)  # Clear previous output
    output_text.insert(tk.END, output)


def on_print():
    output = output_text.get("1.0", tk.END).strip()
    if output:  # Check if there's any output to print
        print_output(output)
    else:
        messagebox.showinfo("Nothing to Print", "There is no output to print.")


# --- GUI setup ---
window = tk.Tk()
window.title("Order Search")

label = tk.Label(window, text="Enter search query:")
label.pack(pady=5)

entry = tk.Entry(window, width=50)
entry.pack(pady=5)

search_button = tk.Button(window, text="Search", command=on_search)
search_button.pack(pady=5)

output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=15)
output_text.pack(pady=5)

#  Add print button with image
print_icon = Image.open("print_icon.png")  # Replace with your print icon image file
print_icon = print_icon.resize((20, 20))  # Adjust size as needed
print_photo = ImageTk.PhotoImage(print_icon)
print_button = tk.Button(window, image=print_photo, command=on_print)  # No text, just the icon
print_button.image = print_photo  # Keep a reference! (important)
print_button.pack()

window.mainloop()
