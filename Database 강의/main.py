from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from model import Author, publisher, Book

# DSN 설정을 이용하여 엔진 생성
engine = create_engine(
    f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
)
Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

jingang = Author(Author_id = 1, first_name='진강', last_name='', birth_date='1997-02-16')
session.add(jingang)
session.commit()

goduck = publisher(publisher = 1, name='고덕', address='서울', phone='64794534')
session.add(goduck)
session.commit()

gildong = publisher(publisher = 1, name='길동', address='서울', phone='45344534')
session.add(gildong)
session.commit()

wanna_be_developer = Book(
    book_id = 1,
    title = '개발자가 되고 싶지만 게임도 잘하고 싶어',
    ISBN = '1234',
    publisher_date='2024-08-27',
    price=50000,
    publisher=goduck
)
session.add(wanna_be_developer)
session.commit()

goduck.address = '서울시 강동구' #업데이트하는 법
session.commit() 

session.delete(gildong)
session.commit()
