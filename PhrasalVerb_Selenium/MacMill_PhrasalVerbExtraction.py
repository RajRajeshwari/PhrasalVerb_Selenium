import io
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# the driver path to open the chrome browser automatically
browser = webdriver.Chrome('/home/rajrajeshwari/Internship/Selenium/chromedriver_linux64/chromedriver')

# a list of all phrases can be found at : /home/rajrajeshwari/Internship/phrasalVerb/PhrasalVerbs.txt

# the final output dictionary of phrasal verb path (file is being opened in append mode):
PhrasalVerbGloss = open('/home/rajrajeshwari/Internship/phrasalVerb/PhrasalVerbsGloss.txt','a')
# take input from the terminal
phrase = sys.argv[1]
# writing the phrasal verb being searched in the final phrasal verb dictionary
PhrasalVerbGloss.write(phrase)
browser.get('https://www.macmillandictionary.com/')
time.sleep(2)                #wait time
 # the search box name is search_input in www.macmillandictionary.com website
search = browser.find_element(By.ID, 'search_input')
# sending the phrase to be searched
search.send_keys(phrase)
time.sleep(2)                   #wait time
# sending enter key event to search the word in the dictionary
search.send_keys(Keys.ENTER)
# find_elements will give us the list of all elements with class name 'SENSE' (as named in macmillandictionary.com)
definition = browser.find_elements(By.CLASS_NAME, 'SENSE')
# writing the gloss in the output file
if len(definition) != 0 :
    for j in definition:
        # print(j.text)
        PhrasalVerbGloss.write(j.text + "\n")
    PhrasalVerbGloss.write("-------------------------------------" + "\n")
else:
    PhrasalVerbGloss.write("NULL" + "\n")
PhrasalVerbGloss.close()
