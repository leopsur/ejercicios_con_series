import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(34, "groupby por mes")
fechas = pd.date_range("2022-01-01", periods=36, freq="MS")  # 3 años
rng = np.random.default_rng(42)
ventas = pd.Series(rng.integers(100, 500, size=36), index=fechas)
medias = ventas.groupby(ventas.index.month).mean()
medias.index.name = "mes"
print(medias.round(2))
