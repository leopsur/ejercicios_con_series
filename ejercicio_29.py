import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(29, "apply")
print(pd.Series([1, 2, 3, 4]).apply(lambda v: v ** 2))
