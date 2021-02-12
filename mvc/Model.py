import json

class Person(object):
    def __init__(self, first_name = None, last_name = None):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_name(self):
        return '{} {}'.format(self.first_name,self.last_name)

    @classmethod
    def get_all(cls):
        database = open('/Users/vipinkumar/Documents/git/python-learners/mvc/person_db.json','r')
        # database = '{"p1":{"first_name":"Vipin","last_name":"Kumar"}}'
        result = []
        json_list = json.loads(database.read())
        print(json_list)

        for i in json_list:
            print(i)
            item = json.loads(i)
            person = Person(item['first_name'],item['last_name'])
            result.append(person)

        return result
        