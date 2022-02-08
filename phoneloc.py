import os
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import colorama
from colorama import Fore
print(Fore.RED+f'''
 ******************************************
  ********************_______*********|
  |***********************************************************************************"   |*****************************************
  |***********"************************************************************************"
  | ******      {Fore.GREEN+"PHONE LOC"}***************************************************
 |***********************************************************************************"   |********************************************
  ''')
print (Fore.LIGHTBLUE_EX+"###########################################################")
print(Fore.GREEN+"[//] Created By Paul Fruitful")
print(Fore.GREEN+"""[//] Contact Me On Whatsapp At +2348114483062 \n[//] Mail Me at fruitful2007@outlook.com""")
print (Fore.LIGHTBLUE_EX+"###########################################################")
print(Fore.LIGHTYELLOW_EX+"""
This Tool Is Used For Tracking Phones Just Using Their Numbers and it also gives you information about the phone number
""")
print(Fore.RED+"""DISCLAIMER: This Tool Is For Educational Purposes Only!!!! 
""")
update=input (Fore.GREEN+"Do You Want To Update [y/n]")
if update=='y':
   os.system("""cd 
                rm -rf phoneloc   
            gitclone https://github.com/paulfruitful/phoneloc""")
else:
 print("Always Update")
input=input(Fore.CYAN+"Please Input Number You Want To Track:")

phonenumbertrack=phonenumbers.parse(input)
track=geocoder.description_for_number(phonenumbertrack,'en')
time=timezone.time_zones_for_number(phonenumbertrack)
carriername=carrier.name_for_number(phonenumbertrack,'en')
print(Fore.GREEN+f'''Location:{track} Provider
Name:{carriername} 
Timezone:{time}''')
