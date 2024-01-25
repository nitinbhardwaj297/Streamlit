from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def ptr(a,pat):
    pattern_to_remove = re.compile(pat)
    fl = [item for item in a if not pattern_to_remove.search(item)]
    return fl

# Replace these with your Instagram credentials
def cmntsget(un,pas,pu):
    # Create a webdriver object
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    #driver = webdriver.Chrome()
    # Navigate to the Instagram login page
    driver.get("https://www.instagram.com/accounts/login/")

    # Wait for the page to load
    time.sleep(5)
    print("ig page loaded!")

    # Find the username and password input fields and fill them in
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(un)
    password_input.send_keys(pas)
    # Submit the form
    login_button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
    login_button.click()
    time.sleep(5)
    print("log in done!")
    # Wait for the login to complete (you might need to adjust the time based on your internet speed)
    notnow = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
    notnow.click()
    print("save info:not now clicked!")
    time.sleep(5)
    noti = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
    noti.click()
    print("no notification clicked")
    time.sleep(3)
    #go to post
    driver.get(pu)
    time.sleep(3)
    print("loaded post page")
    #load comments
    se=driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]")
    time.sleep(2)
    scroll_script = "arguments[0].scrollTo(0, arguments[0].scrollHeight);"
    for i in range(100):
        driver.execute_script(scroll_script, se)
        time.sleep(1)
    print("scrolling done!")
    #cmtwin = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]")
    #print(cmtwin)
    cs = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]")
    a=cs.text.split("\n")
    print("got em cmnts!")
    p1=r'View all.* replies$'
    p2=r'^ (\d+ d|\d+ h|\d+ m|\d+ w|\d +s)$'
    p3=r'^.*(\d+ like|\d+ likes)$'
    p4=r'^See translation$'
    p5=r'^Reply$'
    a=ptr(a,p1)
    a=ptr(a,p3)
    a=ptr(a,p4)
    a=ptr(a,p5)
    driver.close()
    pt1 = 0
    pt2 = 0
    ml=[]
    for i in range(len(a)):
        if re.match(r'^ (\d+ d|\d+ h|\d+ m|\d+ w|\d +s)$',a[i]):
           pt1=i
           j=pt1+1
           while j<len(a):
                if re.match(r'^ (\d+ d|\d+ h|\d+ m|\d+ w|\d +s)$',a[j]):
                   pt2=j
                   break
                else:
                    j=j+1
           ta = a[pt1-1:pt2-1]
           ml.append(ta)
    for i in ml:
        for j in i:
            if re.match(r'^ (\d+ d|\d+ h|\d+ m|\d+ w|\d +s)$',j):
                i.remove(j)
    data={}
    for i in ml:
        if len(i) != 0:
            u=i[0]
            s=""
            for j in range(1,len(i)):
                s=s+" "+i[j]
            data.update({u:s})
    return data