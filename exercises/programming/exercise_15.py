import pandas as pd


df = pd.read_csv("datos")

ingreso_promedio = df.groupby("genero")["ingreso"].mean()

min_edad = df.groupby("genero")["edad"].min()

# df.groupby("genero").agg({"ingreso": "mean", "edad": "min"})?

