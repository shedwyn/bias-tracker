from . import views

# from django.db import models
#
#
# class User(models.Model):
#     user_name = models.CharField()
#     email = models.CharField()
#     sign_up_date = models.DateTimeField()


def fetch_current_names_db():
    """return dictionary of instantiated user details"""
    with open(database.txt, 'w') as humans_db_file:  # should this be 'r'?
        user_database = humans_db_file.readlines()
    # format into proper dictionary?
    return user_database


def check_id_in_db(user_id, user_database):
    """take user_id and see if it is in the db of users, return bool val"""
    if user_id in user_database:
        return True
    else:
        return False


def generate_error_message():
    pass


def get_db_name(user_id):
    """receive user's login id and return user details for that login id"""
    user_database = fetch_current_names_db()
    id_validity = check_id_in_db(user_id, user_database)
    if id_validity:
        return user_id.name
    else:
        generate_error_message()
        return views.render_login_page(request)


# MENU PAGE #

def write_more(key, values):
    with open(database.txt, 'w') as humans_db_file:
        human_database = humans_db_file.readlines()
    print(human_database)
    human_database.write(key values)
    print(human_database)


# INCIDENT PAGE #

write_more()
