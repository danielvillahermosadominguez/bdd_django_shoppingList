import unittest
import pytest
from .prueba import Utils, BDREurope, CSV,  Xlsm, ParseMock
class SlideStub (SlidePresenter):
     def process_slide(self):
         print("soy otro")


class ShoppingListServiceTest(unittest.TestCase):

    def test_generate_ppt (self):
        #Arrange
        dictionary = {1, SlideStub(), 2, SlideStub()}
        sut = SlideLoader(dictionary)
        #Act
        sut.generate()
        
        #Assert

       # self.assertEqual(result, expected)
       # self.assertEqual(1, pa.counter)

    def test_fail_if_file_not_exit(self)