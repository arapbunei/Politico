from datetime import datetime
from ..utils.utils import generate_id

offices = []


"""Where i have annotations for specific functions"""

class Office(object):
    
    def save(self, data):
        
        """Saving new meetup"""
        
        data['id'] = generate_id(offices)
        data['created_on'] = datetime.now()
        data['modified_on'] = datetime.now()
        #data['type'] = 0
        offices.append(data)
        return data

    def exists(self, key, value):
        """ Function to check if question with provided key, value exists """
        office_exists = [office for office in offices if value == office[key]]
        return len(office_exists) > 0 

    def fetch_by_id(self, id):
       
        fetched_offices = [office for office in offices if office['id'] == id]
        return fetched_offices

  

    def all(self):
       
        return offices

    
            
    
