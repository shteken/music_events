import uuid
import pathlib
import pandas as pd
import random

NUMBER_OF_USERS = 10
country_file = pathlib.Path('./source_files/countries.csv')
user_file = pathlib.Path('./source_files/users.csv')

def generate_users(source, user_to_generate):
    country_df = pd.read_csv(source)
    countries = country_df.countryCode
    users = [(random.choice(countries), uuid.uuid4()) for user in range(user_to_generate)]
    user_df = pd.DataFrame(users, columns=['countryCode', 'userUUID'])
    user_df.rename_axis(['userID'], inplace=True)
    return user_df

generate_users(country_file, NUMBER_OF_USERS).to_csv(path_or_buf=user_file)