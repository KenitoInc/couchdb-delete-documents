import sys
from app import DeleteDocuments

dd = DeleteDocuments()

#accept parameters from the commandline
database = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
dd.delete(database, username, password)
