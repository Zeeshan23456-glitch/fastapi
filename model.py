from sqlalchemy import column, String ,Integer
from database import base

class user(base):
    __tablename__ = "users"

    id= column(Integer,primary_key = True)
    name= column(String(50))
    email= column(String(50),unique = True)
    address = column(String(100))