# Anime Recommendation System

An intelligent recommendation system that suggests anime based on user preferences, viewing history, or specified criteria such as mood, genre, or popularity.

## Features

- **Personalized Recommendations**: Suggests anime tailored to the user’s preferences.
- **Mood-Based Suggestions**: Recommends anime based on the user’s mood (e.g., happy, sad, adventurous).
- **Genre Filtering**: Allows users to filter recommendations by genre (e.g., Action, Romance, Comedy).
- **Top Trending Anime**: Displays a list of currently trending anime.
- **Search Functionality**: Enables users to search for specific anime titles and get related recommendations.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Dataset](#dataset)
4. [Technologies Used](#technologies-used)
5. [Contributing](#contributing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/anime-recommendation-system.git
   cd anime-recommendation-system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```env
     API_KEY= app1_anime_reccomend.py
     DB_URL=anime_data.pkl
     ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the app in your browser at `:https://animereccomendation.streamlit.app/`.

## Usage

1. **Get Recommendations**:
   - Enter your favorite anime or select a mood to receive recommendations.

2. **Filter by Genre**:
   - Use the genre dropdown to filter the list of recommendations.

3. **Search for Anime**:
   - Use the search bar to find specific anime titles and view their details.

4. **View Trending Anime**:
   - Check out the "Trending" section for popular anime recommendations.

## Dataset

- The system uses data from public anime databases like [MyAnimeList](https://myanimelist.net/) or custom datasets.
- Sample dataset available on Google Drive: [Download Here](https://drive.google.com/file/d/your-dataset-file-id/view?usp=sharing).

## Technologies Used

- **Language**: Python
- **Framework**: Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Database**: SQLite/PostgreSQL
- **Frontend**: HTML, CSS, Bootstrap
- **API Integration**: MyAnimeList API (optional)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b  manishmmj/anime_reccomendation
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin manishmmj/anime_reccomendation
   ```
5. Open a pull request.

## Acknowledgments

- [MyAnimeList](https://myanimelist.net/) for providing a comprehensive anime database.
- [Scikit-learn](https://scikit-learn.org/) for machine learning tools.
- Open-source libraries and contributors who made this project possible.

---



