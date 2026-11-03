import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(10, "Agregar datos")
s10 = pd.Series([1, 2, 3])
s10 = pd.concat([s10, pd.Series([4, 5])], ignore_index=True)
print(s10)
