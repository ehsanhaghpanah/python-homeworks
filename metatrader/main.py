
# import pytz module for working with time zone
import pytz
import MetaTrader5 as mt5

from datetime import datetime

# connect to MetaTrader 5
if (not mt5.initialize()):
    print("initialize() failed")
    mt5.shutdown()
    quit()

# request connection status and parameters
print(mt5.terminal_info())
# get data on MetaTrader 5 version
print(mt5.version())

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
# request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zone
ticks = mt5.copy_ticks_from("BTCUSD", utc_from, 1000, mt5.COPY_TICKS_ALL)
print(f"last_error = {mt5.last_error()}")
print("Ticks received:",len(ticks))

# # request 1000 ticks from EURAUD
# btcusd_ticks = mt5.copy_ticks_from("BTCUSD", datetime(2020,1,28,13), 1000, mt5.COPY_TICKS_ALL)

# # # request ticks from AUDUSD within 2019.04.01 13:00 - 2019.04.02 13:00
# # audusd_ticks = mt5.copy_ticks_range("AUDUSD", datetime(2020,1,27,13), datetime(2020,1,28,13), mt5.COPY_TICKS_ALL)

# shut down connection to MetaTrader 5
mt5.shutdown()

# #DATA
# print('btcusd_ticks(', len(btcusd_ticks), ')')
# for val in btcusd_ticks[:10]: print(val)

