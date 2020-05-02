from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(
    "postgres://onebgrqspswdak:3e9169b70a48b137e4bf660a6f55e6538399559254d754cf9a46e5c79fba1e4e@ec2-54-246-90-10.eu-west-1.compute.amazonaws.com:5432/dcltn92ol3e8md",
    echo=True)
Session = sessionmaker(bind=engine)


class Tweet(Base):
    __tablename__ = "tweets"
    id = Column('id', Integer, primary_key=True)
    user = Column('username', String)
    date = Column('date', String)
    likes = Column('likes', Integer)
    retweets = Column('retweets', Integer)
    comments = Column('comments', Integer)
    text = Column('text', String)

    def add(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
