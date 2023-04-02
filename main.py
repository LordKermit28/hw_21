from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import RequestError, LogisticError

store = Store(
    items={
        "cookies": 25,
        "vegetables": 20,
        "limonad": 21,
    }
)

shop = Shop(
    items={
        "cookies": 2,
        "vegetables": 2,
        "limonad": 1,
    }
)

storages = {
    'shop': shop,
    'store': store,
}


def main ():
    print('\nGood afternon!\n')

    while True:
        for storage_name in storages:
            print(f'Now in {storage_name}:\n {storages[storage_name].get_items()}')

        user_input = input(
            'print query in format "delivery 3 cookies in shop":\n'
            'Print "stop" if you wanna stop:\n'
        )
        if user_input in ('stop'):
            break

        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue

        try:
            storages[request.departure].remove(request.product, request.amount)
            print(f'Courier has taken {request.amount} {request.product} from {request.departure}')
        except LogisticError as error:
            print(error.message)
            continue

        try:
            storages[request.destination].add(request.product, request.amount)
            print(f'Courier has delivered {request.amount} {request.product} to {request.destination}')
        except LogisticError as error:
            print(error.message)
            storages[request.departure].add(request.product, request.amount)
            print(f'Courier back {request.amount} {request.product} to {request.departure}')
            continue

if __name__ == '__main__':
    main()


