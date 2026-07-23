import mysql.connector

from config import HOST,USER,PASSWORD,DATABASE


def connect_database():

    connection = mysql.connector.connect(

        host=HOST,

        user=USER,

        password=PASSWORD,

        database=DATABASE

    )

    return connection