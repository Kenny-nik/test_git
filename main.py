from src.utils import get_data_from_json
from src.processing import filter_by_state, sort_by_date
from src.operations import search_by_pattern
from src.read_from_file import read_from_csv, read_from_excel
from src.widget import mask_account_card, get_date
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
transactions_csv = BASE_DIR / 'data' / 'transactions_csv.csv'
transactions_xlsx = BASE_DIR / 'data' / 'transactions_excel.xlsx'
transactions_json = BASE_DIR / "data" / "operations.json"

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    if choice not in ["1", "2", "3"]:
        print("Неверный ввод. Пожалуйста, выберите пункт 1, 2 или 3.")
        return

    if choice == "1":
        operations = get_data_from_json(transactions_json)
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        operations = read_from_csv(transactions_csv)
        print("Для обработки выбран CSV-файл.")
    else:
        operations = read_from_excel(transactions_xlsx)
        print("Для обработки выбран XLSX-файл.")

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input("Пользователь: ").strip()
        if status.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции \"{status}\" недоступен.")
            continue
        break

    print(f"Операции отфильтрованы по статусу \"{status.upper()}\"")
    filtered_operations = filter_by_state(operations, status)

    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_choice == "да":
        order_choice = input("Отсортировать по возрастанию или по убыванию? \nПользователь: ").strip().lower()
        if order_choice == "по возрастанию":
            filtered_operations = sort_by_date(filtered_operations,  is_reverse=False)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if currency_choice == "да":
        new_list_sort = []
        for i in filtered_operations:
            if i["operationAmount"]["currency"]["code"] == "RUB":
                new_list_sort.append(i)
    else:
        new_list_sort = filtered_operations

    description_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").strip().lower()
    if description_filter == "да":
        question_description_word = input("Введите слово: ")
        finally_filter = search_by_pattern(new_list_sort, question_description_word)
    else:
        finally_filter = new_list_sort

    if finally_filter:
        print("Программа: Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(finally_filter)}\n")
        for transaction in finally_filter:
            date = get_date(transaction.get("date"))
            description = transaction.get("description")
            mask_to = mask_account_card(transaction.get("to"))
            amount = transaction.get("operationAmount")["amount"]

            if description == "Открытие вклада":
                print(f"{date} {description}")
                print(mask_to)
                print(f"Сумма: {amount}\n")
            else:
                mask_from = mask_account_card(transaction.get("from", "Нет данных"))
                print(f"{date} {description}")
                print(f"{mask_to} -> {mask_from}")
                print(f"Сумма: {amount}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

if __name__ == "__main__":
    main()