import sys
sys.path.append('D:/download/python3.6.3/Lib/site-packages/sqlalchemy/')
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    '''表的名字'''
    __tablename__ = 'user2'
    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    def __init__(self, id, name):
        self.id = id
        self.name = name


def initDb():
    # 初始化数据库连接
    engine = create_engine(
        'mysql+mysqlconnector://root:123456@localhost:3306/mysql')
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)
    # 创建session对象
    session = DBSession()
    return session


def insertToDb(newUser):
    '''添加用户'''
    print('正在添加...')
    session = initDb()
    # # 创建新的user2对象
    # new_user = User(id='1', name='king')

    # 添加到session
    session.add(newUser)

    # 提交即保存到数据库
    session.commit()

    # 关闭session
    session.close()

    print('添加成功...')


def deleteToDb():
    '''删除用户'''
    print('正在删除...')
    session = initDb()
    user = session.query(User).filter(User.id == '2').one()
    session.delete(user)
    session.commit()
    session.close()
    print('删除成功...')
