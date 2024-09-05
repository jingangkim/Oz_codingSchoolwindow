from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class publisher(Base):
    __tablename__ = 'publishers'
    
    publisher_id = Column(Integer, primary_key=True)
    name = Column(String(45))
    address = Column(String(45))
    phone = Column(String(45))
    
    books = relationship('Book', back_populates='publisher')
    
class Book(Base):
    __tablename__ = 'books'
    
    book_id = Column(Integer, primary_key=True)
    title = Column(String(45))
    ISBN = Column(String(45))
    publication_date = Column(Date)
    price = Column(Integer)
    publisher_id = Column(Integer, ForeignKey('publishers.publisher_id'))
    
    publisher = relationship('publisher', back_populates='books')
    authors = relationship('bookAuthor', back_populates='books')
    cars = relationship('Cartsbooks', back_populates='book')
    
class Author(Base):
    __tablename__ = 'author'
    
    Author_id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    las_name = Column(String(45))
    brith_date = Column(Date)
    
    books = relationship('bookAuthor', back_populates='author')
    