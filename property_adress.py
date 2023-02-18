class House:
    def __init__(self, address, num_rooms, area):
        self._address = address
        self._num_rooms = num_rooms
        self._area = area

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def num_rooms(self):
        return self._num_rooms

    @num_rooms.setter
    def num_rooms(self, num_rooms):
        self._num_rooms = num_rooms

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        self._area = area
        
house = House("123 Puskina", 4, 250)
print(house.address) 
print(house.num_rooms) 
print(house.area) 

house.address = "456 Kalatushkina "
house.num_rooms = 3
house.area = 200
print(house.address) 
print(house.num_rooms)
print(house.area) 