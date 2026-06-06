import pandas as pd

df = pd.read_csv("datos.csv")

df.head()
df = df.drop(axis=1,columns=["score_general"])

df = df[df["cantidad"] >= 50]