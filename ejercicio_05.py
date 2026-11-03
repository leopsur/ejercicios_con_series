import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(5, "Diccionario a Series")
d = {"a": 100, "b": 200, "c": 300}
print(pd.Series(d))
