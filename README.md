# Multi-City Weather Tracker

An asynchronous Python application that fetches real-time weather data for multiple cities concurrently using the OpenWeatherMap API. Features comprehensive error handling, SQLite database caching, and full test coverage.

## Features

- 🌍 Fetch weather data for multiple cities concurrently
- ⚡ Async/await implementation for optimal performance
- 🛡️ Comprehensive error handling (timeout, bad status, network errors)
- 💾 SQLite database for caching weather data
- ✅ Full test coverage with mocked API responses
- 🔄 Context manager for safe database operations

## Technologies Used

- **Python 3.x**
- **aiohttp** - Async HTTP client
- **asyncio** - Asynchronous programming
- **SQLite3** - Local database
- **pytest** - Testing framework
- **aioresponses** - Mock async HTTP responses

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jandaghi14/multi-city-weather-tracker.git
cd multi-city-weather-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## API Key Setup

1. Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your API key from the dashboard
3. Replace the `API_Key` in `weather_fetcher.py` with your key:
```python
API_Key = "your_api_key_here"
```

## Usage

Run the weather tracker:
```bash
python weather_fetcher.py
```

The app will:
- Fetch weather data for 5 cities (Tehran, Paris, Tokyo, Rome, and one test city)
- Display temperature and weather description
- Save results to `FileDataBase.db`

## Testing

Run all tests:
```bash
pytest test_weather_fetcher.py -v
```

Tests cover:
- ✅ Successful API responses
- ✅ Timeout errors
- ✅ Bad HTTP status codes (404, 500)
- ✅ Network errors

## Project Structure
```
multi-city-weather-tracker/
├── weather_fetcher.py       # Main async weather fetching logic
├── database.py              # Context manager for SQLite operations
├── test_weather_fetcher.py  # Comprehensive test suite
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```


## Future Improvements

- Add temperature unit conversion (Celsius/Fahrenheit)
- Implement caching to reduce API calls
- Add CLI arguments for custom city lists
- Create data visualization for weather trends
- Add email notifications for weather alerts

---

Built as part of my Python learning journey - Day 69 of 180
