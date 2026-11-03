import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

s16 = pd.Series(range(1, 11))
titulo(17, "Series a NumPy")
print(s16.to_numpy(), type(s16.to_numpy()))
