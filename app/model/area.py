from sqlalchemy import Column, Integer, String
from util.orm import Base


# 创建单表
class Area(Base):
    __tablename__ = 'area'

    id = Column(Integer, primary_key=True)
    city_index = Column(String(64))
    area_index = Column(String(64))
    area_id = Column(String(128))
    insert = Column(Integer)

    def __init__(self, city_index, area_index, area_id=''):
        self.area_id = area_id
        self.city_index = city_index
        self.area_index = area_index
        self.insert = 0
