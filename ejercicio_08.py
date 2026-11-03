import numpy as np
import pandas as pd

def titulo(n, texto):
    print(f"\nEjercicio {n}: {texto}")

titulo(8, "explode()")
lista = [["Colombia", "Perú", "Argentina"], ["Bolivia", "Uruguay"], ["Chile"]]
punto_partida = pd.Series(lista)
print(punto_partida)
objetivo = punto_partida.explode().reset_index(drop=True)
print(objetivo)
