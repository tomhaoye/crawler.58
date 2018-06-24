from util.orm import Base, engine
from .area import Area
from .community import Community

Base.metadata.create_all(engine)
