import subprocess
import time
import datetime
import re
import csv
from colorama import Fore, Style
import pyfiglet

command = ["speedtest",'--secure']
reecord = 'record.csv'
serial_number = 1
start_time = time.time()
banner = pyfiglet.figlet_format("SPEED 1.0.1")
print(Fore.GREEN + banner + Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX+"Built by Avict18"+Style.RESET_ALL)
high = float(input(Fore.MAGENTA+"please place the speed to rank as great!: " + Fore.GREEN))
low = float(input(Fore.MAGENTA+"please place the minimum speed that is expected: "+Fore.RED))

def speed_test():
    print(Style.RESET_ALL)
    global output,current_time, upload_speed, download_speed
    output = subprocess.run(command,capture_output=True,text=True)
    download_speed = re.findall('Download: (.*) Mbit/s', output.stdout)
    upload_speed = re.findall('Upload: (.*) Mbit/s', output.stdout)
    current_time = datetime.datetime.now()
    status = ""

    if float(download_speed[0]) >= high:
        status = "great"
    elif float(download_speed[0]) <= low:
        status = "bad"
    else:
        status = "okay"

    print(Fore.CYAN+f'Data recorded')
    print(Fore.GREEN+f'Download speed: {download_speed[0]}Mbps\t'+Fore.YELLOW+f'Upload speed: {upload_speed[0]}Mbps')
    print(Style.RESET_ALL)
    if status == "great":
        print("STATUS: "+Fore.LIGHTGREEN_EX+"great")
    elif status == "okay":
        print("STATUS: "+Fore.LIGHTBLUE_EX+"okay")
    else:
        print("STATUS: "+Fore.RED+"bad")
    print(Fore.RED+"="*20)

    with open(reecord, mode='a') as file:
        file_writer = csv.writer(file)
        file_writer.writerow([serial_number, current_time, download_speed[0], upload_speed[0],status]) 
    

if __name__ == "__main__":
    while True:
        speed_test()
        serial_number += 1
        time.sleep(60)