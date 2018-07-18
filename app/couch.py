
# !/usr/bin/env python3
# coding: utf-8
import json
import requests
import logging

class DeleteDocuments(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def delete(self, db, user, password):

        if len(db) == 0:
            sys.exit(1)

        r = requests.get("http://{}:{}@localhost:5984/{}/_all_docs".format(user, password, db))
        rows = json.loads(r.text)["rows"]
        print(len(rows))

        todelete = []
        for doc in rows:
            if not (doc['id'].startswith('_')):
                todelete.append({"_deleted": True, "_id": doc["id"], "_rev": doc["value"]["rev"]})
                self.logger.info('Deleting %s', doc["id"])
                print('Deleting %s', doc["id"])
            else:
                self.logger.info('Skipping %s', doc["id"])
                print('Skipping %s', doc["id"])

        r = requests.post("http://{}:{}@localhost:5984/{}/_bulk_docs".format(user, password, db),
                          json={"docs": todelete})
        print(r.status_code)
        self.logger.info('Final status code: %s', r.status_code)

