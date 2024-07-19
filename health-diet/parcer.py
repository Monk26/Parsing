import lxml
import requests
import json
import csv
from bs4 import BeautifulSoup

url = "https://health-diet.ru/table_calorie"
head = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept" : "*/*"
}
# req = requests.get(url, headers=head).text

# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(req)


with open("all_categoties_dict.json", "r", encoding="utf-8") as file:
    all_categories = json.load(file)


count = 0
k = 0
for name, href in all_categories.items():
    sim = ["'", "-", " ", ","]
    
    for i in sim:
        if i in name:
            name = name.replace(i, "_")
    
    count +=1
    with open(f"data\{count}_{name}.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")
    
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue
    
    src = soup.find(class_="uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed").find("tr").find_all("th")
    product = src[0].text
    callories = src[1].text
    proteins = src[2].text
    fats = src[3].text
    carbohytrates = src[4].text
    
    with open(f"data\{count}_{name}.csv", "w", encoding="utf-8") as file:    
        writer = csv.writer(file)
        writer.writerow([product, callories, proteins, fats, carbohytrates])
        
    prod = soup.find("tbody").find_all("tr")
    
    for i in prod:
        list_datas = i.find_all("td")
        
        product = list_datas[0].text
        callories = list_datas[1].text
        proteins = list_datas[2].text
        fats = list_datas[3].text
        carbohytrates = list_datas[4].text
        p = [str(product), str(callories), str(proteins), str(fats), str(carbohytrates)]
        with open(f"data\{count}_{name}.csv", "a", encoding="utf-8") as file:    
            writer = csv.writer(file)
            writer.writerow([product, callories, proteins, fats, carbohytrates])
        
        
        
        
    
    
    
    
    