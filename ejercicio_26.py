import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

s25 = pd.Series([5, 12, 7, 20, 3, 15])
titulo(26, "Remover por condición")
print(s25[s25 > 10])
