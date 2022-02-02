import os
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import colorama
from colorama import Fore
print (Fore.CYAN+"#######################################################################################################")
print(Fore.GREEN+"[//] Created By Paul Fruitful")
print(Fore.GREEN+"""[//] Contact Me On Whatsapp At +2348114483062 \n[//] Mail Me at fruitful2007@outlook.com""")
print (Fore.CYAN+"#######################################################################################################")
print(Fore.LIGHTYELLOW_EX+"""
This Tool Is Used For Tracking Phones Just Using Their Numbers 
""")
update=input (Fore.GREEN+"Do You Want To Update [y/n]")
if update=='y':
   os.system("""cd 
            gitclone https://github.com/paulfruitful/phoneloc""")
else:
 print("Always Update")
input=input(Fore.LIGHTBLUE_EX+"Please Input Number You Want To Track:")

phonenumbertrack=phonenumbers.parse(input)
track=geocoder.description_for_number(phonenumbertrack,'en')
time=timezone.time_zones_for_number(phonenumbertrack)
carriername=carrier.name_for_number(phonenumbertrack,'en')
print(Fore.GREEN+f'''Location:{track} Provider
Name:{carriername} 
Timezone:{time}''')
