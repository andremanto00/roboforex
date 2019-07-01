from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyfiglet
import requests

class Bdswissbot():
    def __init__(self, email, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.email = email
        self.password = password

    def signIn(self):
        ascii_banner = pyfiglet.figlet_format("Roboforex")
        print("\n")
        print(ascii_banner)
        print("\n - Development by @andre_manto_ (instagram) \n\n")

        self.browser.get('https://dashboard.bdswiss.com/trade/forex/6418877')
        time.sleep(3)
        emailInput = self.browser.find_element_by_id('email')
        passwordInput = self.browser.find_element_by_id('password')
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
        self.browser.get('https://trade.bdswiss.com/?embedded=true&login=6418877')
        i = 0
        while(i < 10):
            print("Loading      -->       "+str(i+1)+"/10")
            time.sleep(1)
            i = i + 1

    # Cerca la valuta e click su sell o buy
    def searchValues(self, valuta, action, lot, sl, tp):
        cerca = self.browser.find_element_by_id('assetsSearchInput')
        k = 0
        while(k<10):
            cerca.send_keys(Keys.DELETE)
            cerca.send_keys(Keys.BACKSPACE)
            time.sleep(0.1)
            print("Delete old      -->       "+str(k+1))
            k = k + 1
        cerca.send_keys(valuta)
        cerca.send_keys(Keys.ENTER)
        print("E' stato selezionato: " + valuta)
        time.sleep(1)
        print("Loading...")
        time.sleep(1)
        if(action == "SELL"):
            self.browser.execute_script("document.getElementsByClassName('btn-outline-danger')[0].click()")
            print("  --->   SELL")
        else:
            self.browser.execute_script("document.getElementsByClassName('btn-outline-success')[0].click()")
            print("  --->   BUY")
        i = 0
                
        print("\n Take profit search and delete older... \n")
        
        #tp search and delete older
        item = self.browser.find_elements_by_tag_name('input')[21]
        item.click()
        item.clear()

        k = 0
        while(k<10):
            item.send_keys(Keys.DELETE)
            item.send_keys(Keys.BACKSPACE)
            time.sleep(0.2)
            print("Loading      -->       "+str(k+1))
            k = k + 1
        #take profit --> tp
        item.send_keys(tp) 
        print("\n Take profit --> SUCCESS \n")
        
        #sl search and delete older
        item = self.browser.find_elements_by_tag_name('input')[23]
        item.click()
        item.clear()

        k = 0
        while(k<10):
            item.send_keys(Keys.DELETE)
            item.send_keys(Keys.BACKSPACE)
            time.sleep(0.2)
            print("Loading      -->       "+str(k+1))
            k = k + 1
        #stop loss --> sl
        item.send_keys(sl) 
        print("\n Stop Loss --> SUCCESS \n")

        
        #lots search and delete older
        item = self.browser.find_elements_by_tag_name('input')[19]
        item.click()
        item.clear()
        
        k = 0
        while(k<10):
            item.send_keys(Keys.DELETE)
            item.send_keys(Keys.BACKSPACE)
            time.sleep(0.2)
            print("Loading      -->       "+str(k+1))
            k = k + 1
        #lots --> sl
        item.send_keys(lot) 
        print("\n Lots --> SUCCESS \n")

        # send all
        self.browser.execute_script("document.getElementsByClassName('black_button')[0].click()")
        

    def closeBrowser(self):
        self.browser.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()


#login
bot = Bdswissbot('USERNAME', 'PASSWORD')
bot.signIn()

#richieste al server di segnali per l'invio del segnale solo per inseire un nuovo trade
old = ''
while True:
    r = requests.get('http://localhost/bdswiss_bot/test.php')
    if(r.text != old):
        print("")
        print("NUOVO SEGNALE")
        print(r.text)
        print("")
        x = (r.text).split(',')
        bot.searchValues(x[0],x[1],x[2],x[3],x[4])
        old = r.text
    else:
        print(r.text + " --> Segnale già ricevuto")
    time.sleep(1)
    
    
