import csv
import re
import torch
import tkinter as tk
from tkinter import ttk, messagebox
import seaborn as sns
import matplotlib.pyplot as plt

def clean_and_process_data(csv_path):
    with open(csv_path, 'r', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        data = [row[0] for row in reader if row and row[0].strip()]

    new_array = [row for row in data if 'see' in row and len(row) < 55 and row[0] != '(']
    builder = [row for row in data if re.search(r[A-Za-z]+: row)]
    
    processed_data = [re.search(r'[A-Z][a-z]*', row).group() for row in data if re.search(r'[A-Z][a-z]*', row)]

    return new_array, builder, processed_data

def visualize_tensor(data):
    sns.set(style="whitegrid")

 
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(range(len(data))), y=data)
    
    plt.title("Processed Data Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

class DataProcessingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Processing App")

        # Create GUI elements
        self.csv_path_label = ttk.Label(master, text="Enter CSV File Path:")
        self.csv_path_label.pack(pady=10)

        self.csv_path_entry = ttk.Entry(master)
        self.csv_path_entry.pack(pady=10)

        self.process_button = ttk.Button(master, text="Process Data", command=self.process_data)
        self.process_button.pack(pady=20)

    def process_data(self):
        csv_path = self.csv_path_entry.get()
        try:
            new_array, builder, processed_data = clean_and_process_data(csv_path)

            # Display results in messagebox
            result_message = f"New Array: {new_array}\nBuilder: {builder}\nProcessed Data: {processed_data}"
            messagebox.showinfo("Data Processing Result", result_message)

            
            visualize_tensor(processed_data)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = DataProcessingApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
