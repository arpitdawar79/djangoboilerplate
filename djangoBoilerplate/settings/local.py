from .base import Base

class Local(Base):
  DEBUG = True
  SECRET_KEY = 'SOME_SECRET_KEY'
