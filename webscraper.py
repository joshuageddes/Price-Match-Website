#flask-hack
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as p
from bs4 import BeautifulSoup as soup
import mechanicalsoup
from urllib.request import urlopen
import requests
import math
import numpy
import matplotlib
import pandas
import re

browser = webdriver.Firefox()

#return redirect(url_for('dashboard'))

#
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
	return render_template('index.html')

@app.route("/scrape")
def scrape():
	print("ASD")
	myFile=open('C:/Users/calvi/Desktop/flask-hack/templates/index.html','r')
	soup=soup(myFile,"html5lib")
	query = (soup.find_all('<input name="semail1"'))
	print(query)

	browser.get('C:/Users/calvi/Desktop/flask-hack/templates/index.html')

	#nofrills
	browser.get(f"https://www.nofrills.ca/search?search-bar={query}")
	try:
		ontarioBut = browser.find_element_by_xpath("/html/body/div[1]/div/div[5]/div[2]/div/div/ul/li[7]/button")
		ontarioBut.click()
		nofrillsPrice = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/main/div/div/div/div[2]/div/div[2]/div[2]/div/ul/li[1]/div/div/div[3]/div[2]/ul[1]/li/span")
		print(nofrillsPrice.text)
	except:
		pass

	#superstore
	try:
		browser.get(f"https://www.realcanadiansuperstore.ca/search?search-bar={query}")
		ontarioBut2 = browser.find_element_by_xpath("/html/body/div[1]/div/div[5]/div[2]/div/div/ul/li[4]/button")
		ontarioBut2.click()
		superstorePrice = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/main/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/ul/li[1]/div/div/div[3]/div[2]/ul[1]/li/span")
		print(superstorePrice.text)
	except:
		pass

	#metro
	try:
		browser.get(f"https://www.metro.ca/en/search?filter={query}&freeText=true")
		metroPrice = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div[6]/div/div[3]/div/div[3]/div[1]/div/div[3]/div[1]/div/div/div[1]")
		print(metroPrice.text)
	except:
		pass
	return render_template("scraper.html",nfPrice = nofrillsPrice, sPrice = superstorePrice, mPrice = metroPrice)

if __name__ == "__main__":
	app.run(debug=True)


















