from flask import Flask, render_template
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DatabadeMapper import Base, UserInfo, UserAddress

#engine = create_engine('sqlite:///IPS.db')
engine = create_engine('sqlite:///IPS.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# @app.route('/')
# def DefaltUserAddress():
#     userInfo = session.query(UserInfo).first()
#     address = session.query(UserAddress).filter_by(userInfo_id = userInfo.id)
#     #address = session.query(UserAddress).filter_by(userInfo_id = userInfo.id)
#     output = ''
#     for i in address:
#         output += "</br>"
#         output += str(i.id)
#         output += "</br>"
#         output += i.firstname
#         output += "</br>"
#         output += i.lastname
#         output += "</br>"
#         output += i.phone
#         output += "</br>"
#
#     return output

@app.route('/user/<int:userInfo_id>/')
def Userinfo(userInfo_id):
    userInfo = session.query(UserInfo).filter_by(id = userInfo_id).one()
    address = session.query(UserAddress).filter_by(userInfo_id = userInfo_id)
    return render_template('user.html',userInfo = userInfo, address = address)

    #address = session.query(UserAddress).filter_by(userInfo_id = userInfo.id)
    # output = ''
    # for i in address:
    #     output += "</br>"
    #     output += str(i.id)
    #     output += "</br>"
    #     output += i.firstname
    #     output += "</br>"
    #     output += i.lastname
    #     output += "</br>"
    #     output += i.phone
    #     output += "</br>"
    #
    # return output
    


@app.route('/user/<int:userInfo_id>/new/')
def newUserInfo(userInfo_id):
    return "page to create a new menu item. Task 1 complete!"

# Task 2: Create route for editMenuItem function here

@app.route('/user/<int:userInfo_id>/edit/')
def editUserInfo(userInfo_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route('/user/<int:userInfo_id>/delete/')
def deleteUserInfo(userInfo_id):
    return "page to delete a menu item. Task 3 complete!"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '127.0.0.1', port = 5000)
