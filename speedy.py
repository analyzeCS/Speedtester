import requests # not really needed
import socket #also doesnt matter if its there
import os 
import time
import speedtest

os.system('cls' if os.name == 'nt' else 'clear')

user = input("press enter to start the speedtest: ")

if user == "input": 
    started = "Starting speedtest..."
    print(started) 

os.system('cls' if os.name == 'nt' else 'clear')

banner = """ 
________                 _________        
__  ___/_______________________  /____  __
_____ \___  __ \  _ \  _ \  __  /__  / / /
____/ /__  /_/ /  __/  __/ /_/ / _  /_/ / 
/____/ _  .___/\___/\___/\__,_/  _\__, /  
       /_/                       /____/   
"""

print(banner)
center = "Made by Neky" 
middle = center.center(50)

print(middle)
center2 = "t.me/mumbus200"
middle2 = center2.center(50)
print(middle2)

center3 = "https://github.com/analyzeCS"
middle3 = center3.center(50)
print(middle3)


# get local IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()

# get piblic IP 
try:
    public_ip = requests.get('https://api.ipify.org').text
    print("\nNetwork Information:")
    print("-" * 50)
    print(f"🌐 Local IP Address:  {local_ip}")
    print(f"🌍 Public IP Address: {public_ip}")
    print("-" * 50)
except Exception as e:
    print(f"Error getting public IP: {e}")

print("\n")

#an function to check internet speed
def check_internet_speed():
    st = speedtest.Speedtest()

    print("...Starting test...")
#testing download and upload speed
    download_speed = st.download() / 1_000_000 
    upload_speed = st.upload() / 1_000_000


    st.get_best_server() 
    ping = st.results.ping 

#returning the results as a dictionary
    return {   

    'download': round(download_speed, 2),
    'upload': round(upload_speed, 2),
    'ping': round(ping, 2),
    }

spedtest = check_internet_speed()

print(f"📉Download Speed: {spedtest['download']} Mbps")
print(f"⬆️Upload Speed: {spedtest['upload']} Mbps")   
print(f"🛜Ping: {spedtest['ping']} ms")

time.sleep(3)
   
