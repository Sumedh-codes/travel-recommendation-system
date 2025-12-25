
import seaborn as sns
import matplotlib.pyplot as plt

# heatmap generation function
def heatmap(df):
    df = df.astype(float)
    plt.figure(figsize=(10, 8))
    sns.heatmap(df, cmap="YlGnBu", annot=True, fmt=".2f", linewidths=.5)
    plt.title('Cosine Similarity Heatmap')
    plt.xlabel('Attraction Type')
    plt.ylabel('Attraction Type')
    plt.show()

