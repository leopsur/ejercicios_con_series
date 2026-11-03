import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(25, "where")
s25 = pd.Series([5, 12, 7, 20, 3, 15])
print(s25.where(s25 > 10, 0))