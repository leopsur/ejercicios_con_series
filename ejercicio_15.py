import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

s13 = pd.Series([2, 4, 4, 4, 5, 5, 7, 9])
titulo(15, "describe")
print(s13.describe())
