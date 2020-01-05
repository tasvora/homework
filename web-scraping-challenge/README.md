# Mission to Mars


Flask web application that scrapes various websites for data related to the Mars Mission and displays the information in a single HTML page. 

### Scrapping 

#### NASA Mars News
* Script collects the latest News Title and Paragraph Text.

#### JPL Mars Space Images - Featured Image

* Script finds the image url for the current Featured Mars Image and assigns the url string of the full size image.

#### Mars Weather

* Script visits the Mars Weather twitter account and scrapes the latest Mars weather tweet. 

#### Mars Facts

* Script visit the Mars Facts webpage and uses Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

#### Mars Hemispheres

* Script visits the USGS Astrogeology site and obtains the full resolution images for each of Mar's hemispheres.


### MongoDB and Flask Application

The MongoDB is database used to store all scraped data. It is run locally for this application.

Flask application is used to make the routes and also gives an option on the homepage to scrape new data.

### Requirements 

* Modules Required 
    * pandas==0.24.2
    * selenium==3.141.0
    * pymongo==3.8.0
    * numpy==1.16.4
    * Flask==1.1.1
    * requests==2.22.0
    * beautifulsoup4==4.7.1
    * Flask-PyMongo==2.3.0


![Screenshot_Mars_Data](images/Screenshot_Mars_Data.png)
