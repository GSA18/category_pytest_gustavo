import sys
sys.path.append('.')
from models.base_model import BaseModel
from models.category import Category

name = 'Category'
description = 'Description'

category = Category(name, description)


def test_compare_column_model():
    assert category.name == name
    assert category.description == description


def test_compare_type_column_model():
    assert type(category.name) == str
    assert type(category.description) == str


def test_compare_isinstance():
    assert isinstance(category, BaseModel)
    assert isinstance(category, Category)


def test_has_attribute():
    assert hasattr(category, 'name')
    assert hasattr(category, 'description')

def test_validate_name():
    try:
        Category(None, 'Eletronicos')
    except Exception as e:
        assert isinstance(e, ValueError)

def test_validate_name2():
    try:
        Category(' ', 'Eletronicos')
    except Exception as e:
        assert isinstance(e, ValueError)        


def test_validate_description():
    try:
        Category('Moveis', '     ')
    except Exception as e:
        assert isinstance(e, ValueError)

def test_validate_description2():
    try:
        Category('Moveis', None)
    except Exception as e:
        assert isinstance(e, ValueError)        