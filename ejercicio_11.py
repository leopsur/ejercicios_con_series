import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(11, "Filtrar")
s11 = pd.Series([5, 12, 7, 20, 3, 15])
mayores = s11[s11 > 10]
print(mayores)
