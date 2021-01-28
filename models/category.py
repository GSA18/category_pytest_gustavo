import sys
sys.path.append('.')
from sqlalchemy import Column, String
from models.base_model import BaseModel
from sqlalchemy.orm import validates


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column(String(length=150))
    description = Column(String(length=200))

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if name is None:
            raise ValueError("Please, write a name!")
        elif name.strip(' ') == '':
            raise ValueError("Name can't be null!")
        return name

    @validates('description')
    def validate_description(self, key, description):
        if description is None:
            raise ValueError("Please, write a description!")
        elif description.strip(' ') == '':
            raise ValueError("Description can't be null!")
        return description
