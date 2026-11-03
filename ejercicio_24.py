import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(24, "head y tail")
s24 = pd.Series(range(100, 200, 10))
print("Primeros 3:\n", s24.head(3))
print("Últimos 3:\n", s24.tail(3))
