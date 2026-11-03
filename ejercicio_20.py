import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

s18 = pd.Series([1, np.nan, 3, None, 5])
titulo(20, "dropna")
print(s18.dropna())

