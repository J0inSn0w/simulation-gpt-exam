import pandas as  pd
import matplotlib.pyplot as plt

df = pd.read_excel("excel.xlsx", sheet_name=2)

df = df.drop(columns=["calif_general","direccion","genero"])

df = df.query("edad >= 18")

df.boxplot(column="calif_mate",by="municipio")

plt.show()