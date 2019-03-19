from behave import given,then,when
from hamcrest import equal_to,assert_that


def return_counter(test_dict,text):
    # counter = 0
    # for t in test_dict.values():
    #     if t == text:
    #         counter +=1
    counter = len([ res for res in test_dict.values() if res == text])
    return counter


@given('a set of specific users')
def step_impl(context):
    # context.x = {}
    # for row in context.table:
    #     context.x[row["name"]]=row["department"]
    context.res = {row["name"] : row["department"] for row in context.table}

@when('we count the number of people in each department')
def step_impl(context):
    pass

@then('we will find {count} people in "{department}"')
def step_impl(context,count,department):
    count = int(count)
    result = return_counter(context.res,department)
    assert_that(result,equal_to(count))

@then('we will find {count} person in "{department}"')
def step_impl(context,count,department):
    count = int(count)
    result = return_counter(context.res, department)
    assert_that(result,equal_to(count))
