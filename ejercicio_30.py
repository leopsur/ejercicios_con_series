import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(30, "between")
s30 = pd.Series([1, 5, 10, 15, 20, 25])
print(s30[s30.between(10, 20)])
