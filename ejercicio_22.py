import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(22, "agg")
s22 = pd.Series([10, 20, 30, 40])
print(s22.agg(["min", "max", "mean", "sum"]))
print("Con una función:", s22.agg("sum"))
