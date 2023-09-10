from autots import AutoTS
import pandas as pd


class ForecastTool:
    """A class to forecast out excel data using AutoTS"""

    def __init__(self):
        """Initiate all class variables"""
        
        # Convert data to a pandas dataframe
        self.df = pd.read_excel("C:\\Users\Thomas\\Downloads\\forecast-tool\\testDataZeroIndepVars.xlsx")



test = ForecastTool()
print(test.df)

