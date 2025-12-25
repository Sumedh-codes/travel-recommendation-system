# Travel-Recommendation-System
🌍 Tourism Recommendation System

A content-based recommendation system that suggests tourist attractions to users based on similarity between attraction types, learned from historical user ratings using cosine similarity.

This project demonstrates how classical recommender system concepts can be applied to real-world tourism data using Python and Pandas, with a clean, modular, GitHub-ready codebase.

✨ Features

📊 Uses user ratings to learn attraction preferences

🧠 Computes cosine similarity between attraction types

🗺️ Recommends real tourist locations (addresses)

🔁 Removes duplicate recommendations

🎯 Generates Top-N recommendations per user

📈 Visualizes similarity using a heatmap

🧩 Modular and well-structured codebase

🧠 How It Works

User ratings and attraction metadata are loaded from Excel files

A User × Attraction Type matrix is created using a pivot table

Cosine similarity is computed between attraction types

For each attraction type, the most similar types are identified

Similar attraction types are mapped back to real attractions

Duplicate recommendations are removed

Top-N recommendations per user are selected and exported

📂 Dataset Description
1️⃣ Transaction Dataset (Transaction.xlsx)
Column	Description
UserId	Unique identifier for each user
AttractionId	Unique identifier for each attraction
Rating	User rating for the attraction
2️⃣ Item Dataset (Item.xlsx)
Column	Description
AttractionId	Unique attraction identifier
AttractionTypeId	Category/type of attraction
AttractionAddress	Location or address of attraction

⚙️ Installation & Setup
```
1️⃣ Clone the repository
git clone https://github.com/your-username/tourism-recommendation-system.git
cd tourism-recommendation-system
```
```
2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
```
```
3️⃣ Install dependencies
pip install -r requirements.txt
```

🔑 Environment Variables
```
TRANSACTION_FILE_PATH=data/raw/Transaction.xlsx
ITEM_FILE_PATH=data/raw/Item.xlsx
```

🏗️ Project Structure
```
.
├── data/
│   └── raw/
│       ├── Transaction.xlsx
│       └── Item.xlsx
│
|
|── config.py              # Environment variable & path config
│── data_loader.py         # Data loading + matrix creation
│── similarity_utils.py    # Similar attraction type extraction
│── recommender.py         # Mapping types → attractions
│── postprocessor.py       # Deduplication & Top-N filtering
│── heatmap.py             # Cosine similarity visualization
│
├── outputs/
│   └── final_recommendations.csv
│
├── main.py                    # Pipeline entry point
├── requirements.txt
├── .env.example
└── README.md
```