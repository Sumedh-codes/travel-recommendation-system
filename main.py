# importing all Libraries
import os
from postprocessor import final_recommendations
from heatmap import heatmap
from data_loader import tmp_atrrac_ratings

heatmap(tmp_atrrac_ratings)

# exporting final recommendations to csv
os.makedirs("outputs", exist_ok=True)
final_recommendations.to_csv(
    "outputs/final_recommendations.csv",
    index=False
)

# renaming columns 
print(final_recommendations.head(20))
print(final_recommendations[final_recommendations["UserId"] == 3165])


