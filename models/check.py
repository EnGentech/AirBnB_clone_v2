from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

url = "mysql+mysqldb://root:admin8634@localhost/my_db"

engine = create_engine(url)
connect = engine.connect()

session = Session(bind=engine)

# command = "show tables"
#
# use = connect.execute(text(command))
#
# for i in use:
#     print(i)
print(session.query(('user')).all())
