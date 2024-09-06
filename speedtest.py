import subprocess
import time
import datetime
import re
import csv
from colorama import Fore, Style


command = ["speedtest",'--secure']
reecord = 'record.csv'
serial_number = 1
start_time = time.time()

def speed_test():
    global output,current_time, upload_speed, download_speed, serial_number
    output = subprocess.run(command,capture_output=True,text=True)
    download_speed = re.findall('Download: (.*) Mbit/s', output.stdout)
    upload_speed = re.findall('Upload: (.*) Mbit/s', output.stdout)
    current_time = datetime.datetime.now()
    status = ""

    if float(download_speed[0]) >= 20:
        status = "great"
    elif float(download_speed[0]) <= 8:
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

    with open(reecord, mode='a') as file:
        file_writer = csv.writer(file)
        file_writer.writerow([serial_number, current_time, download_speed[0], upload_speed[0],status]) 
    serial_number += 1
    

if __name__ == "__main__":
    # while time.time() - start_time < 3600:
    while True:
        speed_test()
        time.sleep(60)