import datetime
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like  # Used this as a workaround for an error.
# There is an issue with datareader 0.6 not fully compatible with Pandas 0.23.1
# Workaround taken from https://stackoverflow.com/questions/50394873/import-pandas-datareader-gives-importerror-cannot-import-name-is-list-like
import pandas_datareader.data as web # Import of pandas_datareader for remote data access to retrieve values
import matplotlib.pyplot as plt # Used for plotting
from matplotlib import style # Changing the style of the plot

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()

df = web.DataReader("XOM", "morningstar", start, end) # This will pull the date frames from Mornistar of Stock: XOM

df.reset_index(inplace=True) # Reset the index of the DF output.
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head()) # The .head method allows us to print the first 5 entries o the series

df['High'].plot()
plt.legend()
plt.show()