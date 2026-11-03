import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(33, "Outliers (IQR)")
datos = pd.Series([10, 12, 11, 13, 12, 11, 14, 12, 100, 11, -50, 13])
q1, q3 = datos.quantile(0.25), datos.quantile(0.75)
iqr = q3 - q1
low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print(f"Límites: [{low}, {high}]")
sin_outliers = datos[datos.between(low, high)]
print(sin_outliers)
