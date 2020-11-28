import pandas as pd
quotes = pd.read_csv('quote_stash.csv')
quotes = quotes[['quote', 'author']]
quotes.head()

quotes = quotes.drop_duplicates(subset='author', keep="last")

quotes.shape

quotes.to_csv('quotes.csv', index=None)
