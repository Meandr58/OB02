# Создание базового класса:
class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    # Получение информации (Getters)
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Изменение информации (Setters)
    def set_name(self, name):
        self.__name = name


# Создание дочернего класса
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__admin_access_level = 'admin'

    def get_admin_access_level(self):
        return self.__admin_access_level

    # Метод для добавления пользователя в систему
    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен в систему.")
        else:
            print("Ошибка: Объект не является экземпляром класса User.")

    # Метод для удаления пользователя из системы
    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален из системы.")
                return
        print("Ошибка: Пользователь с таким ID не найден.")

# Тестирование системы управления учетными записями пользователей

# Создание списка пользователей
user_list = []

# Создание обычных пользователей
user1 = User(1, "Василий Теркин")
user2 = User(2, "Максим Горький")

# Добавление пользователей в список
user_list.append(user1)
user_list.append(user2)

# Создание администратора
admin = Admin(3, "Виолетта Мармеладова")

# Администратор добавляет нового пользователя
new_user = User(4, "Антон Чехов")
admin.add_user(user_list, new_user)

# Администратор удаляет пользователя
admin.remove_user(user_list, 2)

