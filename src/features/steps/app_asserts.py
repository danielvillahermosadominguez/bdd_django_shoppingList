import app_utils
def assert_equal(expected_result, shopping_list):
    res_dic = app_utils.create_dictionary(expected_result)
    for key in res_dic:
        _assert_contain(shopping_list, key, res_dic[key])

def _assert_contain(shopping_list, item, quantity):
    value = -1
    size = shopping_list.size()
    for index in range(0, size):
        item_sl = shopping_list.get_item_description(index)
        if(item_sl == item):
            value = shopping_list.get_item_quantity(index)
            break
    assert(int(quantity) == value)
