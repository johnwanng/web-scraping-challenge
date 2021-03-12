## web-scraping-challenge
Web Scraping Homework - Mission to Mars

## Introduction

This exercise will scrape various web sites using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

First we will scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.


Next, we visit JPL Mars Space web site and use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.


Then we visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

Finally, we visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres. Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

In the final exercise, we use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.


## Technologies
 
Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter, MongoDB, Flask, HTML, CSS and Bootstrap
 
## Setup 

1. Download and extract the zip file

2. Open Terminal (on Mac) or Open Bash (on PC)

3. Navigate to the web-scraping-challenge folder

4. Open and run the app.py file

5. Click on the 'Scrape New Data' button on the top of the web page.
