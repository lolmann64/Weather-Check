import requests
import tkinter as tk
from tkinter import messagebox                      #Program to locate weatherdata from an API

#erstellung des hauptfensters
root = tk.Tk()
root.title("Wetter App")

#labels und entry fields
city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

#button für wetter fetch
fetch_button = tk.Button(root, text="Fetch Wetter")
fetch_button.pack()

#display label für infos
weather_label = tk.Label(root, text="")
weather_label.pack()

#funktion des fetch's von der Wetter data

def fetch_weather():
    city = city_entry.get()
    api_key = "72b6c6d97490088897789aeedefaf625"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


    try:
        response = requests.get(url)
        data = response.json()
        #print(data)
        temperature = data["main"]["temp"]
        grad_temperature: float = temperature - 273.15
        round_weather = round(grad_temperature, 2)
        weather = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {round_weather}°C\nWeather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")
fetch_button.config(command=fetch_weather)

# Start the GUI main loop
root.mainloop()





