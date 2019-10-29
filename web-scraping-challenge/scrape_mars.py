from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


mars_data = {}
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    return webdriver.Chrome("windows/chromedriver")


def scrape_marsInfo():
    print("HELLOW WOWOWOWOWOWOOWOWOWOWOW")
    mars_data = scrape_news()
    #print(f"Mars Data ---- {mars_data}")
    mars_data = scrape_spaceImage()
    #print(f"Mars Data ---- {mars_data}")
    mars_data = scrape_marsWeather()
    #print(f"Mars Data ---- {mars_data}")
    mars_data = scrape_marsFacts()
    #print(f"Mars Data ---- {mars_data}")
    mars_data = scrape_hemisphereImg()
    print(f"Mars Data ---- {mars_data}")
    return mars_data
    


def scrape_news():
    browser = init_browser()
    news_url = 'https://mars.nasa.gov/news/'
    browser.get(news_url)
    time.sleep(1)
    news_html = browser.page_source
    news_soup = bs(news_html, 'html.parser')
    news_listing = news_soup.find('div', class_="list_text")
    news_title = news_listing.find('div', class_='content_title').text
    news_p = news_listing.find('div', class_='article_teaser_body').text
    print(f"News Title --> {news_title}")
    print(f"News P --> {news_p}")
    
    # Store data in a dictionary
    mars_data["news_title"] = news_title
    mars_data["news_summary"] = news_p
    #news_data = {"news_title": news_title, "news_summary": news_p}
    # Close the browser after scraping
    browser.close()
    # Return results
    return mars_data


def scrape_spaceImage():

    browser = init_browser()
    jpl_space_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.get(jpl_space_url)
    time.sleep(1)
    jpl_space_html = browser.page_source
    jpl_space_soup = bs(jpl_space_html, 'html.parser')

    jplspace_base_url = "https://www.jpl.nasa.gov"
    carasouel_items = jpl_space_soup.find_all('div', class_="carousel_items")
    for item in carasouel_items:
        image_url = item.find('article', class_="carousel_item").find('footer').find('a')["data-fancybox-href"]
        featured_image_url = jplspace_base_url + image_url
        print(featured_image_url)
        mars_data["featured_img"] = featured_image_url
        #featured_img = {"featuredImg": featured_image_url}

    # Close the browser after scraping
    browser.close()
    # Return results
    return mars_data

def scrape_marsWeather():

    browser = init_browser()
    mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.get(mars_weather_url)
    time.sleep(1)
    mars_html = browser.page_source
    mars_soup = bs(mars_html, 'html.parser')

    tweet_content = mars_soup.find_all('div', class_="js-tweet-text-container")
    
    for tweet in tweet_content:
        tweet_str =  tweet.find('p',class_="tweet-text").text
        mars_data["marsWeather"] = tweet_str
        #tweet_data = {"tweet" : tweet_str)
        print(tweet_str)
        break
    
    # Close the browser after scraping
    browser.close()
    # Return results
    return mars_data

def scrape_hemisphereImg():

    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.get(url)
    time.sleep(1)
    html = browser.page_source
    soup = bs(html, 'html.parser')
    image_pathUrls = []
    image_listing = soup.find_all('div', class_="item")
    print(len(image_listing))
    for image_list in image_listing:
        image_pathUrls.append(image_list.find('a')['href'])

    base_url = "https://astrogeology.usgs.gov"
    hemisphere_image_urls = []
    for imagepath in image_pathUrls:
        url_path = base_url+imagepath
        print(url_path)
        browser.get(url_path)
        html_inner = browser.page_source
        soup_inner = bs(html_inner, 'html.parser')
    
    
        hem_img_url =  base_url + soup_inner.find('img', class_='wide-image')['src']
        hem_img_title = soup_inner.find('h2', class_='title').text
        hemisphere_dict = {"title" : hem_img_title, "img_url": hem_img_url}
    
        print(hem_img_url)
        print(hem_img_title)
        hemisphere_image_urls.append(hemisphere_dict)
        mars_data["hemi_url"] = hemisphere_image_urls
    
    # Close the browser after scraping
    browser.close()
    # Return results
    return mars_data

def scrape_marsFacts():

    facts_url = 'https://space-facts.com/mars/'
    facts_tables = pd.read_html(facts_url)
    mars_facts_df = facts_tables[1]
    mars_facts_df.columns=["Description","Value"]
    mars_facts_df.set_index("Description", inplace=True)    
    html_facts_table = mars_facts_df.to_html()
    mars_data["Facts"] = html_facts_table
    print(html_facts_table)
    # Return results
    return mars_data

#print(scrape_marsInfo())