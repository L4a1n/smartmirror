# import the module
import python_weather
import asyncio

# Return todays weather
async def getWeatherToday(city):
    async with python_weather.Client() as client:
        try:
            weather = await client.get(city)
        except:
            return "Something went wrong"
    return weather.locale

# Return this weeks weather
async def getWeatherWeek(city):
    async with python_weather.Client() as client:
        try:
            weather = await client.get(city)
        except:
            return "Something went wrong"
    return weather.feels_like
