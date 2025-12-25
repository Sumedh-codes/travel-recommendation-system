import pandas as pd
from scipy.spatial.distance import cosine
from config import TRANSACTION_PATH, ITEM_PATH
def load_data(transaction_path, item_path):
    transaction = pd.read_excel(TRANSACTION_PATH)
    item = pd.read_excel(ITEM_PATH)

    # merging Userids with attraction type ids and putting it in df
    user_attar = pd.merge(transaction[["UserId","AttractionId","Rating"]],item[["AttractionId","AttractionTypeId"]], on="AttractionId")
    atrrac_ratings = user_attar.pivot_table(index='UserId', columns='AttractionTypeId', values='Rating', fill_value=0)
    atrrac_ratings.reset_index(inplace=True)
    atrrac_ratings = atrrac_ratings.drop("UserId", axis=1)
    tmp_atrrac_ratings = pd.DataFrame(index=atrrac_ratings.columns, columns = atrrac_ratings.columns )

    # finding cosine similarity
    for i in range(0, len(tmp_atrrac_ratings.columns)):
        for j in range(0,len(tmp_atrrac_ratings.columns)):
            tmp_atrrac_ratings.iloc[i,j] = 1-cosine(atrrac_ratings.iloc[:,i],atrrac_ratings.iloc[:,j])

    return transaction, item, atrrac_ratings, tmp_atrrac_ratings