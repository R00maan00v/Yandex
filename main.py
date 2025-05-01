'''Функция из задачи'''
def parse(response: dict) -> list[str]:

people_data = response.get('people', {}) '''Проверка наличия people в запросе'''

results = people_data.get('result', []) '''Извлечение списка со страницы'''

logins = [person['login'] for person in results if 'login' in person] '''Сборка всех логинов в список'''

return logins


'''Функция парсинга только людей'''
def parse(response: dict) -> list[str]:

    '''Функция для фильтра роботов'''
    def filter_robots(logins: list[str]) -> list[str]:
        return [login for login in logins if "robot" not in login.lower()]

    people_data = response.get("people", {})
    results = people_data.get("result", [])
    logins = [person["login"] for person in results if "login" in person]

    return filter_robots(logins)