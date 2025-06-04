"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    import pandas as pd

    # Cargar el archivo tbl1.tsv
    df = pd.read_csv('files/input/tbl1.tsv', sep='\t')

    # Agrupar por c0 y ordenar
    values = df.groupby('c0')['c4'].apply(lambda x: sorted(x))

    # Retornar la tabla con los resultados
    return values.apply(lambda x: ','.join(x)).reset_index()

if __name__ == "__main__":
    print(pregunta_11())