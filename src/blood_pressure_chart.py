import matplotlib.pyplot as plt
import os

def generate_bp_chart(systolic, diastolic, name):
    os.makedirs("reports", exist_ok=True)
    plt.figure(figsize=(6, 4))
    plt.bar(['Systolic', 'Diastolic'], [systolic, diastolic], color=['skyblue', 'lightcoral'])
    plt.title(f"Blood Pressure Chart - {name}")
    plt.ylabel('mm Hg')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    chart_path = os.path.join("reports", f"{name}_bp_chart.png")
    plt.savefig(chart_path)
    plt.close()
    print(f"📊 BP chart saved in reports/{name}_bp_chart.png")
    return chart_path
