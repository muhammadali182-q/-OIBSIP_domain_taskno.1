# -OIBSIP_domain_taskno.4
Project of Oasis Intern
# Weather App (Python + Tkinter + OpenWeatherMap API)

This is a simple and interactive **desktop weather app** built using **Python and Tkinter** , powered
by the **OpenWeatherMap API**. Just type in a city name, click a button, and get real-time
weather data with a friendly UI and animated feedback.

**Features**

```
➢ Get live weather info for any city
➢ Displays:
o Temperature in Celsius
o Humidity percentage
o Weather condition (with emoji icons!)
➢ Smooth animated feedback on result display
➢ Input placeholder & user-friendly warnings
➢ Uses the OpenWeatherMap API to fetch real-time data
```
**Tech Stack**

```
➢ Python 3.x
➢ tkinter – for the GUI
➢ requests – for API calls
➢ OpenWeatherMap API
```
**Requirements**

```
➢ Make sure you have the following Python package installed:
➢ pip install requests
➢ Also, get your free API key from https://openweathermap.org/api
```
**How to Run**

1. Replace the API key in the script:
2. API_KEY = 'your_api_key_here'
3. Run the app:
4. python weather_app.py



**Example Usage**

Input: New York

Output:

```
🌧️ New York, US
Temperature: 26.5°C
Humidity: 78%
Condition: Light rain
```
**Project Structure**

```
File Description
```
```
weather_app.py Main Python GUI application
```
```
README.md Project overview and documentation
```
**How the API Works**

The app sends a request to:

[http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric](http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric)

It then extracts the required fields (temp, humidity, condition) and shows them in the GUI.

**Author**

Crafted with and Python by Muhammad Ali

**License**

This project is free to use and modify for personal or educational purposes.
