from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    # Set up Splinter
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # return browser = Browser('chrome', **executable_path, headless=False)

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

    #scrape news site
    news_title, news_p = scrape_news(browser)
    featured_image_url = scrape_images(browser)
    mars_html_table = mars_html_table(browser)

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_html_table": str(mars_html_table)

    }
    # Close the browser after scraping
    browser.quit()

    return mars_data

def scrape_news(browser):
    

    # Visit mars website
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get title from mars website
    news_title = soup.find_all('div', class_='content_title')[0].text

    # Get paragraph from mars website
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text

    # # Get the max avg temp
    # max_temp = avg_temps.find_all('strong')[1].text

    # # BONUS: Find the src for the sloth image
    # relative_image_path = soup.find_all('img')[2]["src"]
    # sloth_img = url + relative_image_path


    # Return results
    return news_title, news_p

def scrape_images(browser):
    image_url="https://spaceimages-mars.com"
    browser.visit(image_url)
    html = browser.html
    image_soup = bs(html, 'html.parser')
    relative_image_path = image_soup.find_all('img')[3]["src"]
    featured_image_url = image_url + "/" + relative_image_path 

    return featured_image_url

def scrape_table(browser):
    facts_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(facts_url)
    mars_facts_df = tables[1]
    mars_facts_df.columns = ["Description", "Value"]
    mars_facts_df
    mars_html_table = mars_facts_df.to_html()

    return mars_html_table

 