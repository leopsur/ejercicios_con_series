import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

s27 = pd.Series(["a", "b", "a", "c", "b", "a"])
titulo(31, "drop_duplicates")
print(s27.drop_duplicates())
