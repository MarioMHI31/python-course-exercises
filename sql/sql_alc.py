
# SQL Alchemy - este o librarie care foloseste principiul ORM
# ORM - Object Relational Mapper

# Install: pip install sqlalchemy

# Import
from sql_alc import create_engine, Column, Integer, String
from sql_alc.orm import sessionmaker, declarative_base
import pymysql

# Credentials
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = ''
DATABASE = 'myfirstdb'
TABLE = 'student'


# Connection string
# connection_string = mysql+DRIVER_NAME://USER:PASSWORD@HOST:PORT/DATABASE
connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# Create engine
engine = create_engine(connection_string)

# Declarative base
Base = declarative_base() # class ...
Session = sessionmaker(bind=engine)

# Session started HERE
session = Session()

# Object declaration
# View is a Virtualize Table
class Student(Base):
    __tablename__ = TABLE

    id = Column(Integer(), primary_key=True)
    name = Column(String(100))
    age = Column(Integer())
    grade = Column(String(10))

# CREATE - INSERT INTO ...
# new_student = Student(name="Nume Exemplu", age=20, grade="B")
# session.add(new_student)
# session.commit()

# DELETE and LIKE
# Define pattern
# %Exemplu - CEVAExemplu
# Exemplu% - ExempluCEVA
# %Exemplu% - CEVAExempluCEVA

# first => CEVA2Exemplu, CEVA1Exemplu => CEVA2Exemplu
# student_to_delete = session.query(Student).filter(Student.name.like('%Exemplu%')).first()
# session.delete(student_to_delete)
# session.commit()

# LIMIT
limited_students = session.query(Student).limit(5).all()
for student in limited_students:
    print(student.name)


# UPDATE
session.query(Student).filter(Student.id > 18).update({Student.age: 24, Student.grade: "C"})
session.commit()

# Update bulk
# for i in range(10,15):
#     session.query(Student).filter(Student.id == i).update({Student.name: "Nume Modificat"})
# session.commit()


# READ - SELECT * FROM student
students = session.query(Student).all()
for student in students:
    print('ID:',student.id)
    print('Name:', student.name)
    print('Age:', student.age)
    print('Grade:', student.grade)

    print('-' * 20)


session.close()