import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower())

python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs]

for job_element in python_jobs_elements:
    apply_links = job_element.find_all("a", text="Apply")
    learn_links = job_element.find_all("a", text="Learn")
    for link in apply_links:
        link_url = link['href']
        print(f"Apply here: {link_url}")

    for link in learn_links:
        link_url = link['href']
        print(f"Learn here: {link_url}")
