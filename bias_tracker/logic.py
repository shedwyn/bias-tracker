from . import views

# 'Incident_str({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(
#     self.id, self.author_id, self.i_subject_id, self.filing_date,
#     self.i_date, self.i_time, self.i_type, self.i_descriptors,
#     self.text_description


# def check_id_in_db(user_id, user_database):
#     """take user_id and see if it is in the db of users, return bool val"""
#     if user_id in user_database:
#         return True
#     else:
#         return False
#
#
# def generate_error_message():
#     pass
#
#
# def get_db_name(user_id):
#     """receive user's login id and return user details for that login id"""
#     user_database = fetch_current_names_db()
#     id_validity = check_id_in_db(user_id, user_database)
#     if id_validity = True:
#         return user_id.name
#     else:
#         generate_error_message()
#         # what is this error message?  where does it appear on page?//
#         # probably need to add a warning alert on login page //
#         # possibly reverse the else consequences - return to login page
#         # with "lit" warning message?
#         return views.render_login_page(request)


# MENU PAGE #
#
# def write_more(key, values):
#     with open(database.txt, 'w') as humans_db_file:
#         human_database = humans_db_file.readlines()
#     print(human_database)
#     human_database.write(key values)
#     print(human_database)


# INCIDENT PAGE #
