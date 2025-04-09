import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Your OpenWeatherMap API key
API_KEY = "78195c628f60ab8547295f1a5969e31e"
CITY = "Bengaluru"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data
response = requests.get(URL)
data = response.json()

# Extract temperature and timestamp
timestamps = [entry['dt_txt'] for entry in data['list']]
temperatures = [entry['main']['temp'] for entry in data['list']]
# Create a line plot
plt.figure(figsize=(12, 6))
sns.lineplot(x=timestamps, y=temperatures, marker='o')
plt.title(f"Temperature Trend in {CITY}", fontsize=16)
plt.xlabel("Timestamp", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
