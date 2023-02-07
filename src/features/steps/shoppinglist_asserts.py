from http import HTTPStatus

def assert_not_correct_format(response):
    assert(response.status_code == HTTPStatus.NOT_FOUND)

def assert_is_equal(result, table):
    for row in table:
        item = row['Item']
        quantity = row['Quantity']
        assert(item in result)
        assert(int(quantity) == result[item])

def assert_ok(response):
    assert(response.status_code == HTTPStatus.OK.value)

def assert_there_is_nothing_to_delete(response):
    assert(response.status_code == HTTPStatus.NOT_ACCEPTABLE.value)
    
def assert_the_name_not_exist(response):
    assert(response.status_code == HTTPStatus.NO_CONTENT)
