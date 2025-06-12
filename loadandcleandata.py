from config import fetch_forecast_from_mssql

def load():
    df = fetch_forecast_from_mssql()
    df = df.dropna(subset=['ItemKey','SalesRepKey'])
    df['ItemKey'] = df['ItemKey'].astype('Int64').astype(str)
    df = df[df['CurrencyCode'].isin(['USD', 'EUR', 'INR'])]
    eur_to_usd = 1.1
    inr_tousd = 0.012
    df.loc[df['CurrencyCode'] == 'EUR', 'TotalSalesAmount'] *= eur_to_usd
    df.loc[df['CurrencyCode'] == 'INR', 'TotalSalesAmount'] *= inr_tousd
    df['CurrencyCode'] = 'USD'
    df = df[['YearMonth','CustomerKey','ItemKey','TotalQty', 'TotalSalesAmount']]

    return df