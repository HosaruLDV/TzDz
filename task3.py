from datetime import datetime
import operator

FILE = 'operations.json'
EXECUTED_STATE = 'EXECUTED'


def getPaymentType(payment: str):
    if 'счет' in payment.lower():
        return f'{payment[:5]}**{payment[-2:]}'
    else:
        payment_type = f'{payment.split()[len(payment.split()) - 1]}'
        card_type = f'{payment.replace(f" {payment_type}", "")}'
        payment_type = payment_type[:-10] + '** **** ' + payment_type[12:]
        payment_type = f'{card_type} {payment_type[:4]} {payment_type[4:]}'
        return payment_type


def parse(res):
    count = 0
    for i in res:
        if count == 5:
            return
        if len(i) > 0 and i['state'] == EXECUTED_STATE:

            datetime_str = i['date'].split('T')[0]
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d').date().strftime('%d.%m.%Y')
            cost = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'
            print(f'{datetime_object} {i["description"]}')
            if 'открытие' in i['description'].lower():
                print(f'{getPaymentType(i["to"])}')
            else:
                print(f'{getPaymentType(i["from"])} -> {getPaymentType(i["to"])}')
            print(cost)
            print()
            count += 1


try:
    res = list()
    with open(FILE, 'r', encoding='utf-8' ) as fd:
        res = list(eval(fd.read()))
        fd.close()
    tmp = [date for date in res if 'date' in date]
    tmp.sort(key=operator.itemgetter('date'), reverse=True)
    parse(tmp)
except Exception as _ex:
    print(f'Error: {_ex}')
