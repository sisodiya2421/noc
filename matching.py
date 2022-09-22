import pandas as pd
from pathlib import Path


class ExcelMatching:
    def __init__(self):
        folder = Path('./files/')
        file1 = folder / 'Registration_details.xlsx'
        file2 = folder / 'exam_results.xlsx'
        self.excel1 = pd.read_excel(file1)
        self.excel2 = pd.read_excel(file2)

    def match(self):
        final = self.excel1[["REGISTRATION NO",
                             "STUDENT EMAIL ID ",
                             "NAME OF STUDENT ",
                             "DOB",
                             "GENDER"]].merge(self.excel2[[
                                 "REGISTRATION NO",
                                 "Marks Obtained",
                                 "Percentage"
                             ]], on="REGISTRATION NO", how="inner")
        output = Path('./outputs/')
        final.to_excel(output / 'matching_result.xlsx', index=False)
        return True
