import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(21, "abs")
print(pd.Series([-3, 4, -5, 0, 7]).abs())
