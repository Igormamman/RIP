from behave import *
from patterns import Bridge, Fabric_Method, iterator

@given('1st year student using API 1')
def step_impl(context):
    first_year_creator = Fabric_Method.First_Year_Creator(Fabric_Method.Bridge.First_Year_API_1)
    context.stud = first_year_creator.create_student()

@when('we try to get marks of student')
def step_impl(context):
    context.a=context.stud.get_marks()

@then('we will get their marks in range 5...20')
def step_impl(context):
    assert 0<context.a<25

@given('1st year student using API 2')
def step_impl(context):
    first_year_creator = Fabric_Method.First_Year_Creator(Fabric_Method.Bridge.First_Year_API_2)
    context.stud = first_year_creator.create_student()

@then('we will get their marks in range 0...5')
def step_impl(context):
    assert 0<context.a<5
