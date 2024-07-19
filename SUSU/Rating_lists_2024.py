from bs4 import BeautifulSoup
import lxml
import requests
import csv

url = "https://abit.susu.ru/rating/"
req = requests.get(url).text

with open("index.html", "w", encoding = "utf-8") as file:
    file.write(req)
    
with open("index.html", "r", encoding = "utf-8") as file:
    soup = BeautifulSoup(file, "lxml")
    
src = soup.find("tbody").find_all("tr")

institutes_list = ["Высшая школа электроники и компьютерных наук",
                  "Институт естественных и точных наук"
                  ]
directions_list = ["02.03.02 Фундаментальная информатика и информационные технологии(Интеллектуальные системы)",
                  "09.03.01 Информатика и вычислительная техника",
                  "09.03.04 Программная инженерия(Инженерия информационных и интеллектуальных систем)",
                  "01.03.02 Прикладная математика и информатика(Прикладная математика и искусственный интеллект)"
    
]

for item in src:
    td_list = item.find_all("td")
    
    institute = td_list[2].text
    institute = institute.replace("Подразделение: ", "")
    
    direction = td_list[0].text
    direction = direction.replace("Направление/Специальность: ", "")
    
    if (institute in institutes_list) and (direction in directions_list):
        rate = url + td_list[4].find("a").get("href")
        req = requests.get(rate).text
        
        with open(f"{institute}\directions_html\{direction}.html", "w", encoding="utf-8") as file:
            file.write(req)
        
        with open(f"{institute}\Rate\{direction}.csv", "w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Снилс","Конкурс", "Баллы", "Достижения", "Высший приоритет", "Приоритет"])
        
        with open(f"{institute}\directions_html\{direction}.html", "r", encoding="utf-8") as file:
            soup_dir = BeautifulSoup(file, "lxml")
        
        src_dir = soup_dir.find(class_ = "rating_single").find("tbody").find_all("tr")
        
        for g in src_dir:
            enrollee_data = g.find_all("td")
            if len(enrollee_data) >5:
                snils = enrollee_data[1].text
                snils = snils[snils.index(":")+2:]
                
                type_place = enrollee_data[2].text
                type_place = type_place[type_place.index(":")+2:]
                
                sum_points = enrollee_data[3].text
                sum_points = sum_points[sum_points.index(":")+2:].replace("-", "0")
                
                individual_achievements = enrollee_data[4].text
                individual_achievements = individual_achievements[individual_achievements.index(":")+2:]
                
                highest_priority = enrollee_data[6].text
                highest_priority = highest_priority[highest_priority.index(":")+2:]
                
                priority = enrollee_data[7].text
                priority = priority[priority.index(":")+2:]
                
                with open(f"{institute}\Rate\{direction}.csv", "a", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow([snils, type_place, sum_points, individual_achievements, highest_priority, priority])
                
                

    
        
        
        
        
    
