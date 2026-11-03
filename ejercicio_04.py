import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(4, "Comparaciones")
x = pd.Series([1, 5, 3, 8])
y = pd.Series([2, 5, 1, 9])
print("x > y:\n", x > y)
print("x == y:\n", x == y)
print("x <= y:\n", x <= y)
