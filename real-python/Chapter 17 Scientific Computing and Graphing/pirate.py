from pathlib import Path
import csv
from matplotlib import pyplot as plt

csv_path = Path.home() / \
    "python-basics-exercises\ch17-scientific-computing-and-graphing\practice_files\pirates.csv"


pirate_lists = []
temperature_lists = []
years = []
with csv_path.open(mode="r", encoding="utf-8") as file:

    csv_data = csv.DictReader(file)

    for row in csv_data:
        pirate_lists.append(row['Pirates'])
        temperature_lists.append(row['Temperature'])
        years.append(row['Year'])


plt.xlabel("Pirates")
plt.ylabel("Global Temperature")
plt.title("The relation between the numbers of pirates and the global temperatures")


plt.plot(pirate_lists, temperature_lists)

plt.scatter(pirate_lists, temperature_lists)

for i, year in enumerate(years):
    plt.annotate(year, (pirate_lists[i], temperature_lists[i]))

plt.show()
plt.savefig('Pirates.png')
