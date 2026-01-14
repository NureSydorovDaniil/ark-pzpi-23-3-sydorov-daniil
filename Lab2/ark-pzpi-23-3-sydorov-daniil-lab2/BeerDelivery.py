from crud import create_user, get_all_users, create_beer, get_all_beers

user = create_user("Иван Иванов", "123456789", "ivan@mail.com", "password123")
print(f"Создан пользователь: {user.user_id}, {user.name}")

users = get_all_users()
print("Список пользователей:")
for u in users:
    print(u.user_id, u.name, u.email)

beer = create_beer("Светлое пиво", "Lager", 120.0)
print(f"Создано пиво: {beer.beer_id}, {beer.name}, {beer.price}")

beers = get_all_beers()
print("Список пив:")
for b in beers:
    print(b.beer_id, b.name, b.type, b.price)
