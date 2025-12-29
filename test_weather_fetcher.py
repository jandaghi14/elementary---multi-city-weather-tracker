import pytest 
from aioresponses import aioresponses
import asyncio
import aiohttp
from weather_fetcher import fetch_weather , fetch_all_weather , save_to_database

@pytest.mark.asyncio
async def test_fetch_weather_success():
    with aioresponses() as mock:
        fake_response = {'name' : 'jandagh' , 'main' : {'temp' : 150} , 'weather' : [{'description' : 'Snowing'}]}
        API_Key = "4907d8ee413a95e945f504b0a9ef3b70"
        mock.get(f"https://api.openweathermap.org/data/2.5/weather?q=jandagh&appid={API_Key}" , payload = fake_response)
        async with aiohttp.ClientSession() as session:
            response = await fetch_weather(session , "jandagh")
            assert response == fake_response

@pytest.mark.asyncio
async def test_fetch_weather_timeout():
    with aioresponses() as mock:
        fake_response = {'name' : 'jandagh' , 'main' : {'temp' : 150} , 'weather' : [{'description' : 'Snowing'}]}
        API_Key = "4907d8ee413a95e945f504b0a9ef3b70"
        mock.get(f"https://api.openweathermap.org/data/2.5/weather?q=jandagh&appid={API_Key}" , exception = asyncio.TimeoutError)
        async with aiohttp.ClientSession() as session:
            response = await fetch_weather(session , "jandagh")
            assert response is None

@pytest.mark.asyncio
async def test_fetch_weather_bad_status():
    with aioresponses() as mock:
        fake_response = {'name' : 'jandagh' , 'main' : {'temp' : 150} , 'weather' : [{'description' : 'Snowing'}]}
        API_Key = "4907d8ee413a95e945f504b0a9ef3b70"
        mock.get(f"https://api.openweathermap.org/data/2.5/weather?q=jandagh&appid={API_Key}" , payload = {'message' : 'fake message' , 'cod' : 'fake code'},status = 404)
        async with aiohttp.ClientSession() as session:
            response = await fetch_weather(session , "jandagh")
            assert response is None
            
@pytest.mark.asyncio
async def test_fetch_weather_network_error():
    with aioresponses() as mock:
        fake_response = {'name' : 'jandagh' , 'main' : {'temp' : 150} , 'weather' : [{'description' : 'Snowing'}]}
        API_Key = "4907d8ee413a95e945f504b0a9ef3b70"
        mock.get(f"https://api.openweathermap.org/data/2.5/weather?q=jandagh&appid={API_Key}" , exception = aiohttp.ClientError)
        async with aiohttp.ClientSession() as session:
            response = await fetch_weather(session , "jandagh")
            assert response is None    