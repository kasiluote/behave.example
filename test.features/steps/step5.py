from behave import when,then,given
from hamcrest import assert_that,equal_to
from forbulator import Forbulator

@given('a sample text loaded into the forbulator')
def step_impl(context):
    forbulator = getattr(context,"forbulator",None)
    if not forbulator:
        context.forbulator = Forbulator()
    context.forbulator.text = context.text

@when('we activate the forbulator')
def step_impl(context):
    context.forbulator.activate()

@then('we will find it similar to {language}')
def step_impl(context,language):
    assert_that(language,equal_to(context.forbulator.seems_like_language()))
