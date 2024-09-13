from model.connection import collection
from faker import Faker

fake=Faker()

class Crud():
    def __init__(self):
        pass

    def insert(self):
        for self.id in range(1,51):
            self.info=fake.boolean()
            self.name=fake.first_name()
            self.surname = fake.last_name()
            self.birthday = str(fake.date_of_birth())
            self.last_login = str(fake.date())
            self.sign_out_time = fake.time()


            collection.insert_one({"id":self.id,
                                    "name":self.name,
                                    "surname":self.surname,
                                    "birthday":self.birthday,
                                    "last_login":self.last_login,
                                    "sign_out_time":self.sign_out_time,
                                    "info":self.info})
    def update(self):
        a=int(input("Enter admin id: "))
        b=input("Enter what would you like to change: info/name/surname/birthday/last_login/sign_out_time")
        new_value=input("Enter the new value for {b}")

        update_field={b:new_value}

        collection.update_one({"id":a},{"$set":update_field})
        print(f"Updated document with ID {a}: set {b} to {new_value}")
    
    def delete(self):
        x=int(input("Enter admin id that you would like to delete: "))
        collection.delete_one({"id":x})
        print(f"Deleted successfully")
    
    def search(self,regex_pattern):
        results =collection.find({"name": {"$regex": regex_pattern}})
        for result in results:
            print(result["name"])


obj=Crud()
#obj.insert()
#obj.search("^W")
#obj.search("a$")