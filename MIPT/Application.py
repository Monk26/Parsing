import json
import csv

#перевод с рус на англ
directions_translator= {"Авиационные технологии и автономные транспортные системы" : "aviatech",
                "Биотехнология" : "biotech",
                "Биофизика и биоинформатика" : "biophys",
                "Геокосмические науки и технологии" : "geospace",
                "Компьютерные технологии и вычислительная техника" : "pc_tech",
                "Математическое моделирование и компьютерные технологии" : "mathmatical",
                "Общая и прикладная физика" : "applied_phys",
                "Прикладная математика и информатика" : "applied_math",
                "Природоподобные" : "natural_like",
                "Программная инженерия и компьютерные технологии" : "soft_engin_pc_tech",
                "Программная инженерия" : "soft_engin",
                "Радиотехника и компьютерные технологии" : "radion_engin",
                "Системное программирование и прикладная математика" : "sys_prog",
                "Техническая физика" : "phys_tech",
                "Физика перспективных технологий" : "phys_tech_promising",
                "Экономика и ERP системы" : "economics",
                "Электроника и наноэлектроника" : "nanoelect",
}

#количество мест на направления
number_of_seats= {"Авиационные технологии и автономные транспортные системы" : 28,
                "Биотехнология" : 50,
                "Биофизика и биоинформатика" : 50,
                "Геокосмические науки и технологии" : 58,
                "Компьютерные технологии и вычислительная техника" : 16,
                "Математическое моделирование и компьютерные технологии" : 127,
                "Общая и прикладная физика" : 189,
                "Прикладная математика и информатика" : 165,
                "Природоподобные" : 35,
                "Программная инженерия и компьютерные технологии" : 36,
                "Программная инженерия" : 448,
                "Радиотехника и компьютерные технологии" : 95,
                "Системное программирование и прикладная математика" : 30,
                "Техническая физика" : 15,
                "Физика перспективных технологий" : 88,
                "Экономика и ERP системы" : 10,
                "Электроника и наноэлектроника" : 37,
}

#список всех абитуриентов формата {snils : {priority: [direction, score]}}
applicants = dict()

#запись данных абитуриента в формат {snils : {priority: [direction, score]}}
def add_in_applicants(data : dict, direction : str):
    for item in data:
        id = item["id"]
        priority = int(item["priority"])
        score = int(item["score"])
        
        if id in applicants:
            applicants[id][int(priority)] = [direction, score]
        if id not in applicants:
            applicants[id] = {int(priority):[direction, score]}

#перепись из файла .json в applicants
def create_all_applicants():
    with open("SRC\Авиационные технологии и автономные транспортные системы.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Авиационные технологии и автономные транспортные системы")
            
    with open("SRC\Биотехнология.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Биотехнология")

    with open("SRC\Биофизика и биоинформатика.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Биофизика и биоинформатика")

    with open("SRC\Геокосмические науки и технологии.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Геокосмические науки и технологии")
            
    with open("SRC\Компьютерные технологии и вычислительная техника.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Компьютерные технологии и вычислительная техника")
            
    with open("SRC\Математическое моделирование и компьютерные технологии.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Математическое моделирование и компьютерные технологии")
            
    with open("SRC\Общая и прикладная физика.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Общая и прикладная физика")
            
    with open("SRC\Прикладная математика и информатика.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Прикладная математика и информатика")
            
    with open("SRC\Природоподобные.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Природоподобные")
            
    with open("SRC\Программная инженерия и компьютерные технологии.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Программная инженерия и компьютерные технологии")
            
    with open("SRC\Программная инженерия.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Программная инженерия")
        
    with open("SRC\Радиотехника и компьютерные технологии.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Радиотехника и компьютерные технологии")
            
    with open("SRC\Системное программирование и прикладная математика.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Системное программирование и прикладная математика")
            
    with open("SRC\Техническая физика.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Техническая физика")
            
    with open("SRC\Физика перспективных технологий.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Физика перспективных технологий")
            
    with open("SRC\Экономика и ERP системы.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Экономика и ERP системы")
            
    with open("SRC\Электроника и наноэлектроника.json") as file:
        file = json.load(file)
        add_in_applicants(file, "Электроника и наноэлектроника")
create_all_applicants()

check_seat = applicants.copy()

#рейтинговый список по направлениям формата {direction : [[snils, priority, score]]}
direction_rate_list = {
    "aviatech" : [] ,
    "biotech" : [] ,
    "biophys" : [] ,
    "geospace" : [] ,
    "pc_tech" : [] ,
    "mathmatical" : [] ,
    "applied_phys" : [] ,
    "applied_math" : [] ,
    "natural_like" : [] ,
    "soft_engin_pc_tech" : [] ,
    "soft_engin" : [] ,
    "radion_engin" : [] ,
    "sys_prog" : [] ,
    "phys_tech" : [] ,
    "phys_tech_promising" : [] ,
    "economics" : [] ,
    "nanoelect" : [] ,
}

#добавление приоритета абитуриента в direction_rate_list формата [snils, priority, score]
def add_in_directions_rate_list(direction : str, applicate_data : list):
    if "Авиационные технологии и автономные транспортные системы" == direction: direction_rate_list["aviatech"].append(applicate_data)
    if "Биотехнология" == direction: direction_rate_list["biotech"].append(applicate_data)
    if "Биофизика и биоинформатика" == direction: direction_rate_list["biophys"].append(applicate_data)
    if "Геокосмические науки и технологии" == direction: direction_rate_list["geospace"].append(applicate_data)
    if "Компьютерные технологии и вычислительная техника" == direction: direction_rate_list["pc_tech"].append(applicate_data)
    if "Математическое моделирование и компьютерные технологии" == direction: direction_rate_list["mathmatical"].append(applicate_data)
    if "Общая и прикладная физика" == direction: direction_rate_list["applied_phys"].append(applicate_data)
    if "Прикладная математика и информатика" == direction: direction_rate_list["applied_math"].append(applicate_data)
    if "Природоподобные" == direction: direction_rate_list["natural_like"].append(applicate_data)
    if "Программная инженерия и компьютерные технологии" == direction: direction_rate_list["soft_engin_pc_tech"].append(applicate_data)
    if "Программная инженерия" == direction: direction_rate_list["soft_engin"].append(applicate_data)
    if "Радиотехника и компьютерные технологии" == direction: direction_rate_list["radion_engin"].append(applicate_data)
    if "Системное программирование и прикладная математика" == direction: direction_rate_list["sys_prog"].append(applicate_data)
    if "Техническая физика" == direction: direction_rate_list["phys_tech"].append(applicate_data)
    if "Физика перспективных технологий" == direction: direction_rate_list["phys_tech_promising"].append(applicate_data)
    if "Экономика и ERP системы" == direction: direction_rate_list["economics"].append(applicate_data)
    if "Электроника и наноэлектроника" == direction: direction_rate_list["nanoelect"].append(applicate_data)

#запись снилсов выпавших абитуриентов
dropped_out_applicants = list()

#сортировка направлений по баллам direction_rate_list и добавление снилсов выпавших в dropped_out_list
def sort_directions_rate_list():
    global dropped_out_applicants
    for i in directions_translator:
        direction_rate_list[directions_translator[i]].sort(key=lambda data: data[2], reverse=True)
        count_members = number_of_seats[i]
        drop_applicants = direction_rate_list[directions_translator[i]][count_members:].copy()
        if len(drop_applicants) != 0:
            drop_applicants = list(map(lambda x: x[0], drop_applicants))
            dropped_out_applicants += drop_applicants
        direction_rate_list[directions_translator[i]] = direction_rate_list[directions_translator[i]][:count_members]

def check_applicant_in_directions_rate_list(snils : str) -> bool:
    if snils not in applicants:
        return True
    data_applicant = check_seat[snils]
    for priority in data_applicant:
        score = data_applicant[priority]
        data = [snils, priority, score]
        for direction in direction_rate_list:
            if data in direction_rate_list[direction]:
                return True
    return False

# добавление 1 минимальный приоритет
def add_min_priority_applicant_in_direction_rate():
    for snils in applicants.copy():
        if check_applicant_in_directions_rate_list(snils):
            continue
        priority = min(applicants[snils])
        direction = applicants[snils][priority][0]
        score = applicants[snils][priority][1]
        data = [snils, priority, score]
        add_in_directions_rate_list(direction, data)
        del applicants[snils][priority]        
        if len(applicants[snils]) == 0:
            del applicants[snils]
        sort_directions_rate_list()

#добавляет остальные приоритеты до того пока все снилсы в dropped_out_applicants не будут содержаться в applicants
def add_rest_priorities_applicant_in_direction_rate():
    global dropped_out_applicants
    while True:
        k = 0
        for snils in dropped_out_applicants:
            if snils not in applicants:
                k += 1
                continue
            if check_applicant_in_directions_rate_list(snils):
                continue
            priority = min(applicants[snils])
            direction = applicants[snils][priority][0]
            score = applicants[snils][priority][1]
            data = [snils, priority, score]
            add_in_directions_rate_list(direction, data)
        dropped_out_applicants = list()
        sort_directions_rate_list
        if k == len(dropped_out_applicants):
            break

#делает рейтинговые списки
while len(applicants) != 0:
    add_min_priority_applicant_in_direction_rate()
    add_rest_priorities_applicant_in_direction_rate()
    sort_directions_rate_list()

#Записывает в файлы с названием direction.csv из direction_rate_list
def write_to_file():
    for direction in direction_rate_list:
        with open(f"Rate_lists\{direction}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Позиция", "Снилс", "Приоритет", "Баллы"])
            position = 0
            for data in direction_rate_list[direction]:
                position += 1
                writer.writerow([position] + data)
write_to_file()