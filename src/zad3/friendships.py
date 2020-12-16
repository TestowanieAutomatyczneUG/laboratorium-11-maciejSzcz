class Friendships(object):
    def __init__(self):
        self.value = {}

    def make_friends(self, person1, person2):
        if type(person1) != str or type(person2) != str:
            raise TypeError("person must be of string type")
        self.add_friend(person1, person2)
        self.add_friend(person2, person1)
    
    def add_friend(self, person, new_friend):
        if person in self.value:
            self.value[person].append(new_friend)
        else:
            self.value[person] = [new_friend]

    def get_friends_list(self, person):
        if type(person) != str:
            raise TypeError("person must be of string type")
        elif person not in self.value:
            raise ValueError("person doesn't exist")
        return self.value[person]

    def are_friends(self, person1, person2):
        if type(person1) != str or type(person2) != str:
            raise TypeError("person must be of string type")
        elif person1 not in self.value[person2]:
            return False
        else:
            return True
