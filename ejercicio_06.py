import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(6, "NumPy a Series")
arr = np.array([5, 10, 15, 20])
print(pd.Series(arr))
