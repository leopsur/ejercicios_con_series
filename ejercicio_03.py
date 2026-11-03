import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(3, "Aritmética")
a = pd.Series([1, 2, 3, 4])
b = pd.Series([10, 20, 30, 40])
print("Suma:\n", a + b)
print("Resta:\n", b - a)
print("Multiplicación:\n", a * b)
print("División:\n", b / a)
