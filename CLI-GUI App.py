import joblib
import numpy as np
import tkinter as tk
from tkinter import messagebox

# Load the saved model
model = joblib.load('final_model.pkl')

def predict_calories():
    try:
        gender = int(gender_var.get())
        age = int(age_entry.get())
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        duration = float(duration_entry.get())
        heart_rate = float(heart_rate_entry.get())
        body_temp = float(body_temp_entry.get())

        if gender not in [0, 1]:
            raise ValueError("Gender must be 0 or 1.")

        input_features = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
        prediction = model.predict(input_features)[0]
        messagebox.showinfo("Prediction", f"Predicted Calories Burned: {prediction:.2f}")
    except ValueError as e:
        messagebox.showerror("Invalid input", f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Calories Burned Predictor")

# Create and place labels and entry widgets
tk.Label(root, text="Gender (0 for female, 1 for male):").grid(row=0, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
tk.Entry(root, textvariable=gender_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Height (in cm):").grid(row=2, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Weight (in kg):").grid(row=3, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Duration of exercise (in minutes):").grid(row=4, column=0, padx=10, pady=5)
duration_entry = tk.Entry(root)
duration_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Heart Rate:").grid(row=5, column=0, padx=10, pady=5)
heart_rate_entry = tk.Entry(root)
heart_rate_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Body Temperature (in Celsius):").grid(row=6, column=0, padx=10, pady=5)
body_temp_entry = tk.Entry(root)
body_temp_entry.grid(row=6, column=1, padx=10, pady=5)

# Create and place the predict button
predict_button = tk.Button(root, text="Predict", command=predict_calories)
predict_button.grid(row=7, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
