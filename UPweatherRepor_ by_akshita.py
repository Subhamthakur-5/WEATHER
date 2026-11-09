import requests
import pandas as pd
import time

urls = {
    "Agra": "https://api.open-meteo.com/v1/forecast?latitude=27.18&longitude=78.01&current=temperature_2m&timezone=Asia/Kolkata",
    "Aligarh": "https://api.open-meteo.com/v1/forecast?latitude=27.88&longitude=78.08&current=temperature_2m&timezone=Asia/Kolkata",
    "Ambedkar Nagar": "https://api.open-meteo.com/v1/forecast?latitude=26.43&longitude=82.55&current=temperature_2m&timezone=Asia/Kolkata",
    "Amethi": "https://api.open-meteo.com/v1/forecast?latitude=26.15&longitude=81.81&current=temperature_2m&timezone=Asia/Kolkata",
    "Amroha": "https://api.open-meteo.com/v1/forecast?latitude=28.90&longitude=78.47&current=temperature_2m&timezone=Asia/Kolkata",
    "Auraiya": "https://api.open-meteo.com/v1/forecast?latitude=26.47&longitude=79.51&current=temperature_2m&timezone=Asia/Kolkata",
    "Ayodhya": "https://api.open-meteo.com/v1/forecast?latitude=26.80&longitude=82.20&current=temperature_2m&timezone=Asia/Kolkata",
    "Azamgarh": "https://api.open-meteo.com/v1/forecast?latitude=26.07&longitude=83.18&current=temperature_2m&timezone=Asia/Kolkata",
    "Baghpat": "https://api.open-meteo.com/v1/forecast?latitude=28.95&longitude=77.22&current=temperature_2m&timezone=Asia/Kolkata",
    "Bahraich": "https://api.open-meteo.com/v1/forecast?latitude=27.57&longitude=81.59&current=temperature_2m&timezone=Asia/Kolkata",
    "Ballia": "https://api.open-meteo.com/v1/forecast?latitude=25.76&longitude=84.15&current=temperature_2m&timezone=Asia/Kolkata",
    "Balrampur": "https://api.open-meteo.com/v1/forecast?latitude=27.43&longitude=82.18&current=temperature_2m&timezone=Asia/Kolkata",
    "Banda": "https://api.open-meteo.com/v1/forecast?latitude=25.48&longitude=80.33&current=temperature_2m&timezone=Asia/Kolkata",
    "Barabanki": "https://api.open-meteo.com/v1/forecast?latitude=26.94&longitude=81.19&current=temperature_2m&timezone=Asia/Kolkata",
    "Bareilly": "https://api.open-meteo.com/v1/forecast?latitude=28.36&longitude=79.43&current=temperature_2m&timezone=Asia/Kolkata",
    "Basti": "https://api.open-meteo.com/v1/forecast?latitude=26.80&longitude=82.73&current=temperature_2m&timezone=Asia/Kolkata",
    "Bhadohi": "https://api.open-meteo.com/v1/forecast?latitude=25.39&longitude=82.57&current=temperature_2m&timezone=Asia/Kolkata",
    "Bijnor": "https://api.open-meteo.com/v1/forecast?latitude=29.37&longitude=78.13&current=temperature_2m&timezone=Asia/Kolkata",
    "Budaun": "https://api.open-meteo.com/v1/forecast?latitude=28.03&longitude=79.12&current=temperature_2m&timezone=Asia/Kolkata",
    "Bulandshahr": "https://api.open-meteo.com/v1/forecast?latitude=28.40&longitude=77.85&current=temperature_2m&timezone=Asia/Kolkata",
    "Chandauli": "https://api.open-meteo.com/v1/forecast?latitude=25.27&longitude=83.27&current=temperature_2m&timezone=Asia/Kolkata",
    "Chitrakoot": "https://api.open-meteo.com/v1/forecast?latitude=25.20&longitude=80.92&current=temperature_2m&timezone=Asia/Kolkata",
    "Deoria": "https://api.open-meteo.com/v1/forecast?latitude=26.50&longitude=83.78&current=temperature_2m&timezone=Asia/Kolkata",
    "Etah": "https://api.open-meteo.com/v1/forecast?latitude=27.56&longitude=78.66&current=temperature_2m&timezone=Asia/Kolkata",
    "Etawah": "https://api.open-meteo.com/v1/forecast?latitude=26.78&longitude=79.02&current=temperature_2m&timezone=Asia/Kolkata",
    "Farrukhabad": "https://api.open-meteo.com/v1/forecast?latitude=27.39&longitude=79.58&current=temperature_2m&timezone=Asia/Kolkata",
    "Fatehpur": "https://api.open-meteo.com/v1/forecast?latitude=25.93&longitude=80.81&current=temperature_2m&timezone=Asia/Kolkata",
    "Firozabad": "https://api.open-meteo.com/v1/forecast?latitude=27.15&longitude=78.40&current=temperature_2m&timezone=Asia/Kolkata",
    "Gautam Buddha Nagar": "https://api.open-meteo.com/v1/forecast?latitude=28.47&longitude=77.50&current=temperature_2m&timezone=Asia/Kolkata",
    "Ghaziabad": "https://api.open-meteo.com/v1/forecast?latitude=28.67&longitude=77.44&current=temperature_2m&timezone=Asia/Kolkata",
    "Ghazipur": "https://api.open-meteo.com/v1/forecast?latitude=25.58&longitude=83.58&current=temperature_2m&timezone=Asia/Kolkata",
    "Gonda": "https://api.open-meteo.com/v1/forecast?latitude=27.13&longitude=81.97&current=temperature_2m&timezone=Asia/Kolkata",
    "Gorakhpur": "https://api.open-meteo.com/v1/forecast?latitude=26.76&longitude=83.37&current=temperature_2m&timezone=Asia/Kolkata",
    "Hamirpur": "https://api.open-meteo.com/v1/forecast?latitude=25.95&longitude=80.15&current=temperature_2m&timezone=Asia/Kolkata",
    "Hapur": "https://api.open-meteo.com/v1/forecast?latitude=28.73&longitude=77.78&current=temperature_2m&timezone=Asia/Kolkata",
    "Hardoi": "https://api.open-meteo.com/v1/forecast?latitude=27.39&longitude=80.13&current=temperature_2m&timezone=Asia/Kolkata",
    "Hathras": "https://api.open-meteo.com/v1/forecast?latitude=27.60&longitude=78.05&current=temperature_2m&timezone=Asia/Kolkata",
    "Jalaun": "https://api.open-meteo.com/v1/forecast?latitude=26.15&longitude=79.35&current=temperature_2m&timezone=Asia/Kolkata",
    "Jaunpur": "https://api.open-meteo.com/v1/forecast?latitude=25.75&longitude=82.68&current=temperature_2m&timezone=Asia/Kolkata",
    "Jhansi": "https://api.open-meteo.com/v1/forecast?latitude=25.45&longitude=78.57&current=temperature_2m&timezone=Asia/Kolkata",
    "Kannauj": "https://api.open-meteo.com/v1/forecast?latitude=27.05&longitude=79.91&current=temperature_2m&timezone=Asia/Kolkata",
    "Kanpur Dehat": "https://api.open-meteo.com/v1/forecast?latitude=26.42&longitude=79.92&current=temperature_2m&timezone=Asia/Kolkata",
    "Kanpur Nagar": "https://api.open-meteo.com/v1/forecast?latitude=26.45&longitude=80.33&current=temperature_2m&timezone=Asia/Kolkata",
    "Kasganj": "https://api.open-meteo.com/v1/forecast?latitude=27.81&longitude=78.65&current=temperature_2m&timezone=Asia/Kolkata",
    "Kaushambi": "https://api.open-meteo.com/v1/forecast?latitude=25.53&longitude=81.38&current=temperature_2m&timezone=Asia/Kolkata",
    "Kushinagar": "https://api.open-meteo.com/v1/forecast?latitude=26.74&longitude=83.89&current=temperature_2m&timezone=Asia/Kolkata",
    "Lakhimpur Kheri": "https://api.open-meteo.com/v1/forecast?latitude=27.95&longitude=80.78&current=temperature_2m&timezone=Asia/Kolkata",
    "Lalitpur": "https://api.open-meteo.com/v1/forecast?latitude=24.69&longitude=78.41&current=temperature_2m&timezone=Asia/Kolkata",
    "Lucknow": "https://api.open-meteo.com/v1/forecast?latitude=26.85&longitude=80.95&current=temperature_2m&timezone=Asia/Kolkata",
    "Maharajganj": "https://api.open-meteo.com/v1/forecast?latitude=27.14&longitude=83.56&current=temperature_2m&timezone=Asia/Kolkata",
    "Mahoba": "https://api.open-meteo.com/v1/forecast?latitude=25.29&longitude=79.87&current=temperature_2m&timezone=Asia/Kolkata",
    "Mainpuri": "https://api.open-meteo.com/v1/forecast?latitude=27.23&longitude=79.02&current=temperature_2m&timezone=Asia/Kolkata",
    "Mathura": "https://api.open-meteo.com/v1/forecast?latitude=27.49&longitude=77.67&current=temperature_2m&timezone=Asia/Kolkata",
    "Mau": "https://api.open-meteo.com/v1/forecast?latitude=25.94&longitude=83.56&current=temperature_2m&timezone=Asia/Kolkata",
    "Meerut": "https://api.open-meteo.com/v1/forecast?latitude=28.98&longitude=77.71&current=temperature_2m&timezone=Asia/Kolkata",
    "Mirzapur": "https://api.open-meteo.com/v1/forecast?latitude=25.15&longitude=82.57&current=temperature_2m&timezone=Asia/Kolkata",
    "Moradabad": "https://api.open-meteo.com/v1/forecast?latitude=28.83&longitude=78.77&current=temperature_2m&timezone=Asia/Kolkata",
    "Muzaffarnagar": "https://api.open-meteo.com/v1/forecast?latitude=29.47&longitude=77.70&current=temperature_2m&timezone=Asia/Kolkata",
    "Pilibhit": "https://api.open-meteo.com/v1/forecast?latitude=28.64&longitude=79.80&current=temperature_2m&timezone=Asia/Kolkata",
    "Pratapgarh": "https://api.open-meteo.com/v1/forecast?latitude=25.90&longitude=81.95&current=temperature_2m&timezone=Asia/Kolkata",
    "Prayagraj": "https://api.open-meteo.com/v1/forecast?latitude=25.44&longitude=81.84&current=temperature_2m&timezone=Asia/Kolkata",
    "Rae Bareli": "https://api.open-meteo.com/v1/forecast?latitude=26.23&longitude=81.24&current=temperature_2m&timezone=Asia/Kolkata",
    "Rampur": "https://api.open-meteo.com/v1/forecast?latitude=28.80&longitude=79.02&current=temperature_2m&timezone=Asia/Kolkata",
    "Saharanpur": "https://api.open-meteo.com/v1/forecast?latitude=29.97&longitude=77.55&current=temperature_2m&timezone=Asia/Kolkata",
    "Sambhal": "https://api.open-meteo.com/v1/forecast?latitude=28.58&longitude=78.55&current=temperature_2m&timezone=Asia/Kolkata",
    "Sant Kabir Nagar": "https://api.open-meteo.com/v1/forecast?latitude=26.77&longitude=83.07&current=temperature_2m&timezone=Asia/Kolkata",
    "Shahjahanpur": "https://api.open-meteo.com/v1/forecast?latitude=27.88&longitude=79.91&current=temperature_2m&timezone=Asia/Kolkata",
    "Shamli": "https://api.open-meteo.com/v1/forecast?latitude=29.45&longitude=77.31&current=temperature_2m&timezone=Asia/Kolkata",
    "Shravasti": "https://api.open-meteo.com/v1/forecast?latitude=27.51&longitude=82.05&current=temperature_2m&timezone=Asia/Kolkata",
    "Siddharthnagar": "https://api.open-meteo.com/v1/forecast?latitude=27.28&longitude=83.08&current=temperature_2m&timezone=Asia/Kolkata",
    "Sitapur": "https://api.open-meteo.com/v1/forecast?latitude=27.57&longitude=80.68&current=temperature_2m&timezone=Asia/Kolkata",
    "Sonbhadra": "https://api.open-meteo.com/v1/forecast?latitude=24.69&longitude=83.07&current=temperature_2m&timezone=Asia/Kolkata",
    "Sultanpur": "https://api.open-meteo.com/v1/forecast?latitude=26.26&longitude=82.07&current=temperature_2m&timezone=Asia/Kolkata",
    "Unnao": "https://api.open-meteo.com/v1/forecast?latitude=26.55&longitude=80.49&current=temperature_2m&timezone=Asia/Kolkata",
    "Varanasi": "https://api.open-meteo.com/v1/forecast?latitude=25.32&longitude=82.99&current=temperature_2m&timezone=Asia/Kolkata"
}
allurls = []
for district, url in urls.items():
    response = requests.get(url)
    data = response.json()
    temperature = data["current"]["temperature_2m"]
    date_time = data["current"]["time"]

    lat = data["latitude"]
    lon = data["longitude"]

    allurls.append({
        "district": district,
        "date_time": date_time,
        "latitude": lat,
        "longitude": lon,
        "temperature_c": temperature
    })
    print(f"{district}: {date_time} {temperature} Degree Celsius")
df = pd.DataFrame(allurls)
df = df.sort_values(by="temperature_c", ascending=True, ignore_index=True)
av = df["temperature_c"].mean()
min_temp = df["temperature_c"].min()
max_temp = df["temperature_c"].max()
df = df.rename(columns={"temperature_c": "Temperature"})
df = df.rename(columns={"date_time": "Date/Time"})
print(f"Average Temp = {av}")
print(f"Min Temp = {min_temp}")
print(f"Max Temp = {max_temp}")
df.to_csv("Uttar_Pradesh_District_Temp.csv", index=False)

print(df)