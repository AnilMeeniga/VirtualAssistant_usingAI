from selenium import webdriver
Driver=webdriver.Chrome()
cdl=Driver.service.path

print("path",cdl)