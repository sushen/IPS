from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DatabadeMapper import Base, UserInfo, UserAddress

# engine = create_engine('sqlite:///IPS.db')
engine = create_engine('sqlite:///IPS.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def mainpage():
    users = session.query(UserInfo).all()
    output = ''
    for user in users:
        output += '<a href="/user/{}/">{}</a><br/><br/>'.format(user.id, user.email)
    return output

@app.route('/user/<int:userInfo_id>/')
def allUser(userInfo_id):
    userInfo = session.query(UserInfo).filter_by(id=userInfo_id).one()
    address = session.query(UserAddress).filter_by(userInfo_id= userInfo.id)
    output = ''
    for i in address:
        output += "</br>"
        output += str(i.id)
        output += "</br>"
        output += i.firstname
        output += "</br>"
        output += i.lastname
        output += "</br>"
        output += i.phone
        output += "</br>"

    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host = '127.0.0.1', port = 5000)
