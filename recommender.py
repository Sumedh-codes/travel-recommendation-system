import pandas as pd 
import os
from similarity_utlis import similar_destination
from data_loader import transaction,item

# dividing similar destination df in columns
similar_destination_columns = similar_destination.rename(columns={3:"attrc_type_id_1",4:"attrc_type_id_2",5:"attrc_type_id_3"})
similar_destination_column_1 = similar_destination_columns.drop(['attrc_type_id_2','attrc_type_id_3'],axis=1)
similar_destination_1 = similar_destination_column_1.head(10).iloc[:10,2:3]
similar_destination_column_2 = similar_destination_columns.drop(['attrc_type_id_1','attrc_type_id_3'],axis=1)
similar_destination_2 = similar_destination_column_2.head(10).iloc[:10,2:3]
similar_destination_column_3 = similar_destination_columns.drop(['attrc_type_id_1','attrc_type_id_2'],axis=1)
similar_destination_3 = similar_destination_column_3.head(10).iloc[:10,2:3]

# creating a temp df
temp_df1 = pd.merge(transaction[["UserId","AttractionId","Rating"]],item[["AttractionId","AttractionTypeId",'AttractionAddress']], on="AttractionId")
temp_df = temp_df1.loc[:,['UserId','AttractionTypeId','AttractionId','AttractionAddress']]

# merging similar destination diff columns with tempdf
recommendation_1 = pd.merge(similar_destination_1, temp_df, on='AttractionTypeId')
recommendation_2 = pd.merge(similar_destination_2, temp_df, on='AttractionTypeId')
recommendation_3 = pd.merge(similar_destination_3, temp_df, on='AttractionTypeId')

# merging all the 3 recommendation into 1 df
recommendation = pd.merge(recommendation_1, recommendation_2, on='UserId')
recommendation = pd.merge(recommendation, recommendation_3, on='UserId')
