import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import colorama
from colorama import Fore
print(Fore.GREEN+"[//] Created By Paul Fruitful")
print(Fore.CYAN+"""
[//] Contact Me On Whatsapp At +2348114483062 Or Mail Me at fruitful2007@outlook.com
""")
print(Fore.MAGENTA+"Welcome To Phoneloc")
print(Fore.LIGHTYELLOW_EX+"""
This Tool Is Used For Tracking Phones Just Using Their Numbers 
""")
input=input(Fore.LIGHTBLUE_EX+"Please Input Number You Want To Track:")

phonenumbertrack=phonenumbers.parse(input)
track=geocoder.description_for_number(phonenumbertrack,'en')
time=timezone.time_zones_for_number(phonenumbertrack)
carriername=carrier.name_for_number(phonenumbertrack,'en')
print(f'''Location:{track} Provider
Name:{carriername} 
Timezone:{time}''')
