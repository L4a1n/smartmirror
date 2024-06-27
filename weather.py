# import the module
import python_weather
import asyncio

# Return todays weather
async def getWeatherToday(city):
    temp = None
    async with python_weather.Client() as client:
        try:
            weather = await client.get(city)
        except:
            return "Something went wrong"
# get the weather forecast for a few days
    for daily in weather.daily_forecasts:
      print(daily)

      # hourly forecasts
      for hourly in daily.hourly_forecasts:
        print(f' --> {hourly!r}')
    return temp

# Return this weeks weather
async def getWeatherWeek(city):
    async with python_weather.Client() as client:
        try:
            weather = await client.get(city)
        except:
            return "Something went wrong"
    return weather.feels_like
