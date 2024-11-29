import pandas as pd


data = {
    "Motor": ["Motor 1", "Motor 2", "Motor 3", "Motor 4", "Motor 5"],
    "Potencia (kW)": [12, 65, 185, 400, 250],
    "Velocidad RMS (mm/s)": [4.3, 1.05, 33, 8.5, 0.75],
    "Velocidad Pico (in/s)": [2.5, 0.05, 0.525, 0.25, 0.75],
    "Desplazamiento (P-P)": [2.5, 0.05, 0.525, 0.25, 0.75],
    "Frecuencia (RPM)": [3600, 5750, 10500, 4500, 7600],
}

motors_df = pd.DataFrame(data)

def classify_vibration(v_rms):
    if v_rms <= 0.28:
        return "Good"
    elif v_rms <= 1.12:
        return "Satisfactory"
    elif v_rms <= 7.10:
        return "Unsatisfactory"
    else:
        return "Unacceptable"

motors_df["Condición"] = motors_df["Velocidad RMS (mm/s)"].apply(classify_vibration)

print(motors_df)

motors_df.to_csv("condiciones_motores.csv", index=False)
print("\nEl archivo 'condiciones_motores.csv' ha sido creado.")
