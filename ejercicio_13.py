import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(13, "std y mean")
s13 = pd.Series([2, 4, 4, 4, 5, 5, 7, 9])
print("Promedio:", s13.mean())
print("Desviación estándar:", s13.std())
