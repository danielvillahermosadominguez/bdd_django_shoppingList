import os

from steps.utils import remove_folder, run_server, kill, remove_folder
from behave import fixture, use_fixture
from behave.fixture import use_fixture_by_tag
from shoppinglistapi.shoppinglist.application.shoppinglist_appserv import  ShoppingListAppServ
from shoppinglistapi.shoppinglist.infra.shoppinglistrepositoryFile import ShoppingListRepositoryFile

@fixture
def prepare_environment(context, timeout=30, **kwargs):
    context.process = run_server()
    yield context.process 
    kill(context.process.pid)

@fixture
def prepare_application(context, timeout=30, **kwargs):
    remove_folder(".\data")
    repository = ShoppingListRepositoryFile()
    context.application = ShoppingListAppServ(repository)
    yield context.application
    

fixture_registry = {
    "fixture.prepare.environment": prepare_environment,
}

def before_tag(context, tag):
    if(tag.startswith("fixture.prepare.environment")):
       use_fixture(prepare_environment, context)
    if(tag.startswith("fixture.prepare.application_layer")):
           use_fixture(prepare_application, context)
       # return use_fixture_by_tags(tag, context, fixture_registry)

#def before_all(context):
#def before_feature(context, feature):
    

def before_scenario(context, scenario):
     if 'Application' in scenario.tags:
         remove_folder(".\data")

#def after_all(context):
#def after_feature(context, feature):
#def after_scenario(context, scenario):
 