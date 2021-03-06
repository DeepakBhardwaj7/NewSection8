import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field can't be blank")
    parser.add_argument('password', type=str, required=True, help="This field can't be blank")

    def post(self):
        data = UserRegister.parser.parse_args()
        if (UserModel.find_by_username(data['username'])):   ## used To check the duplicacy
            return {"message": "username already exists!!"}, 400

        user=UserModel(**data)
        user.save_to_db()
        return {"message": "Account created!"}
#----------------------------------------------------------------------------
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO users VALUES(NULL,?,?)"
        # cursor.execute(query, (data['username'], data['password']))
        #
        # connection.commit()
        # connection.close()
        return {"message": "Account created!"}


