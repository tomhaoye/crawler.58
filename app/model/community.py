from sqlalchemy import Column, Integer, String, Text
from util.orm import Base


# 创建单表
class Community(Base):
    __tablename__ = 'community'

    id = Column(Integer, primary_key=True)
    listname = Column(String(255))
    city_index = Column(String(64))
    area_index = Column(String(64))
    infoid = Column(Integer)
    area_name = Column(String(128))
    address = Column(String(255))
    alias = Column(String(255))
    subway = Column(String(255))
    shangquan = Column(String(128))
    price = Column(Integer)
    completiontime = Column(String(128))
    detail_info = Column(Text)
    lat_lon = Column(String(128))

    def __init__(self, city_index, area_index, info):
        self.listname = info['infoParamEntity']['map']['listname']
        self.city_index = city_index
        self.area_index = area_index
        self.infoid = info['infoid']
        self.area_name = info['areaName']
        self.address = info['address']
        self.alias = info['alias']
        self.subway = info['infoParamEntity']['map']['subway']
        self.shangquan = info['shangquanName']
        self.price = info['price']
        self.completiontime = info['infoParamEntity']['map']['completiontime']
