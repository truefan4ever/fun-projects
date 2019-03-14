import requests
import json
import re
import datetime
from operator import itemgetter


def calc_age(uid):
	"""This function gets data from api.vk.com about user and returns the sorted array of tuples with ages and amounts of them."""
	current_year = datetime.date.today().year
	list_of_dates = []
	list_of_years = []
	list_of_ages = []
	list_of_ages_sorted = []
	token = "609bb1ed609bb1ed609bb1ed9260f283a96609b609bb1ed3c1edb0380c6c1542ec50c5c"
	base_url = "https://api.vk.com/method"
	req_1 = requests.get(f"{base_url}/users.get?user_ids={uid}&access_token={token}&v=5.89")
 
	for response_value in req_1.json().values():
		for items in response_value:
			for item in items.keys():
				if item == 'id':
					user_id = items[item]
				elif item == 'is_closed':
					user_is_closed = items[item]

	if user_is_closed == False:
		req_2 = requests.get(f"{base_url}/friends.get?user_id={user_id}&access_token={token}&fields=bdate&v=5.80")
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
    res = calc_age('basta')
    print(res)
