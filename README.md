# 🎬 Movie Recommendation System

A stylish and functional content-based Movie Recommender System built with **Streamlit**, using movie metadata and cosine similarity to suggest similar films.

![Streamlit](https://img.shields.io/badge/Made%20With-Streamlit-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![Status](https://img.shields.io/badge/Project-Active-brightgreen?style=flat-square)

---

## 🌟 Features

- Recommend 5 similar movies based on your selection
- Movie poster fetching using TMDb API
- Styled UI with gradient background and hover effects
- Streamlit interactive interface
- Fast content-based recommendation using cosine similarity

---

## 🚀 Demo

![Demo GIF](https://github.com/pradeepjswl/movie_reccomendation_system/assets/your-image.gif)


---

## 🛠️ Technologies Used

- **Python**
- **Pandas**, **NumPy**
- **Streamlit**
- **Scikit-learn** (for similarity)
- **TMDb API** (for posters)

---

## 📦 Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/pradeepjswl/movie_reccomendation_system.git
   cd movie_reccomendation_system
   
Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py


🔑 TMDb API Key Setup (Optional)
Replace the TMDb API key in app.py:

api_key = 'your_tmdb_api_key_here'


📁 File Structure

├── app.py                              # Streamlit frontend & logic

├── movie_dict.pkl                      # Movie metadata

├── similarity.pkl                      # Cosine similarity matrix

├── requirements.txt                    # Project dependencies

├── README.md                           # Project documentation



🌐 Deployment Options

Streamlit Cloud
Render
Heroku

✨Future Improvements
Add genre-based filters

Search bar or autocomplete

Collaborative filtering support

Save user preferences

🤝 Contributing
Contributions are welcome! Feel free to fork the repo, raise an issue, or submit a PR.

📧 Contact
Created by Pradeep Jaiswal
Feel free to reach out!


### ✅ Next Step

1. Copy the above text into a file named `README.md` in your project folder.
2. Push to GitHub:
   ```bash
   git add README.md
   git commit -m "Added professional README"
   git push origin main
