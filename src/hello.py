import sqlalchemy 
from sqlalchemy import text
from repository.database import SessionLocal
from repository.database import engine

def checkSession():
    with engine.connect() as connection:
        res = connection.execute(text('SELECT VERSION()'))
        connection.commit
        return res

def main():
    print(session)
    print(checkSession().all())

session = SessionLocal()

if __name__ == "__main__":
    main()
    
