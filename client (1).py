import requests

BASE_URL = "http://0.0.0.0:5000"

def main_menu():
    print("\n=== API Client ===")
    print("1. Отримати список користувачів")
    print("2. Отримати інформацію про користувача за ID")
    print("3. Отримати список тренувань")
    print("4. Додати нове тренування")
    print("5. Вийти")
    return input("Оберіть опцію: ")

def get_users():
    response = requests.get(f"{BASE_URL}/users")
    if response.status_code == 200:
        print("Список користувачів:")
        print(response.json())
    else:
        print("Помилка отримання користувачів:", response.status_code)

def get_user():
    user_id = input("Введіть ID користувача: ")
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        print(f"Деталі користувача {user_id}:")
        print(response.json())
    else:
        print(f"Користувач з ID {user_id} не знайдений. Статус:", response.status_code)

def get_workouts():
    response = requests.get(f"{BASE_URL}/workouts")
    if response.status_code == 200:
        print("Список тренувань:")
        print(response.json())
    else:
        print("Помилка отримання тренувань:", response.status_code)

def add_workout():
    try:
        user_id = int(input("Введіть ID користувача: "))
        workout_type = input("Введіть тип тренування (наприклад, Cardio): ")
        duration = int(input("Введіть тривалість тренування (хвилини): "))
        date = input("Введіть дату тренування (YYYY-MM-DD): ")

        data = {
            "user_id": user_id,
            "type": workout_type,
            "duration": duration,
            "date": date
        }

        response = requests.post(f"{BASE_URL}/workouts", json=data)
        if response.status_code == 201:
            print("Тренування успішно додано:")
            print(response.json())
        else:
            print("Помилка додавання тренування:", response.status_code)
    except ValueError:
        print("Некоректний ввід даних. Спробуйте ще раз.")

if __name__ == "__main__":
    while True:
        option = main_menu()
        if option == "1":
            get_users()
        elif option == "2":
            get_user()
        elif option == "3":
            get_workouts()
        elif option == "4":
            add_workout()
        elif option == "5":
            print("Вихід із програми.")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")