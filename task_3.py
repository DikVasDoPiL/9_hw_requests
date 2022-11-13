from requests import get
from datetime import date
from datetime import timedelta

def get_question(days, tag='python', site='stackoverflow', sort='creation'):
    fromdate = (date.today() - timedelta(days=days)).strftime('%Y-%m-%d')
    url = f'https://api.stackexchange.com/2.3/questions?fromdate={fromdate}&sort={sort}&tagged={tag}&site={site}'
    req = get(url).json()
    result = req['items']

    return result

py_quests = get_question(1) #Выбран интервал за сегодня и еще один день

#Для проверки вывожу самый старый вопрос
print(py_quests[0]['owner']['display_name'])
print(py_quests[0]['title'])
print(py_quests[0]['link'])


