import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Database1 import Base, engine
from auth.models import User

Base.metadata.create_all(bind=engine)
print("Tables created.")
