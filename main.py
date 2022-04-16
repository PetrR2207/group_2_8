from good_info import Good, Goods
if __name__  == '__main__':
    file_name = input('Введите путь к файлу:')
    goods = Goods()
    goods.get_from_file(file_name)
    print(goods)

# def get_goods_from_file(file_name: str) -> list[str]:
#     with open(file_name, 'r', encoding='utf-8') as data_file:
#         result = data_file.readlines()
#
#         return re
#
#
# goods_list = get_goods_from_file('goods.txt')
#
#
# def get_goods_info(goods_list: list) -> dict:
#     """Gets info about goods from list.
#
#
#     :param goods_list (list: List of goods
#     :return: dict: Goods info in dictionary
#     """
#     result = {}
#     expensive_goods = set()
#     min_price = float('inf')
#     max_price = 0
#     goods_count = 0
#     price_sun = 0
#
#     for good in goods_list:
#         item = good.replace('\n', '').split(':')
#         item_price = int(item[1])
#         price_sun += item_price
#         if item_price < min_price:
#             min_price = item_price
#         elif item_price > max_price:
#             max_price = item_price
#         if item_price > 100:
#             expensive_goods.add(item[0])
#         goods_count +=1
#
#     nean_price = round(price_sun / goods_count, 2)
#
#     result['min_price'] = min_price
#     result['max_price'] = max_price
#     result['nean_price'] = nean_price
#     result['goods_count'] = goods_count
#     result['expensive_goods'] = expensive_goods
#
#     return result
#
# def print_goods_info(goods_list):
#
#     goods_dict = get_goods_info(goods_list)
#     expensive_goods = '\n'.join(list(goods_dict['expensive_goods']))
#
#     print(f'Максимальная цена товара: {goods_dict["max_price"]}',
#           f'Максимальная цена товара: {goods_dict["min_price"]}',
#           f'Средняя цена товара: {goods_dict["nean_price"]}',
#           f'Количество товаров: {goods_dict["nean_price"]}',
#           f'Дорогие товары:\n{expensive_goods}',
#           sep='\n'
#           )
# print_goods_info(goods_list)