from person import person

import json

def load_SashaTheory_data(folder):
    # Загрузка имен Саши из папки с данными
    with open(folder + '/names.json', 'r', encoding='utf-8') as file:
        SashaTheory_names = json.load(file)

    # Загрузка внешности Саши из папки с данными
    with open(folder + '/appearance.txt', 'r', encoding='utf-8') as file:
        SashaTheory_appearance = file.read()

    # Загрузка интересов Саши из папки с данными
    with open(folder + '/interests.json', 'r', encoding='utf-8') as file:
        SashaTheory_interests = json.load(file)

    # Загрузка локации Саши из папки с данными
    with open(folder + '/location.json', 'r', encoding='utf-8') as file:
        SashaTheory_location = json.load(file)

    # Загрузка биографии Саши из папки с данными
    with open(folder + '/biography.json', 'r', encoding='utf-8') as file:
        SashaTheory_biography = json.load(file)

    # Загрузка системы принятия решений Саши из папки с данными
    with open(folder + '/volition.json', 'r', encoding='utf-8') as file:
        SashaTheory_volition = json.load(file)

    # Загрузка активностей Саши из папки с данными
    with open(folder + '/activities.json', 'r', encoding='utf-8') as file:
        SashaTheory_activities = json.load(file)

    return SashaTheory_names, SashaTheory_appearance, SashaTheory_interests, SashaTheory_biography, SashaTheory_volition, SashaTheory_activities, SashaTheory_location


if __name__ == '__main__':

    # Загрузка данных Саши
    folder = 'SashaTheory_data'
    (SashaTheory_names,
     SashaTheory_appearance,
     SashaTheory_interests,
     SashaTheory_biography,
     SashaTheory_volition,
     SashaTheory_activities,
     SashaTheory_location) = load_SashaTheory_data(folder)

    # Создание персонажа
    SashaTheory = person.Person(SashaTheory_names,
                                SashaTheory_appearance,
                                SashaTheory_interests,
                                SashaTheory_biography,
                                SashaTheory_activities,
                                SashaTheory_volition,
                                SashaTheory_location)

    # Запуск главного жизненного цикла
    delay = 1
    SashaTheory.live(delay)
