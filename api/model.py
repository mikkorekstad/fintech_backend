import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot
from pandas import datetime
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

if __name__ == '__main__':
    import scraper
    number_of_days = 1000
    
    SCRAPER_TSLA = scraper.Scraper(ticker="TSLA", n_days=number_of_days)
    SCRAPER_VIX = scraper.Scraper(ticker="^VIX", n_days=number_of_days)
    SCRAPER_GME = scraper.Scraper(ticker="GME", n_days=number_of_days)
    SCRAPER_SP500 = scraper.Scraper(ticker="^GSPC", n_days=number_of_days)
    SCRAPER_AAPL = scraper.Scraper(ticker="AAPL", n_days=number_of_days)
    
    df = pd.concat([SCRAPER_TSLA.historic_data, 
                    SCRAPER_VIX.historic_data, 
                    SCRAPER_GME.historic_data, 
                    SCRAPER_SP500.historic_data, 
                    SCRAPER_AAPL.historic_data], 
                   axis=1)
    
    df = SCRAPER_VIX.historic_data

    print(df)
    
    #plt.figure()
    #lag_plot(SCRAPER_TSLA.historic_data['Open'], lag=3)
    #plt.title('TESLA Stock - Autocorrelation plot with lag = 3')
    #plt.show()
    
    
    train_data, test_data = df[0:int(len(df)*0.7)], df[int(len(df)*0.7):]
    training_data = train_data['Close'].values
    test_data = test_data['Close'].values
    history = [x for x in training_data]
    model_predictions = []
    N_test_observations = len(test_data)
    for time_point in range(N_test_observations):
        model = ARIMA(history, order=(4,1,0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        model_predictions.append(yhat)
        true_test_value = test_data[time_point]
        history.append(true_test_value)
    MSE_error = mean_squared_error(test_data, model_predictions)
    print('Testing Mean Squared Error is {}'.format(MSE_error))
    
    test_set_range = df[int(len(df)*0.7):].index
    plt.plot(test_set_range, model_predictions, color='blue', marker='o', linestyle='dashed',label='Predicted Price')
    plt.plot(test_set_range, test_data, color='red', label='Actual Price')
    plt.title('TESLA Prices Prediction')
    plt.xlabel('Date')
    plt.ylabel('Prices')
    plt.xticks(df[int(len(df)*0.7):].index)
    plt.legend()
    plt.show()