from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars = {}

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars["x"] = soup.find("div", class_="collapsible results")
    # mars["y"] = soup.find("div", class_="item").get_text()
    # mars["z"] = soup.find("div", class_="item").get_text()

    return mars