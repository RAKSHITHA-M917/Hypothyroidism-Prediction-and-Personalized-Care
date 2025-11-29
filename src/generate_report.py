import datetime
from predict_app import predict_thyroid

def parse_bp(bp_input):
    """
    Parse BP input like '120/80 mm Hg' or '110/70'
    Returns systolic, diastolic as floats
    """
    try:
        parts = bp_input.replace("mm Hg", "").strip().split("/")
        systolic = float(parts[0].strip())
        diastolic = float(parts[1].strip())
    except Exception:
        print("⚠️ Invalid BP format. Please enter like '120/80 mm Hg'")
        systolic, diastolic = 0, 0
    return systolic, diastolic


def generate_patient_report():
    print(">>")
    name = input("Enter Name: ").strip()
    age = int(input("Enter Age: ").strip())
    gender = input("Enter Gender (Male/Female): ").strip()
    pregnant = input("Pregnant (Yes/No): ").strip()
    location = input("Enter Location: ").strip()
    sugar_level = float(input("Enter Sugar Level (mg/dL): ").strip())
    bp_input = input("Enter Blood Pressure (e.g. 120/80 mm Hg): ").strip()
    systolic, diastolic = parse_bp(bp_input)

    TSH = float(input("Enter TSH value: ").strip())
    T3 = float(input("Enter T3 value: ").strip())
    T4 = float(input("Enter TT4 value: ").strip())

    print("\n🧠 Predicting hypothyroid level...")

    # ✅ Predict using trained model
    result = predict_thyroid(name, age, gender, pregnant, location, sugar_level, systolic, diastolic, TSH, T3, T4)

    # ✅ Add date/time to report
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = (
        f"\n==============================\n"
        f"🩺 HYPOTHYROID PATIENT REPORT\n"
        f"==============================\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Gender: {gender}\n"
        f"Pregnant: {pregnant}\n"
        f"Location: {location}\n"
        f"Date & Time: {current_time}\n"
        f"------------------------------\n"
        f"Sugar Level: {sugar_level} mg/dL\n"
        f"Blood Pressure: {systolic}/{diastolic} mm Hg\n"
        f"TSH: {TSH}\nT3: {T3}\nTT4: {T4}\n"
        f"------------------------------\n"
        f"Predicted Result: {result}\n"
        f"==============================\n"
    )

    print(report)

    # ✅ Save report
    with open("patient_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print("✅ Report saved as 'patient_report.txt'")

if __name__ == "__main__":
    generate_patient_report()
