from selenium import webdriver
import time

options = webdriver.ChromeOptions()
path=r"D:\Selenium Drivers\chromedriver.exe"
exPath=r"D:\Selenium Drivers\chUSEx.crx"
options.add_extension(exPath)
time.sleep(5)
chrome = webdriver.Chrome(executable_path=path, options=options)
chrome.get("http://ipinfo.io")