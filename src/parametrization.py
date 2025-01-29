from const import Country, TAX_RATES, ROLES, ROLE_NAMES, ERR_MES

def select_country():
    print('Enter a country number:')
    [print(f'{i} - {c.name}') for i, c in enumerate(Country)]
    num = 0
    try:
        num = int(input())
    except:
        print(ERR_MES)
        select_country()
    if num > len(Country)-1:
        print('No such country number')
        select_country()
    countries = tuple(Country)
    return countries[num], countries[num].value

def select_roles():
    print('Enter numbers of preferred professions using a separator (dot, comma or gap) or just press Enter to select all ones:')
    selected_nums = set()
    for i, r in enumerate(ROLE_NAMES):
        selected_nums.add(i)
        print(f'{str(i)} - {r}')
    nums = input()
    if nums == "": 
        return selected_nums
    else:
        try:
            selected_nums = set(map(int, nums.split(''.join(s for s in [',','.',' '] if s in nums))))
        except:
            print(ERR_MES)
            select_roles()
        for num in selected_nums:
            if num > len(ROLES)-1:
                print(f'No such profession number - {num}')
                select_roles()
        return selected_nums

def get_net_rate(country):
    return 1-TAX_RATES[country]

def get_currency_rates():
    try:
        return int(input('Enter the current USD rate for correct salary calculation: ')), int(input('Enter the current EUR rate: '))
    except:
        print(ERR_MES)
        get_currency_rates()