import tkinter as tk
import requests
from tkinter import messagebox

API_KEY = '1b927d523b628a7ef8f3a09777127cfe'  # <-- Replace with your API key

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            raise ValueError(data.get("message", "Invalid response"))

        # Extract data
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].capitalize()

        # Emoji for fun
        icon = "☀️" if "clear" in condition.lower() else "☁️" if "cloud" in condition.lower() else "🌧️" if "rain" in condition.lower() else "❓"

        result = f"{icon} {city_name}, {country}\n"
        result += f"Temperature: {temperature}°C\n"
        result += f"Humidity: {humidity}%\n"
        result += f"Condition: {condition}"

        result_var.set(result)
        # Animate result label color
        animate_label(result_label)

    except Exception as e:
        result_var.set("")
        messagebox.showerror("Error", f"Could not retrieve weather data.\n\nReason: {str(e)}")

def animate_label(label):
    # Color animation for UI feedback
    colors = ["#2193b0", "#6dd5ed", "#b2feea", "#ffffff"]
    def fade(i=0):
        label.config(bg=colors[i % len(colors)])
        if i < 8:
            label.after(100, fade, i+1)
        else:
            label.config(bg="#ffffff")
    fade()

def on_entry_click(event):
    if city_entry.get() == 'e.g. London, New York':
       city_entry.delete(0, "end")
       city_entry.config(fg='black')

def on_focusout(event):
    if city_entry.get() == '':
        city_entry.insert(0, 'e.g. London, New York')
        city_entry.config(fg='grey')

# ------------------- GUI ------------------- #
root = tk.Tk()
root.title("🌦️ Weather App")
root.geometry("400x420")
root.resizable(False, False)
root.config(bg="#f1f8ff")

# Top Frame
top_frame = tk.Frame(root, bg="#56ccf2")
top_frame.pack(fill="x")

title_label = tk.Label(top_frame, text="Weather App", font=("Segoe UI", 24, "bold"), bg="#56ccf2", fg="#2d2d2d")
title_label.pack(pady=(18, 8))

subtitle = tk.Label(root, text="Check current weather & forecast", font=("Segoe UI", 13), bg="#f1f8ff", fg="#4f4f4f")
subtitle.pack(pady=(0, 12))

input_frame = tk.Frame(root, bg="#f1f8ff")
input_frame.pack(pady=8)

city_entry = tk.Entry(input_frame, font=("Segoe UI", 16), justify='center', width=20, fg='grey', bg="#e3f2fd", relief="ridge", borderwidth=2)
city_entry.insert(0, 'e.g. London, New York')
city_entry.bind('<FocusIn>', on_entry_click)
city_entry.bind('<FocusOut>', on_focusout)
city_entry.pack(ipady=7)

get_weather_btn = tk.Button(root, text="Get Weather", font=("Segoe UI", 14, "bold"), bg="#2193b0", fg="white", activebackground="#6dd5ed", activeforeground="#2d2d2d", bd=0, relief="ridge", command=get_weather, cursor="hand2")
get_weather_btn.pack(pady=18, ipadx=16, ipady=5)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Segoe UI", 14, "bold"), justify='center', wraplength=370, bg="#ffffff", fg="#2193b0", relief="groove", borderwidth=2, padx=10, pady=16)
result_label.pack(pady=16, fill="x", padx=16)

footer = tk.Label(root, text="Powered by OpenWeatherMap API", font=("Segoe UI", 10), bg="#f1f8ff", fg="#4f4f4f")
footer.pack(side="bottom", pady=10)

root.mainloop()