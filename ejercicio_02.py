import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")
 
s = pd.Series([10, 20, 30, 40, 50])
titulo(2, "Series a lista")
print(s.tolist())

