"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
    """
    import pandas as pd

    # Cargar el archivo tbl0.tsv
    df = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    # Retornar el valor máximo de 'c2' por cada letra de 'c1'
    return df.groupby('c1')['c2'].max()

if __name__ == '__main__':
    print(pregunta_05())