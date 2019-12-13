from re import finditer
def get_password():

    list_of_passwords = []

    for number in range(245182, 790572):
        number = str(number)

        if check_for_ddd(number) is True & check_increase_number(number) is True:
            list_of_passwords.append(number)

    return len(list_of_passwords)


def check_for_dd(number):
    if len(set(number)) == len(number):
        return False
    return True


def check_for_ddd(number):
    matches = []
    for match in finditer(r'(\d)\1+', number):
        matches.append(match.group(0))
    return any(len(match) == 2 for match in matches)


def check_increase_number(number):
    number = [int(d) for d in number]
    res = all(i <= j for i, j in zip(number, number[1:]))
    if res:
        return True
    return False


print(get_password())
