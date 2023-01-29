from selenium import webdriver
import psutil
import os


def quizonline():
    driver = webdriver.Chrome()
    url = "https://forms.gle/4cK2RZFcet7B6Ped6/"
    driver.get(url)
    while (True):
        driver_len = len(driver.window_handles)
        if driver_len > 1:
            ch = driver.window_handles[1]
            driver.switch_to.window(ch)
            driver.close()
        a = 1
        while (a == 1):
            os.system("taskkill/im vlc.exe")
            os.system("taskkill/im brave.exe")
            os.system("taskkill/im POWERPNT.EXE")
            os.system("taskkill/im WINWORD.EXE")
            os.system("taskkill/im Discord.exe")
            os.system("taskkill/im EXCEL.EXE")
            a = a-1
