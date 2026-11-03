import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(27, "value_counts")
s27 = pd.Series(["a", "b", "a", "c", "b", "a"])
print(s27.value_counts())
