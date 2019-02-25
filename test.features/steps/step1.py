from behave import given,when,then

@given('First test with behave here')
def step_impl(context):
    pass

@when('Config test')
def step_impl(context):
    assert 1 == 1


@then('Test pass or fail.')
def step_impl(context):
    assert "Yes" != "No"
