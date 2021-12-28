import python_weather
import asyncio
import datetime
import locale

locale.setlocale(locale.LC_TIME, "es_ES")


async def getweather(ciudad):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)
    # fetch a weather forecast from a city
    weather = await client.find(ciudad)
    # close the wrapper once done
    await client.close()
    # returns the current day's forecast temperature (int)
    return weather.current.temperature


def obtener_estado_tiempo(ciudad):
    loop = asyncio.get_event_loop()
    temperatura = loop.run_until_complete(getweather(ciudad))
    celsius = (temperatura - 32) * 5.0/9.0
    return celsius


def traer_fecha():
    fecha = datetime.datetime.now()
    return fecha.strftime("%A, %d de %B de %Y a las %I:%M %p")
