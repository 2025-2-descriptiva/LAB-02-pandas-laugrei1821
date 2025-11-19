"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

"""
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """

import pandas as pd

def pregunta_06():
    ruta = r"C:\Especializacion-Analitica\Descriptiva\LAB-02-pandas-laugrei1821\files\input\tbl1.tsv"
    df = pd.read_csv(ruta, sep="\t")
    return sorted(df["c4"].str.upper().unique())

if __name__ == "__main__":
    print(pregunta_06())
