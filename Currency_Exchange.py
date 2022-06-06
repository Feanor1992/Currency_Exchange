# use yahoo_fin library to parse data

import yahoo_fin.stock_info as si
from datetime import datetime, timedelta


def convert_currency(src, dst, amount):
    # construct the currency pair symbol
    symbol = f'{src} {dst}=X'

    # use get_data() from stock_info to pass the symbol of currency
    # pass "1m" as the interval parameter in the get_data() method to retrieve data for the current minute
    # not the default current day
    latest_data = si.get_data(symbol, interval='1m', start_date=datetime.now() - timedelta(days=2))
    # extract minute data from the last 2 days, because there be problems with the course on the weekend

    # get the latest datetime
    latest_datetime = latest_data.index[-1].to_pydatetime()

    # get the last price
    last_price = latest_data.iloc[-1].close

    # return the latest data and converted amount
    return latest_datetime, last_price * amount


if __name__ == "__main__":
    import sys
    # get currency and amount
    source_currency = sys.argv[1]
    destination_currency = sys.argv[2]

    amount = float(sys.argv[3])

    latest_datetime, exchange_rate = convert_currency(source_currency, destination_currency, amount)

    print(f'Last update time: {latest_datetime}')
    print(f'{amount} {source_currency} = {exchange_rate} {destination_currency}')



