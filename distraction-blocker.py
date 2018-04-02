import time
from datetime import datetime as dt

hosts_path="/etc/hosts"
redirect="127.0.0.1"
sitelist=["www.reddit.com","reddit.com","www.facebook.com","facebook.com","www.twitter.com","twitter.com","www.instagram.com","instagram.com","www.youtube.com","youtube.com","www.twitch.tv","twitch.tv"]

while True:
    if dt(dt.now().year, dt.now().month,dt.now().day,9) < dt.now() <
    dt(dt.now().year, dt.now().month,dt.now().day,16)
        print("You should be working")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for site in sitelist:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sitelist)
                file.truncate()
        print("Have fun!")
    time.sleep(5)
