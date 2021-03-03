#github.com/alpkeskin
from selenium import webdriver
from selenium.webdriver import ActionChains
import time, pickle
from os import path
from requests_html import HTMLSession

def bot(twit):
	driver = webdriver.Chrome()
	driver.get("https://twitter.com/login")
	time.sleep(3)
	if(str(path.exists("cookies4bot.pkl")) == "False"):

		USERNAME = " SET USERNAME "
		PASSWORD = " SET PASSWORD "

		driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(USERNAME)
		driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(PASSWORD)
		driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
		pickle.dump( driver.get_cookies() , open("cookies4bot.pkl","wb"))

	cookies = pickle.load(open("cookies4bot.pkl", "rb"))
	for cookie in cookies:
	    driver.add_cookie(cookie)
	driver.get("https://twitter.com")
	time.sleep(3)
	driver.find_element_by_class_name('DraftEditor-root').click()
	element=driver.find_element_by_class_name('public-DraftEditorPlaceholder-root')
	ActionChains(driver).move_to_element(element).send_keys(twit).perform()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span').click()
	time.sleep(1)
	driver.quit()

def dominance():
	session = HTMLSession()
	r = session.get("https://tr.tradingview.com/symbols/CRYPTOCAP-BTC.D/")
	current_sleep = 2
	element_count = 0
	while element_count == 0:
		r.html.render(sleep=current_sleep)
		elements = r.html.xpath('//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[1]')
		element_count = len(elements)
		current_sleep += 2
		if current_sleep == 10:
			return "Timeout"
	return elements[0].text

def main():
	counter = 0
	while True:
		btcd = dominance()
		twit = '$BTC Dominance : '+btcd+' \n $ETH $ADA #crypto #altcoin '
		bot(twit)
		counter += 1
		print("Number of posts: "+ str(counter))
		time.sleep(3600) # a hour

main()
