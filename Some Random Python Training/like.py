import tkinter as tk
from tkinter import ttk
import numpy as np

def random_array(m, n, x, y):
    return np.random.randint(x, y, size=(m, n))

def compute_inverses():
    results_text.delete(1.0, tk.END)  # Clear previous results

    matrices = [random_array(4, 4, 0, 10) for _ in range(10)]

    for idx, matrix in enumerate(matrices):
        matrix_name = chr(ord('A') + idx)
        
        results_text.insert(tk.END, f"{matrix_name}:\n{matrix}\n\n")
        
        inverse_matrix = np.linalg.inv(matrix)
        np.set_printoptions(precision=2, suppress=True)
        results_text.insert(tk.END, f"Inverse {matrix_name}:\n{inverse_matrix}\n\n")
        
        results_text.insert(tk.END, "-"*40 + "\n")

# Create the main window
root = tk.Tk()
root.title("Matrix Inverse Calculator")

# Create a button to calculate inverses
calculate_button = ttk.Button(root, text="Calculate Inverses", command=compute_inverses)
calculate_button.pack(pady=10)

# Create a text widget to display results
results_text = tk.Text(root, height=30, width=80)
results_text.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()