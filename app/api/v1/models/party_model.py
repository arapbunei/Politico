from datetime import datetime
from ..utils.utils import generate_id

parties = []



class Party(object):
   

    def save(self, data):
      
        data['id'] = generate_id(parties)
        data['created_on'] = datetime.now()
        data['modified_on'] = datetime.now()
        parties.append(data)
        return data

    def fetch_by_id(self, id):
       
        fetched_parties = [party for party in parties if party['id'] == id]
        return fetched_parties

    def exists(self, key, value):
       
        fetched_parties = [party for party in parties if party[key] == value]
        return len(fetched_parties) > 0

    def all(self):
       
        return parties


    def delete(self, id):
        """ Function to delete item """
        #global parties
        part = [party for party in parties if party['id'] != id]
        return part

    def edit(self, id):
       
        for party in parties:
            if party['id'] == party_id:
                party['name'] = party['name']

            return party