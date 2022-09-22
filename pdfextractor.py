import tabula
import pandas as pd


class PdfExtractor:
    def __init__(self):
        self.tables = tabula.read_pdf(
            "./files/Climate.pdf", pages=3, multiple_tables=True)

    def extract(self):
        self.tables[0].rename(columns={'Mean\rMax.\rTemp.\r(oC)': 'Mean_Max_Temp',
                                       'Mean\rMin.\rTemp.\r(oC)': 'Mean_Min_Temp',
                                       'Relative\rHumidity\r(%)': 'Relative_Humidity_Morning',
                                       'Month’s\rTotal\rRain\r(mm)': 'Relative_Humidity_Evening',
                                       'Rainy days': 'Month_Total_Rain',
                                       'Days with': 'Rain_2.5',
                                       'Unnamed: 0': 'Rain_3.5',
                                       'Unnamed: 1': 'Days_with_Thunder',
                                       'Unnamed: 2': 'Days_with_Fog'}, inplace=True)

        self.tables[0].drop([0, 1], axis=0, inplace=True)
        self.tables[0].drop(self.tables[0].tail(1).index, inplace=True)

        cols = ['Relative_Humidity_Morning', 'Relative_Humidity_Evening',
                'Rain_2.5', 'Rain_3.5', 'Days_with_Thunder', 'Days_with_Fog']
        self.tables[0][cols] = self.tables[0][cols].apply(
            pd.to_numeric, errors='coerce', axis=1)

        self.tables[0].to_excel(
            "./outputs/pdf_extracted_output.xlsx", index=False)

        return True
