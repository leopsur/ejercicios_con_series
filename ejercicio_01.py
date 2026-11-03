import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")
 
titulo(1, "Crear una Series")
s = pd.Series([10, 20, 30, 40, 50])
print(s)

