import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


target = f"mysql+pymysql://\
{config.config.database['user']}:{config.config.database['password']}@\
{config.config.database['host']}:{config.config.database['port']}/{config.config.database['db']}\
?charset=utf8"
engine = create_engine(target, max_overflow=5)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
