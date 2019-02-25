from behave import given,when,then
from blender import Blender
from hamcrest import assert_that, equal_to


@given('I put {thing} in a blender')
def step_impl(context,thing):
    context.blender = Blender()
    context.blender.add(thing)


@when('I switch the blender on')
def step_impl(context):
    context.blender.switch_on()


@then('it should transform into {other_thing}')
def step_impl(context,other_thing):
    assert_that(context.blender.result,equal_to(other_thing))
