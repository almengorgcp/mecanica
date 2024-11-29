import pandas as pd
import matplotlib.pyplot as plt
from mechanic import motors_df


motors_df["Frecuencia (CPM)"] = motors_df["Frecuencia (RPM)"] * 1
fig, ax = plt.subplots(figsize=(10, 7))

ax.set_xscale("log")
ax.set_yscale("log")

for i, row in motors_df.iterrows():
    ax.scatter(row["Frecuencia (CPM)"], row["Desplazamiento (P-P)"],
               label=row["Motor"], s=100)

ax.set_xlim(200, 20000)
ax.set_ylim(0.001, 10)
ax.set_xlabel("Frecuencia (CPM)", fontsize=12)
ax.set_ylabel("Desplazamiento (P-P)", fontsize=12)
ax.set_title("Gráfica de Severidad de Vibración ISO 10816", fontsize=14)
ax.grid(True, which="both", linestyle="--", linewidth=0.5)
ax.legend()

plt.savefig("grafica_severidad_vibracion.png")
print("La gráfica ha sido guardada como 'grafica_severidad_vibracion.png'.")
plt.show()
