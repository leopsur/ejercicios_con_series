import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

s27 = pd.Series(["a", "b", "a", "c", "b", "a"])
titulo(28, "to_csv")
print(s27.to_csv(index=False, header=False))
print(s27.to_csv())