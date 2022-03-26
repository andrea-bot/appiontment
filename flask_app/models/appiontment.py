from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class appiontment:
    def __init__(self,data):
        self.id = data['id']
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        
    @staticmethod
    def validate_appiontment(form_data):
        is_valid = True

        if len(form_data['task']) < 3 :
            flash("Task must be longer than 2 characters!","task")
            is_valid=False
        if form_data['date']=="":
            flash("Date must be given!","date")
            is_valid=False
        return is_valid


@classmethod
def save(cls,data):
    query = "INSERT INTO appiontments (task, date,status,user_id) VALUES ( %(task)s, %(date)s, %(status)s,%(user_id)s,);"

    new_appt_id = connectToMySQL('appiontment_db').query_db(query, data)

    return new_appt_id


