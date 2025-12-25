from recommender import recommendation

# dropping unncessary columns
recommendation = recommendation.drop(recommendation.columns[[0,1]], axis=1)
recommendation = recommendation.drop('attrc_type_id_3',axis=1)
recommendation = recommendation.drop('AttractionTypeId',axis=1)
recommendation = recommendation.drop('AttractionId',axis=1)
recommendation = recommendation.drop('AttractionId_x',axis=1)
recommendation = recommendation.drop('AttractionTypeId_y',axis=1)
recommendation = recommendation.drop('attrc_type_id_2',axis=1)
recommendation = recommendation.drop('AttractionId_y',axis=1)
# dropping duplicate values
recommendations = recommendation.drop_duplicates(
    subset=["UserId", "AttractionAddress"]
)
# getting top 5 recommendations per user
final_recommendations = (
    recommendations
    .groupby("UserId")
    .head(5)   # top 5 recommendations per user
)