print('Hello World')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import openpyxl
import xlrd

s = pd.Series([1,3,5,np.nan,6,8])

print(s)

#--------------------

dates = pd.date_range('20130101',periods=6)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

df['E']=['one', 'one','two','three','four','three']

s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130102',periods=6))
df['F'] = s1

df.to_excel('foo.xlsx', sheet_name='Sheet1')

df2 = pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])

df2

#----------------------------

df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
s = df.iloc[3]

#----------------------------
#series 1 plot
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
#series 2 plot
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

plt.ylabel('some numbers')
plt.xlabel('the dates')
#plt.show()

#----------------------------------

# pd.read_csv('foo.csv', header=2, index_col=0, parse_dates=True)

#-------------------------------------

fig = plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_aspect(0.3)

#remove internal whitespace
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

x,y=np.random.random((2,100))
plt.scatter(x,y)    

x,y=np.random.random((2,100))
plt.scatter(x,y) 

x,y=np.random.random((2,100))
plt.scatter(x,y) 

#---------------------------------

#no index import
#stock_history = pd.read_excel('first 6 months 2014 historical stock prices.xlsx', 'output', index_col=None, na_values=['NA'])
#stock_history = stock_history.set_index('Date')

#indexed import
stock_history = pd.read_excel('first 6 months 2014 historical stock prices.xlsx', 'output', index_col='Date', na_values=['NA'])


#plot AMD
amd_history = stock_history[stock_history['Symbol'].isin(['AMD'])]
amd_history['Adj_Close'].plot()

#data literals
amd_history.Adj_Close.plot()

#plot AMD vs Intel
intel_history = stock_history[stock_history['Symbol'].isin(['AMD'])]
intel_history['Adj_Close'].plot()

intel_history = stock_history[stock_history['Symbol'].isin(['INTC'])]
intel_history['Adj_Close'].plot()

#-------------------------------------



#KEEP PLAYING WITH THIS

def get_symbol_dimension(symbol,dimension):
    return (symbol, stock_history[stock_history['Symbol'].isin([symbol])]) #return a tuple
    
def get_symbols_dimension(symbols, dimension):
        return  { key:value for (key,value) in [get_symbol_dimension(symbol,dimension) for symbol in symbols] }
        
#tuple in 1 slot
symbol_dimension = get_symbol_dimension('AMD','Adj_Close')
symbol_dimension[1].plot()

#dictionary 
symbols_dimension = get_symbols_dimension(['AMD','INTC'], 'Adj_Close')
symbols_dimension['AMD'].plot()



#------------------------------------

