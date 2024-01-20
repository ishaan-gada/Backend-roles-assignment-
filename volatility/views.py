from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd 

@api_view(['POST'])
def get_volatality(request):
    df = pd.read_csv(request.data["datafile"])
    #if using the csv file given in the assignment make sure code has 'Close ' and not 'Close'line 8 views.py
    df['Daily Returns'] = df['Close '] / df['Close '].shift(1) - 1
    df = df.dropna()
    daily_return = df['Daily Returns']
    daily_volatility = round(df['Daily Returns'].std(), 4)
    annualized_volatility =round(daily_volatility * (len(df)**0.5),4)
    print(df['Daily Returns'])
    return Response({"Daily_Returns":daily_return,"Daily_Volatality":str(daily_volatility),"Annual_Volatality":str(annualized_volatility)})
