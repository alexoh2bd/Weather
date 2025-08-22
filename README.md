# Weather Application

A sleek and responsive weather application that provides current weather information for any city worldwide. Built with Python and Streamlit.

## Features

- Real-time weather data for any city
- Clean and intuitive user interface
- Multiple city comparison
- Detailed weather information including temperature, humidity, and weather conditions

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- OpenWeatherMap API key (free tier available)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your OpenWeatherMap API key:
     ```
     API_Key=your_api_key_here
     ```
   - Replace `your_api_key_here` with your actual OpenWeatherMap API key

## 🏃‍♂️ Running the Application

### Command Line Version
Run the command line version of the weather app:
```bash
python cityweather.py
```

### Web Interface (Recommended)
Launch the Streamlit web application:
```bash
streamlit run app.py
```

## Using the Application

1. Launch the application using either method above
2. Enter the name of a city when prompted
3. View the current weather information
4. (Web version) Add more cities using the input field and button

## Dependencies

- Python 3.8+
- dotenv
- requests
- streamlit

## Acknowledgments

- Weather data provided by [OpenWeather](https://openweathermap.org/)
- Built with [Streamlit](https://streamlit.io/)