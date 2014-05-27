#-*- coding:utf-8 -*-

__author__ = 'lionel'

"""
PGLeon.src.conf
Gestion de la partie configuration de pgleon.
"""

from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, BooleanField, TextField
from PyQt4.QtGui import QDesktopServices

d = QDesktopServices.storageLocation(QDesktopServices.DataLocation)
print(d)

#TODO : mettre la base dans le répertoire personnel de l'utilisateur
conf_db = SqliteDatabase('pgleon.db')


class Connection(Model):
    host = CharField(null=True)
    port = CharField(null=True)
    database = CharField(null=True)
    user = CharField(null=True)
    password = CharField(null=True)
    name = CharField(null=False)
    internal = BooleanField(default=False)

    class Meta:
        database = conf_db
        # indexes = (
        #     # Index unique
        #     (('host', 'port', 'database', 'user'), True),
        # )


class Section(Model):
    connection = ForeignKeyField(Connection, related_name='sections')
    name = CharField(null=False)


class Query(Model):
    connection = ForeignKeyField(Connection, related_name='queries')
    section = ForeignKeyField(Section, related_name='queries')
    name = CharField(null=False)
    description = CharField()
    query = TextField(null=False)
    internal = BooleanField(default=False)  # Requetes internes à pgleon, ne pas effacer ni afficher dans l'ui
    deletable = BooleanField(
        default=True)  # Requetes pouvant être effacées. Les requetes globales et internes seront à False

    class Meta:
        database = conf_db
        indexes = (
            (('section', 'name'), True),
        )


Connection.create_table(True)
Query.create_table(True)


def fixtures():
    """Create defaults items"""
    qList = [["Tables list", "List tables except system ones",
              """SELECT table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
AND table_schema NOT IN ('pg_catalog', 'information_schema');"""],
             ["All tables list", "List all tables, including system tables",
              """SELECT table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE';"""],
             ["Views list", "List views except system ones",
              """SELECT table_name
FROM information_schema.views
WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
AND table_name !~ '^pg_';"""],
             ["ALl views list", "List all views, including system views",
              """SELECT table_name
FROM information_schema.views;"""]
    ]

