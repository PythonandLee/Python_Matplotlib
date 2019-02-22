

```python
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates = []
    highs, lows = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
        

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

plt.title("Daily high and low temperature, July 2014", fontsize=24)
plt.xlabel('', fontsize=14)
plt.ylabel("Temperature(F)", fontsize=14)
plt.tick_params(axis='both', labelsize=10)
fig.autofmt_xdate()

plt.show()
```




