import tkinter as tk
from tkinter import ttk
import joblib
import numpy as np
from feature_options import feature_options
from feature_order import feature_order

model = joblib.load('laptop_price_model.pkl')


root = tk.Tk()
root.title("Laptop Price Predictor")
root.minsize(width=400, height=1)

entries = {}


def create_input_fields():
    for feature, options in feature_options.items():
        label = tk.Label(root, text=feature)
        label.pack()
        if options:
            combobox = ttk.Combobox(root, values=options)
            combobox.pack()
            entries[feature] = combobox
        else:
            entry = tk.Entry(root)
            entry.pack()
            entries[feature] = entry


def predict_price():
    input_data = np.zeros(211)  # Initialize with zeros for all features

    for i, tk_value in enumerate(entries.values()):
        value = tk_value
        index = -1
        if value.get() in feature_order:
            index = feature_order.index(value.get())
            input_data[index] = 1
            print(
                f"index: {index}, feature: {value.get()}, boolean: {input_data[index]}")
        else:
            print("field value:", value.get())
            input_data[i] = float(value.get())

    price = model.predict([input_data])[0]
    result_label.config(text=f"Predicted Price: {price}")


def clear_fields():
    for widget in entries.values():
        widget.delete(0, tk.END) if isinstance(
            widget, tk.Entry) else widget.set('')


# Create input fields
create_input_fields()

# Predict button
predict_button = ttk.Button(
    root, text="Predict Price", command=predict_price, style='TButton')
predict_button.pack()

# Clear button
clear_button = tk.Button(root, text="New Laptop",
                         command=clear_fields, bg="red", fg="white")
clear_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
