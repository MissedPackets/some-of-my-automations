# import webdriver 
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
id=19
url = f"https://www.myopenmath.com/embedq2.php?id={id}"
driver.get(url)
search_text = '''{7}{x}'''
iter=99999999999
for i in range(iter):
    print('searching for:',search_text)
    # note: getting source has to be within the scope here, if it is saved in global, it will save it until the loop ends(you don't want that):
    get_source = driver.page_source
    search=(search_text in get_source)
    if search ==False:
        print('false')
        driver.find_element(By.CLASS_NAME,"secondary").click()

    if search==True:
        print('TRUE')
        break;



