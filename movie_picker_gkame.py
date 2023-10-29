# The program is to create an app which suggests a movie based on the genre selected by the user. 

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import random
driver=webdriver.Chrome()
driver.maximize_window()
#the web application used to get the movie data is IMDB
driver.get("https://www.imdb.com/")
page =driver.execute_script('return document.readyState;')
if page=='complete':
    print("Page loaded Successfully")
else:
    print("The page is ",page)
    time.sleep(5)
    driver.refresh()
    page =driver.execute_script('return document.readyState;')
    if page=='complete':
        print("Page loaded Successfully")
    else:
        print("There is some issue loading the page. Please restart the app")
#Creating a database to suggest a movie from respective genre
try:
    driver.find_element('xpath','//div//label[@id="imdbHeader-navDrawerOpen"]').click()
    categories= driver.find_elements('xpath','//div[@data-testid="list-container"]//div//ul//a//span')
    for i in categories:
        if not i.text=='':
            #print(i.text)
            if i.text=='Browse Movies by Genre':
                i.click()
                break
    scrollable_element = driver.find_element('id','jump-to')
    js_code = "arguments[0].scrollIntoView();"
    driver.execute_script(js_code, scrollable_element)
    select= Select(driver.find_element('id','jump-to'))
    driver.find_element('xpath','//div//span[@data-testid="jumpTo"]//span').click()
    #collecting the various genre available
    for i in select.options:
        print(i.text)
        if i.text=='Popular movies by genre':
            i.click()
            break
    genre= driver.find_elements('xpath','//section//div//a//h3//span[contains(text(),"Popular movies by genre")]//following::div[1]//div[@class="ipc-chip-list__scroller"]/a')
    movies_genre=[]
    movie_titles=[]
    movie_list=[]
    movie_href_genre=[]
    movie_dict={'Genre':movies_genre, 'URL': movie_href_genre}
    for i in genre:
        #print(i.text)
        href= i.get_attribute('href')
        #print(href)
        movie_href_genre.append(href)
        movies_genre.append(i.text)
    #movie_dict = {movies_genre[i]: movie_href_genre[i] for i in range(len(movies_genre))}
    movie_data= pd.DataFrame.from_dict(movie_dict,orient='index')
    movie_data= movie_data.T
    movie_data.to_excel("Movie_Data.xlsx",index=False)
    print('_______________________________________________________'*2)
    print("The Genre available are \n",('\n').join(movies_genre))
    print('_______________________________________________________'*2)
    required_genre= input("Please input your genre from the displayed details:")
    for a in range(len(movie_data)):
        if movie_data['Genre'].iloc[a]==required_genre:
            url= movie_data['URL'].iloc[a]
            driver.get(url)
            time.sleep(2)
            movie_titles= driver.find_elements('xpath','//div[@class="lister list detail sub-list"]//h3//a')        
            for data in movie_titles:
                movie_list.append(data.text)
    print("Automation suggests you to watch ---------",random.choices(movie_list)[0])
    print("Enjoy your movie.")
    driver.close()
except Exception as e:
    print("The following error occured",e.args[0])
    print("Please restart application")