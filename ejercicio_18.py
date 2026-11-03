import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(18, "Contiene NaN")
s18 = pd.Series([1, np.nan, 3, None, 5])
print(s18.isna())
print("¿Hay NaN?:", s18.isna().any())
