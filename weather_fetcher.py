import aiohttp
import asyncio
from datetime import datetime , timedelta
from database import WeatherDatabase

async def fetch_weather(session , city , timeout = 10):
    API_Key = "4907d8ee413a95e945f504b0a9ef3b70"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"
    try:
        async with session.get(url, timeout = aiohttp.ClientTimeout(total= timeout)) as response:
            result =await response.json()
            if response.status != 200:
                print(f"{result['message']} - {result['cod']}")
                return None
            return result
    except asyncio.TimeoutError:
        print("Timeout Error!")
        return None
    except aiohttp.ClientError as e:
        print(f"There is an error {e}")
        return None
        
    
async def fetch_all_weather(cities):
        async with aiohttp.ClientSession() as session:
            city_fetch = [fetch_weather(session, city) for city in cities]
            result = await asyncio.gather(*city_fetch)
            to_send_database = []
            for i in result:
                if i is not None:
                    city_name = i['name']
                    temperature = i['main']['temp']
                    description = i['weather'][0]['description']
                    to_send_database.append((city_name,temperature,description))
            database_result = save_to_database(to_send_database)
            if database_result:
                print("Fetch and save successfully")
                return True
            print("Could not save to database! try again!")
            return False
                
def save_to_database(weather_data):
    print(weather_data)
    try:
        with WeatherDatabase("FileDataBase.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                                CREATE TABLE IF NOT EXISTS weathercache (
                                    city_name TEXT,
                                    temperature TEXT,
                                    description TEXT, 
                                    timestamp TEXT
                                )
                                """)
            timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            for city in weather_data:
                cursor.execute("""
                                                INSERT INTO weathercache (city_name , temperature,description,timestamp)
                                                VALUES (?,?,?,?)
                                                """,(city[0], city[1], city[2],timestamp))
            return True
    except Exception as e:
        print(f"Error in saving in database : {e}")
        return False
    
    
if __name__ == "__main__":
    cities = ['lonod' , 'tehran' , 'paris' , 'tokyo' , 'rome']
    asyncio.run(fetch_all_weather(cities))
    
        