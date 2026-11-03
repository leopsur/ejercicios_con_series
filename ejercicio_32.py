import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(32, "equals")
p = pd.Series([1, 2, 3])
q = pd.Series([1, 2, 3])
r = pd.Series([1, 2, 4])
print("p y q:", p.equals(q))
print("p y r:", p.equals(r))
