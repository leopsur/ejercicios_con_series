import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

s13 = pd.Series([2, 4, 4, 4, 5, 5, 7, 9])
titulo(14, "min y max")
print("Mínimo:", s13.min(), "| Máximo:", s13.max())
