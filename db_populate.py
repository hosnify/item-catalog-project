"""
This script populate database with fake data for testing
"""
from project2 import db , bcrypt
from project2.models import Category , Course , User

db.drop_all()
db.create_all()

hashed_password = bcrypt.generate_password_hash('password')
user = User(user_name = 'admin' ,password=hashed_password , email='admin@test.com')
db.session.add(user)
db.session.commit()

engineering=Category(name='Engineering', description='Courses for Engineering students' , author = user)
language=Category(name='Language Learning', description='Courses for Language students' , author = user)
business=Category(name='Business', description='Courses for Business students' , author = user)

db.session.add(engineering)
db.session.add(language)
db.session.add(business)
db.session.commit()


course_1=Course(name='Marketing' , description='Learn principles of marketing' , author= user , category=business , price = 100 )
course_2=Course(name='Corporate Finance' , description='Learn key financial concepts ' , author= user , category=business , price = 250 )
course_3=Course(name='Engineering Mechanics' , description='Introduction to Engineering Mechanics' , author= user , category=engineering , price = 150 )
course_4=Course(name='Systems Engineering' , description='Introduction to Systems Engineering' , author= user , category=engineering , price = 300 )
course_5=Course(name='English Phonetics' , description='The sounds of English and the International Phonetic Alphabet' , author= user , category=language , price = 100 )
course_6=Course(name='Chinese for Beginners' , description='introduction of phonetics and daily expressions in Chinese' , author= user , category=language , price = 200 )

db.session.add(course_1)
db.session.add(course_2)
db.session.add(course_3)
db.session.add(course_4)
db.session.add(course_5)
db.session.add(course_6)

db.session.commit()