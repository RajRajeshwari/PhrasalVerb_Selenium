FAQs:
-----
Q: Why was this task assigned?
A: During meetings we would often encounter phrasal verbs in sentences and there was often misalignment due to it. We don't even have a robust multi-word dictionary.
The main problem which we face during machine translation is of multi-word expressions. 
	For example: He looke up in the sky. [here up is preposition]
		     He looked up the word in the dictionary. [here look up is a phrasal verb]
To solve such ambiguity, one of the method is to make the list of all the phrasal verbs, compounds etc under respective groups. 

Q: Where will it be integrated?
A: These lists will be integrated in our system and help improve machine translations.

Q: Why Selenium?
A: Tools like beautifulsoup are sufficient when scraping data from static webpages. When scraping from dynamic websites, we require to perform few additional action events(scroll, click, etc.). Selenium is perfect for tasks such as these. 
	"Selenium is an automation testing framework for web applications/websites which can also control the browser to navigate the website just like a human. 
	 Selenium uses a web-driver package that can take control of the browser and mimic user-oriented actions to trigger desired events."
	 
Q: Where to study Selenium?
A: 1.https://www.pluralsight.com/guides/web-scraping-with-selenium
   2.After that just experiment and look up for errors on stackoverflow

Q: How to I access/click/type in textbox/clear textbox using the 'x' button/click 'see more..' etc?
A: Each element on the webpage has a name(class) and ID. We access the elements using this information. You can check https://www.guru99.com/accessing-forms-in-webdriver.html (some errors in site..change)

Q: How do I extract multiple glosses of the same word?
A: All the elements in the website has an ID and/or a class name. Using that information we can see that all the meaning/sense for a word will be given under a certain class name. For example in Mac-Millian the meaning for all the senses where under the div named "SENSE". Using find_elements(to find all possible occurance of the element with that name) instead of find_element(which gives only the first occurance of that element). 

Pre-processing:
---------------
1. Go to https://www.usingenglish.com/reference/phrasal-verbs/list.html
2. Then press Ctrl+P to print the file in PDF format.
3. The list of phrasal verbs was extracted from the pdf using the command pdftotext as follows:
	pdftotext PhrasalVerbsList-UsingEnglish.com.pdf PhrasalVerbs.txt
4. Then the spaces were removed manually from the converted text file.
	Ctrl+H
	Replace \n by 00
	Replace 00 by 0
	Replace 0 by \n

Finding the meaning for each of the phrasal verbs:
--------------------------------------------------
To find the meaning of the phrasal verbs, we will be doing web-scraping(using selenium) from the website:www.macmillandictionary.com(not using ludwig.guru because there is some limitation for taking text from the pop of "see more" in the website for input word(s)).

