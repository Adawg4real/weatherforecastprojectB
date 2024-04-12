# import the module
import python_weather

import asyncio
import os

async def getweather():
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city

    city = input("Welcome to the Weather App! Please enter a city name: ")
    # try:
    weather = await client.get(city)
    # except:
    #   print("Error: - invalid city name. Please put in valid value")

    # returns the current day's forecast temperature (int)
    print("The temperature for today is: " + str(weather.temperature) +
          " degrees Farehneit.")
    # ans = input("Do you want to know the temperature in celsius? ")
    # if ans.upper() == "YES":
    #   celsius = (weather.temperature - 32) * 5 / 9
    #   print("The temperature for today is: " + str(int(celsius)) +
    #         " degrees Celsius.")
    # else:
    #   print("Okay.")
    # print("The wind speed is:  mph.")
    # print("The humidity is: " + str(weather.humidity) + "%.")
    # print("The sky is currently: " + str(weather.description))
    # print("The current time is: " + str(weather.datetime)) temperature=48

    ans = input("Do you want to know the weather for the next few days? ")
    if ans.upper() == "YES":
      for daily in weather.daily_forecasts:
        high = max(daily.hourly_forecasts.temperature)
        low = min(daily.hourly_forecasts.temperature)
        sky = max(daily.hourly_forecasts.description, key= daily.hourly_forecasts.description.count)
        print("The temperature high will be:" + str(high) )
        print("The temperature low will be:" + str(low) )
        print("On this date: " + str(daily.date))
        print("The sky will be: " + str(sky))

        # hourly forecasts
        # for hourly in daily.hourly_forecasts:
        #   print(f' --> {hourly!r}')
    else:
      print('Alright.')

    # # get the weather forecast for a few days
    # for daily in weather.daily_forecasts:
    #   print(daily)

    # # hourly forecasts
    # for hourly in daily.hourly_forecasts:
    #   print(f' --> {hourly!r}')


if __name__ == '__main__':
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(getweather())
