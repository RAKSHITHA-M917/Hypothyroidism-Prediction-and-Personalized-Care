import tkinter as tk
from tkinter import messagebox
from src.predict_app import predict_thyroid

def run_prediction():
    try:
        name = name_var.get()
        age = int(age_var.get())
        gender = gender_var.get()
        pregnant = pregnant_var.get()
        location = location_var.get()
        sugar = float(sugar_var.get())
        sys_bp = float(sys_var.get())
        dia_bp = float(dia_var.get())
        TSH = float(tsh_var.get())
        T3 = float(t3_var.get())
        T4 = float(t4_var.get())

        result = predict_thyroid(name, age, gender, pregnant, location, sugar, sys_bp, dia_bp, TSH, T3, T4)
        messagebox.showinfo("Prediction Result", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Hypothyroid Prediction System")
root.geometry("400x500")
root.configure(bg="#e6f7ff")

# Labels and entries
fields = ["Name", "Age", "Gender (Male/Female)", "Pregnant (Yes/No)", "Location",
          "Sugar Level", "Systolic BP", "Diastolic BP", "TSH", "T3", "T4"]
vars_ = [tk.StringVar() for _ in fields]
name_var, age_var, gender_var, pregnant_var, location_var, sugar_var, sys_var, dia_var, tsh_var, t3_var, t4_var = vars_

for i, field in enumerate(fields):
    tk.Label(root, text=field, bg="#e6f7ff", font=("Arial", 10, "bold")).pack(pady=3)
    tk.Entry(root, textvariable=vars_[i], width=30).pack()

tk.Button(root, text="Predict", command=run_prediction, bg="#4CAF50", fg="white",
          font=("Arial", 11, "bold")).pack(pady=15)

root.mainloop()
