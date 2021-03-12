from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)
mars_data = {}


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=True)

# Function to scrape the https://mars.nasa.gov/news/ and put the title and news into the mars_data dictionary
def nasa():
    url = 'https://mars.nasa.gov/news/'
    html = requests.get(url)
    soup = bs(html.text, 'lxml')
    # Retrieve the latest news Title and Paragraph text
    titleResults = soup.find('div', class_='content_title')
    newsResults = soup.find('div', class_='rollover_description_inner')
    nasaDict = {"title" : titleResults.a.text.strip()}
    nasaDict.update(news = newsResults.text)
    return nasaDict


def jpl():
    #Use splinter to navigate the site and find the image url for the current Featured Mars Image 
    JPL_URL = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'

    browser.visit(JPL_URL + 'index.html')
    # Click on the FULL IMAGE button
    browser.click_link_by_partial_text('FULL IMAGE')
    html = browser.html
    soup = bs(html, 'html.parser')
    imageResults = soup.find('div', class_='fancybox-inner')
    # If the link contains the image then assign it to a variable called featured_image_url.
    if imageResults.img:
        featureImageURL = JPL_URL + imageResults.img["src"]
        JPLDict = {"featureImageURL" : featureImageURL}
        return JPLDict

# Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
def spacefacts():
    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    marsFactsURL = 'https://space-facts.com/mars/'
    # Use Pandas to convert the data to a HTML table string.
    tables = pd.read_html(marsFactsURL)
    df = tables[0]
    html = df.to_html(index=False,header=False)
    spaceFactsDict = {"spacefacts" : html}
    return spaceFactsDict


def hempisheres():
    marsHemispheresURL = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere Enhanced", "img_url": ""},
        {"title": "Schiaparelli Hemisphere Enhanced", "img_url": ""},
        {"title": "Syrtis Major Hemisphere Enhanced", "img_url": ""},
        {"title": "Valles Marineris Hemisphere Enhanced", "img_url": ""}]
    hempDict = {}
    x = 0
    # Loop through the dictionary
    for i in hemisphere_image_urls:
        #print(i['title'])
        x = x + 1
        # Visit the main site 
        browser.visit(marsHemispheresURL)
        # Click on the link of the title from the dictionary
        browser.click_link_by_partial_text(i['title'])
        html = browser.html
        soup = bs(html, 'html.parser')
        # Get all li
        imageResults = soup.find_all('li')
        for image in imageResults:
            # If it is a href and its text is Sample then use its href link as the image url
            a = image.find('a')
            if a.text == 'Sample':
                imageURL = a['href']
                # Update the img_url 
                i.update({'img_url':imageURL})
                #print('after: ' + i['img_url'])
                hempDict.update({"hempisheres" + str(x) : i['title']})
                hempDict.update({"hempisheres_image_url" +str(x) : i['img_url']})
    #print(hempDict)            
    return hempDict

        

def scrape():
    browser = init_browser()

    # Call nasa function to scrape https://mars.nasa.gov/news/ and put the title and news into the mars_data dictionary
    mars_data = nasa()
    # Call jpl function to scrape https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/ and put featureImageURL into the mars_data dictionary
    mars_data.update(jpl())
    # Call spacefacts to scrape https://space-facts.com/mars/ and populate html table into the mars_data dictionary
    mars_data.update(spacefacts())
    # Call hempisheres to scrape https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars and populate those hempishere images into the mars_data dictionary
    mars_data.update(hempisheres())

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data


#xx = scrape()
#print(xx)