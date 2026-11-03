import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(9, "sort_values")
s9 = pd.Series([30, 10, 50, 20, 40])
print(s9.sort_values())
print(s9.sort_values(ascending=False))
