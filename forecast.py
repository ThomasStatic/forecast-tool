from autots import AutoTS
import pandas as pd


class ForecastTool:
    """A class to forecast out excel data using AutoTS"""

    def __init__(self, filepath, dateCol):
        """Initiate all class variables"""
        
        # Convert data to a pandas dataframe
        self.df = pd.read_excel(filepath) 

        idx = pd.DatetimeIndex(self.df[dateCol])

        self.df = self.df.set_index(idx)
        self.df = self.df.drop(dateCol, axis=1)



        self.model = AutoTS(
            forecast_length=12, 
            frequency='infer',
            ensemble='auto',
            max_generations=4,
            num_validations=2,
        )


        self.model = self.model.fit(self.df)

        self.prediction = self.model.predict()    

        self.forecasts_df = self.prediction.forecast

        self.forecasts_up = self.prediction.upper_forecast

        self.forecasts_down = self.prediction.lower_forecast


test = ForecastTool(filepath="C:\\Users\Thomas\\Downloads\\forecast-tool\\testDataZeroIndepVars.xlsx", dateCol="Date")
#print("\n\n\n--------------Model--------------")
#print(test.model)
print("\n\n\n\n\n\n\n-------------Forecast-------------")
print(test.forecasts_df)
print("\n\n\n\n\n\n\n--------------Upper--------------")
print(test.forecasts_up)
print("\n\n\n\n\n\n\n--------------Lower--------------")
print(test.forecasts_down)


