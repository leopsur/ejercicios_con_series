import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(7, "Cambiar dtype")
txt = pd.Series(["1", "2", "3", "4"])
print(txt.dtype)
num = txt.astype(int)  # también: pd.to_numeric(txt)
print(num.dtype)
print(num.astype(float))
