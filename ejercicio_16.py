import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(16, "Pares e impares")
s16 = pd.Series(range(1, 11))
print("Pares:", s16[s16 % 2 == 0].tolist())
print("Impares:", s16[s16 % 2 != 0].tolist())

