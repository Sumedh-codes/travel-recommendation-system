import pandas as pd
from data_loader import tmp_atrrac_ratings

# finding similar destinations based off cosine similarity
similar_destination = pd.DataFrame(index = tmp_atrrac_ratings.columns, columns = range(1,7))
for i in range(0,len(tmp_atrrac_ratings.columns)):
    similar_destination.iloc[i,:6] = tmp_atrrac_ratings.iloc[0:,i].sort_values(ascending=False)[:6].index
# print(similar_destination.head(10).iloc[:10,2:5])


