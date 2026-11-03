import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(12, "reindex")
s12 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(s12.reindex(["d", "c", "b", "a"]))
