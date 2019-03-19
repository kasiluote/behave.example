def return_counter(test_dict,text):
    # counter = 0
    # for t in test_dict.values():
    #     if t == text:
    #         counter +=1
    counter = len([ res for res in test_dict.values() if res == text])
    return counter

from behave   import given, when, then
from hamcrest import assert_that, has_items
from hamcrest.library.collection.issequence_containinginanyorder \
    import contains_inanyorder

@then('we will have the following people in "{department}"')
def step_impl(context,department):
    expected_persons = [ row["name"] for row in context.table ]
    actual_persons = context.res.values()

    assert_that(contains_inanyorder(*expected_persons),actual_persons)


@then('we will have at least the following people in "{department}"')
def step_impl(context, department):
    expected_persons = [row["name"] for row in context.table]
    actual_persons = context.res.values()

    assert_that(contains_inanyorder(*expected_persons), actual_persons)