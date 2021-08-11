import requests
from bs4 import BeautifulSoup, element

url = "https://pythonjobs.github.io/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

all_jobs = soup.find_all("div", {"class": "job"})

for job in all_jobs:
    title_url = job.find_all("a")[1]
    print(title_url.get_text())

    job_info = job.find_all("span", {"class": "info"})
    job_info = [info.get_text().strip() for info in job_info]

    print(f"Location: {job_info[0]}")
    print(f"Date Post: {job_info[1]}")
    print(f"Type of contract: {job_info[2]}")
    print(f"Company: {job_info[3]}")

    job_detail = job.find("p", {"class": "detail"})
    print(f"{job_detail.get_text()}".strip())
    print("\n")
