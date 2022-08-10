# imports 
import quantstats as qs 

#Ticker examples:
# Facebook Meta - (META)
# Apple - (AAPL)
# Microsoft - (MSFT)
# Tesla - (TSLA)
# Coca-Cola - (KO)

# request ticker from user's input
print("Introduce Stock ticker: ")
ticker = input().upper()

print("Introduce initial inversion: ")
initial_balance = input()    
# extend pandas functionality
qs.extend_pandas()

# we get returns from ticker input
stock = qs.utils.download_returns(ticker)

stock.plot_earnings(savefig="plot_earnings/"+ticker+'.png', start_balance=int(initial_balance))

qs.plots.snapshot(stock, title=ticker+' Perfomance')

qs.reports.html(stock, "SPY", title=ticker+" Metrics", output=ticker+'.html',download_filename="metrics/"+ticker+"-metrics.html")