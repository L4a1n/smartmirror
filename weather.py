import python_weather
import asyncio
from datetime import datetime
import re

# Return todays weather
async def getWeatherToday(city="Kassel"):
    tempDaily = []
    tempHouhrly = []
    async with python_weather.Client() as client:
        try:
            weather = await client.get(city)
        except:
            return "Something went wrong"
    toRemove = ["<", ">", "datetime.date", "datetime.time", "Kind."]
    # get the weather forecast for three days
    # and format the output into usable strings for later 
    tempDaily.append(f"lastRefreshed=({datetime.now().strftime("%H, %M, %S")})")
    for daily in weather.daily_forecasts:
        temp = str(daily)
        pattern = "|".join(re.escape(seq) for seq in toRemove)
        temp = re.sub(pattern, "", temp)
        tempDaily.append(temp)
        tempHouhrly = []
        for hourly in daily.hourly_forecasts:
            temp = str(hourly)
            pattern = "|".join(re.escape(seq) for seq in toRemove)
            temp = re.sub(pattern, "", temp)
            tempHouhrly.append(temp)
        tempDaily.append(tempHouhrly)

    return tempDaily
