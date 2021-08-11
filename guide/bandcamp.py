from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options

opts = Options()
opts.set_headless()
assert opts.headless

browser = Edge(options=opts)
browser.get('https://duckduckgo.com')
