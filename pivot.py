import pandas as pd
import numpy as np
from pathlib import Path


class Pivot:
    def __init__(self):
        folder = Path('./outputs/')
        self.df = pd.read_csv(folder / 'titanic.csv')

    def createPivot(self):
        self.df.drop(['PassengerId', 'Ticket', 'Name'], inplace=True, axis=1)
        table = pd.pivot_table(data=self.df, index=['Sex'])

        output_folder = Path("./outputs/")
        table.to_excel(output_folder /
                       "pivot_output.xlsx")
