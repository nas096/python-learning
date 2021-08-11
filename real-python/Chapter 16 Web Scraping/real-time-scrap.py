import time
import mechanicalsoup

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    print(f"The result of your dice is {tag.text}")

    this_time = page.soup.select("#time")[0]
    print(f"The current time is {this_time.text}")

    time.sleep(15)