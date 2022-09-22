import pandas as pd


class ExcelMatching:
    def __init__(self):
        self.excel1 = pd.read_excel("./files/Registration_details.xlsx")
        self.excel2 = pd.read_excel("./files/exam_results.xlsx")

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

        final.to_excel('./outputs/matching_result.xlsx', index=False)
        return True
