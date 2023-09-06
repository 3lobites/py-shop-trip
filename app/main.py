from customer import Customer, read_from_json
from shop import Shop
from car import get_directions


def shop_trip():
    # write your code here
    print("test")
    pass


if __name__ == "__main__":
    shop_trip()

#   -----------------TESTS------------------

#   тест данные из файла
test_customs = read_from_json("config.json", "customers")
test_shop = read_from_json("config.json", "shops")

#   тест объекты классов из данных
custom_list = []
shop_list = []
for _ in test_customs:
    custom_list.append(Customer.load_info_customer(_))
for _ in test_shop:
    shop_list.append(Shop.load_info_shop(_))

#   тест расстояния до магазинов каждого покупателя
test_direction = get_directions(custom_list, shop_list)

#   тест поиска нужных покупок
test_shopping = f"Customer {custom_list[0].name} visited shop {shop_list[0].name}"
test_right_products = custom_list[0].search_right_products(shop_list[0])

# ttt = read_from_json("config.json", "customers")
# mmm = read_from_json("config.json", "shops")
# rrr = read_from_json("config.json", "FUEL_PRICE")
# ddd = read_from_json("config.json", "FUEL_PRIC")
yyy = 0
