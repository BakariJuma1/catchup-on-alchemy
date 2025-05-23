from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,Integer,DateTime,create_engine
from datetime import datetime


Base=declarative_base()
engine=create_engine("sqlite:///users.db")
Session= sessionmaker(bind=engine)
    

 # id int, 
    # usserna,e
    # email str
    # date created datetime

class User(Base):
    # tablename
    __tablename__ = 'users'
    id = Column(Integer(),primary_key = True)
    user_name= Column(String(25),nullable=False,unique=True)
    email= Column(String(18),unique=True,nullable=False)
    date_created= Column(DateTime(),default=datetime.utcnow)

    def __repr__(self):
        return(f" username:{self.user_name} \n email:{self.email}")
    
Base.metadata.create_all(bind=engine)    
session_one= Session()


users=[
    {
        "username":"jerry",
        "email":'jerry@gmail.com'
    },
     {
        "username":"jacky",
        "email":'jacky@gmail.com'
    },
     {
        "username":"jack",
        "email":'jack@gmail.com'
    },
     {
        "username":"jean",
        "email":'jean@gmail.com'
    },
]


session_one.query(User).delete()
session_one.commit()

# print(new_user)
for user in users:
    new_user=User(user_name=user["username"],email=user['email'])
    session_one.add(new_user)
    session_one.commit()
    print(f"added{user['username']}")
   
jerry=session_one.query(User).filter(User.user_name=='jerry')   
print(jerry)