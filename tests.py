import json
from config import filename


def read_file():
    print("[INFO] Получили список вопросов для теста")
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data

