
def add_items(items, context):
    items_list = items.split(",")
    for item in items_list:
        context.application.add(item.strip(), context.user)
def change_items(items, context):
    changes_dic = create_dictionary(items)
    for item in changes_dic:
        context.application.change(item.strip(),changes_dic[item], context.user)

def remove_items(items, context):
    items_list = items.split(",")
    for item in items_list:
        context.application.delete(item.strip(), 1, context.user)

def create_dictionary(input):
    res_dic = dict(item.split(":") for item in input.split(","))
    return res_dic