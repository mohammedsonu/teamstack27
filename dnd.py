import time
from datetime import datetime as dt


def sonu():
    hosts_path = "C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"
    website_list = ["www.facebook.com", "facebook.com",
                    "www.instagram.com", "instagram.com"]
    print("im running")

    while True:

        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        print("blocked")
        break
