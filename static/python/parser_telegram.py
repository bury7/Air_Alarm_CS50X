from telethon.sync import TelegramClient
from configparser import ConfigParser
import os
import datetime



class InvalidIDException(Exception):
    "Raised when the id value is not exist"
    pass


class InvalidHashException(Exception):
    "Raised when the id value is not exist"
    pass



class Telegram:
    def __init__(self) -> None:
        """!!!You need to change file config.ini!!!"""
        self.api_id, self.api_hash = self.get_config("config.ini")

        """Alarms Dictionary"""
        self.alarms ={
        "KyivCity":{
            "name": "#м_Київ",
            "eng_name": "City Kyiv",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Dnipropetrovsk":{
            "name": "#Дніпропетровська_область",
            "eng_name": "Dnipropetrovsk Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Kharkiv":{
            "name": "#Харківська_область",
            "eng_name": "Kharkiv Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Kyiv":{
            "name": "#Київська_область",
            "eng_name": "Kyiv Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Lviv":{
            "name": "#Львівська_область",
            "eng_name": "Lviv Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Odesa":{
            "name": "#Одеська_область",
            "eng_name": "Odesa Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Donetsk":{
            "name": "#Донецька_область",
            "eng_name": "Donetsk Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Poltava":{
            "name": "#Полтавська_область",
            "eng_name": "Poltava Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Zaporizhia":{
            "name": "#Запорізька_область",
            "eng_name": "Zaporizhia Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Vinnytsia":{
            "name": "#Вінницька_область",
            "eng_name": "Vinnytsia Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Cherkasy":{
            "name": "#Черкаська_область",
            "eng_name": "Cherkasy Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Mykolaiv":{
            "name": "#Миколаївська_область",
            "eng_name": "Mykolaiv Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Khmelnytskyi":{
            "name": "#Хмельницька_область",
            "eng_name": "Khmelnytskyi Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Zhytomyr":{
            "name": "#Житомирська_область",
            "eng_name": "Zhytomyr Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "IvanoFrankivsk":{
            "name": "#ІваноФранківська_область",
            "eng_name": "Ivano-Frankivsk Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Chernihiv":{
            "name": "#Чернігівська_область",
            "eng_name": "Chernihiv Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Sumy":{
            "name": "#Сумська_область",
            "eng_name": "Sumy Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Volyn":{
            "name": "#Волинська_область",
            "eng_name": "Volyn Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Kirovohrad":{
            "name": "#Кіровоградська_область",
            "eng_name": "Kirovohrad Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Rivne":{
            "name": "#Рівненська_область",
            "eng_name": "Rivne Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Kherson":{
            "name": "#Херсонська_область",
            "eng_name": "Kherson Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Ternopil":{
            "name": "#Тернопільська_область",
            "eng_name": "Ternopil Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Zakarpattia":{
            "name": "#Закарпатська_область",
            "eng_name": "Zakarpattia Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Chernivtsi":{
            "name": "#Чернівецька_область",
            "eng_name": "Chernivtsi Region",
            "alarm": False,
            "time": None,
            "duration": None,        
        },
        "Luhansk":{
            "name": "#Луганська_область",
            "eng_name": "Luhansk Region",
            "alarm": True,
            "time": "2022-04-04 19:45",
            "duration": compute_time(datetime.datetime.now() - datetime.datetime.strptime("2022-04-04 19:45", "%Y-%m-%d %H:%M")), 
        },
        "Crimea":{
            "name": "#Кримська_область",
            "eng_name": "Autonomous Republic of Crimea",
            "alarm": True,
            "time": "2022-12-11 00:22",
            "duration": compute_time(datetime.datetime.now() - datetime.datetime.strptime("2022-12-11 00:22", "%Y-%m-%d %H:%M")),
        },
        "Sevastopol":{
            "name": "#Севастополь",
            "eng_name": "City Sevastopol",
            "alarm": True,
            "time": "2022-12-11 00:22",
            "duration": compute_time(datetime.datetime.now() - datetime.datetime.strptime("2022-12-11 00:22", "%Y-%m-%d %H:%M")),   
        }
        ,}


    """
    Gets ID and hash data from the configuration file from static/config/YourConfig.ini
    Args:
        path: Path to the config file
    Returns:
        Two strings of data, the first with ID, the second with hash
    Raises:
        InvalidIDException: Raised when the id value is not exist
        InvalidHashException: Raised when the id value is not exist
    """
    def get_config(self, path:str) -> str:
        config = ConfigParser()
        path = os.path.abspath("./static/config/" + path)
        config.read(path)

        api_id = config["TELEGRAM"]["api_id"]
        if not api_id:
            raise InvalidIDException

        api_hash = config["TELEGRAM"]["api_hash"]
        if not api_hash:
            raise InvalidHashException

        return api_id, api_hash 


    """
    Gets information from Air Alarm telegram chanel
    Returns:
        Change Alarms Dictionary
    """
    async def get(self) -> None:
        async with TelegramClient("parse", self.api_id, self.api_hash) as client:
            async for message in client.iter_messages("air_alert_ua", offset_date=datetime.date.today(), reverse=True):
                msg = message.message
                if msg.startswith("🔴"):
                    for name, info in self.alarms.items():
                        if info["name"] in msg:
                            self.alarms[name]["alarm"] = True
                            time = datetime.datetime.strptime(str(datetime.date.today()) + " " + msg.split()[1], "%Y-%m-%d %H:%M")
                            self.alarms[name]["time"] = str(time.strftime("%Y/%m/%d %H:%M"))
                            self.alarms[name]["duration"] = compute_time(datetime.datetime.now() - time)

                elif msg.startswith("🟢") or msg.startswith("🟡"):
                    for name, info in self.alarms.items():
                        if info["name"]  in msg:
                            self.alarms[name]["alarm"] = False
                            self.alarms[name]["time"] = None
                            self.alarms[name]["duration"] = None
                            break

"""
Convert timedelta to srting
Args:
    time: timedelta
Returns:
    Retunrs string of timedelta
"""
def compute_time(time:datetime.timedelta) -> str:
    total_seconds = time.total_seconds()
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)      
    minutes, seconds = divmod(remainder, 60)
    
    message = ""
    if days >= 1:
        message += f"{int(days):02} d. "
    if hours >= 1:
        message += f"{int(hours):02} h. "
    if minutes >= 1:
        message += f"{int(minutes):02} m. "

    return message
