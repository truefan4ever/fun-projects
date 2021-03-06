"""
Необходимо написать клиент к API VK , который будет считать
распределение возрастов друзей для указанного пользователя.
То есть на вход подается username или user_id пользователя,
на выходе получаем список пар (<возраст>, <количество друзей
с таким возрастом>), отсортированный по убыванию по второму
ключу (количество друзей) и по возрастанию по первому ключу (возраст)
"""

import requests
import re
import datetime
from operator import itemgetter
from tokens import TOKEN


def calc_age(uid):
    """
    This function gets data from api.vk.com about user and returns
    the sorted array of tuples with ages and amounts of them.
    """
    current_year = datetime.date.today().year
    list_of_dates = []
    list_of_years = []
    list_of_ages = []
    list_of_ages_sorted = []
<<<<<<< HEAD
    base_url = "https://api.vk.com/method"
    req_1 = requests.get(f"{base_url}/users.get?user_ids={uid}&access_token={TOKEN}&v=5.89")
=======

    base_url = "https://api.vk.com/method"
    req_1 = requests.get(
        f"{base_url}/users.get?user_ids={uid}&access_token={TOKEN}&v=5.89")
>>>>>>> e28e676ff043bd0a35cc765668badc6edfedfe96

    for response_value in req_1.json().values():
        for items in response_value:
            for item in items.keys():
                if item == 'id':
                    user_id = items[item]
                elif item == 'is_closed':
                    user_is_closed = items[item]

    if user_is_closed is False:
<<<<<<< HEAD
        req_2 = requests.get(f"{base_url}/friends.get?user_id={user_id}&access_token={TOKEN}&fields=bdate&v=5.80")
=======
        req_2 = requests.get(
            f"{base_url}/friends.get?user_id={user_id}&access_token={TOKEN}&fields=bdate&v=5.80")
>>>>>>> e28e676ff043bd0a35cc765668badc6edfedfe96
        for response_value in req_2.json().values():
            for key in response_value.keys():
                if key == 'items':
                    value = response_value[key]
                    for element in value:
                        # print(element)
                        for key in element.keys():
                            if key == 'bdate':
                                date_string = element[key]
                                list_of_dates.append(date_string)

        for date in list_of_dates:
            result = re.findall(r'\d{1,2}.\d{1,2}.(\d{4})', date)
            if result:
                list_of_years.append(result[0])

        for element in list_of_years:
            age = int(current_year) - int(element)
            list_of_ages.append(age)
            sorted_dict = {}.fromkeys(list_of_ages, 0)

        for age in list_of_ages:
            sorted_dict[age] += 1

        for key, value in sorted_dict.items():
            tup = (key, value)
            list_of_ages_sorted.append(tup)

        sort_1 = sorted(list_of_ages_sorted, key=itemgetter(0))

        sort_2 = sorted(sort_1, key=itemgetter(1), reverse=True)

        return sort_2
    else:
        err_text = 'Oh, we are sorry. This profile is closed. Enter another profile.'
        return err_text


if __name__ == '__main__':
    res = calc_age('s.nemogai')
    print(res)
