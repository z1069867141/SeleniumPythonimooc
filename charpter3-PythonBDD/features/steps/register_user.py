from behave import *
from features.lib.page.register_page import RegisterPage

use_step_matcher("re")

@When("I open the register website")
def step_register(context,url):
    RegisterPage(context).get_url(url)

@Then('I expect that the title is "([^"]*)"')
def step_register1(context,title_name):
    title = RegisterPage(context).get_title()
    assert title_name in title