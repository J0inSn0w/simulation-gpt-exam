import pandas as pd 

try: 
    df = pd.read_csv("datos.csv")
except FileNotFoundError:
    print("lo sentimos no lo encontramos")