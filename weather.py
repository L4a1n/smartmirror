# import the module
import python_weather
import asyncio

# Return todays weather
async def getWeatherToday(city):
    tempDaily = []
    tempHouhrly = []
    async with python_weather.Client() as client:
        try:
            weather = await client.get(city)
        except:
            return "Something went wrong"
    # get the weather forecast for three days
    for daily in weather.daily_forecasts:
        tempDaily.append(daily)

        # hourly forecasts for three days
        for hourly in daily.hourly_forecasts:
            tempHouhrly.append(hourly)
    print(tempDaily)
    

# Return this weeks weather
async def getWeatherWeek(city):
    async with python_weather.Client() as client:
        try:
            weather = await client.get(city)
        except:
            return "Something went wrong"
    return weather.feels_like

asyncio.run(getWeatherToday('Kassel'))
