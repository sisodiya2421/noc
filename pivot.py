import pandas as pd
import numpy as np


class Pivot:
    def __init__(self):
        self.df = pd.read_csv('./files/titanic.csv')

    def createPivot(self):
        self.df.drop(['PassengerId', 'Ticket', 'Name'], inplace=True, axis=1)
        table = pd.pivot_table(data=self.df, index=['Sex'])
        table.to_excel(
            "./outputs/pivot_output.xlsx")
