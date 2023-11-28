from datetime import date
import file_manager.menu_mod

wallet = 5000.0
shopping_book = []


def curent_date():  # текущая дата
    current_date = str(date.fromisoformat('2019-01-01').today())
    return current_date


def adding_wallet_func():  # пополнение счёта
    global wallet
    add_money = input('Введите сумму пополнения в рублях: ')
    while add_money.isdigit() != True:
        print('Некоректный ввод! Повторите попытку.')
        return adding_wallet_func()
    wallet += float(add_money)
    print(f'Пополнение на сумму {float(add_money)} руб. выполнено успешно.')
    return score_func()


def buy_func():  # Покупка
    global wallet
    purchase_sum = input('Введите сумму покупки в рублях: ')
    while purchase_sum.isdigit() != True:
        print('Некоректный ввод! Повторите попытку.')
        return buy_func()
    if float(purchase_sum) > wallet:
        print('Недостаточно средств!')
        score_func()
    elif float(purchase_sum) <= 0:
        print('Сумма не может быть равна нулю!')
        score_func()
    else:
        purchase_name = input('Введите название покупки: ')
        wallet -= float(purchase_sum)
        history_func(purchase_name, purchase_sum)
        return score_func()


def history_func(purchase_name, purchase_sum):  # история покупок
    global shopping_book
    current_purchase = [curent_date(), purchase_name, purchase_sum]
    shopping_book.append(current_purchase)
    return shopping_book


def score_func():  # главное меню
    while True:
        print(f'Текущий баланс: {wallet} руб.')
        print(f'1. пополнение счета.')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            adding_wallet_func()
        elif choice == '2':
            buy_func()
        elif choice == '3':
            if shopping_book == []:
                print('История пуста...')
            print('Дата.....................Сумма..............Наименование операции')
            for i in range(len(shopping_book)):
                print(f'{shopping_book[i][0]}...............{shopping_book[i][2]}...............{shopping_book[i][1]}')
            score_func()
        elif choice == '4':
            file_manager.menu_mod.main_menu_print()
            return file_manager.menu_mod.main_menu_input()
        else:
            print('Неверный пункт меню')
