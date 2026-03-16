class User:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id
u = User(101)
print("User id:", u.id)