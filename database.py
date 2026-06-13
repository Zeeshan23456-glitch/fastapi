from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

Database_url = "mysql+pymysql://root:password@localhost/my_db"

engine = create_engine(Database_url)

sessionlocal = sessionmaker(
    autoflush=False,      
    autocommit= False,  # change are not save automatically
    bind=engine    # connection to the database
)

base = declarative_base()

def get_db():
    db = sessionlocal()     # open the database session
    try:
        yield db  # passes the session to the route
    finally:
        db.close()  # closes the session after the request is finished.