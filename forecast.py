from autots import AutoTS
import pandas as pd


class ForecastTool:
    """A class to forecast out excel data using AutoTS"""

    def __init__(self, filepath, dateCol):
        """Initiate all class variables"""
        
        # Convert data to a pandas dataframe
        self.df = pd.read_excel(filepath) 

        # Set the date column from the data set to be a DatetimeIndex
        idx = pd.DatetimeIndex(self.df[dateCol])
        self.df = self.df.set_index(idx)
        self.df = self.df.drop(dateCol, axis=1)

        

    def run_forecast_unbiased(self):
        """Run AutoTS forecast on the data and return an unbiased set of forecast results"""

        # Create a autoTS model
        model = AutoTS(
            forecast_length=12, 
            frequency='infer',
            ensemble='auto',
            max_generations=4,
            num_validations=2,
        )

        # Fit the data set to the model
        model = model.fit(self.df)

        # Run predictions on the data
        prediction = model.predict()

        # Create a dataframe of unbiased prediction results
        forecasts_df = prediction.forecast

        #forecasts_up = prediction.upper_forecast

        #forecasts_down = prediction.lower_forecast

        return forecasts_df


    


#test = ForecastTool(filepath="C:\\Users\Thomas\\Downloads\\forecast-tool\\testDataZeroIndepVars.xlsx", dateCol="Date")
#print("\n\n\n--------------Model--------------")
#print(test.model)
#print("\n\n\n\n\n\n\n-------------Forecast-------------")
#print(test.forecasts_df)
#print("\n\n\n\n\n\n\n--------------Upper--------------")
#print(test.forecasts_up)
#print("\n\n\n\n\n\n\n--------------Lower--------------")
#print(test.forecasts_down)


