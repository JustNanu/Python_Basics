import pandas as pd

series = {"numbers": [2, 3, 4, 5 ,6],
          "cubes": [8, 27, 64, 125, 256]
         }
table = pd.DataFrame(series)

print(table)

print(table.loc[3])
