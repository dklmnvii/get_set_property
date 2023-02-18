class House:
    def __init__(self, address, num_rooms, area):
        self._address = address
        self._num_rooms = num_rooms
        self._area = area

    
    def get_address(self):
        return self._address

    
    def set_address(self, address):
        self._address = address


    def get_num_rooms(self):
        return self._num_rooms

   
    def set_num_rooms(self, num_rooms):
        self._num_rooms = num_rooms

    
    def get_area(self):
        return self._area

   
    def set_area(self, area):
        self._area = area
        
house = House("123 Puskina", 4, 250)
print(house._address) 
print(house._num_rooms) 
print(house._area) 

house.address = "456 Kalatushkina "
house.num_rooms = 3
house.area = 200
print(house.address) 
print(house.num_rooms)
print(house.area) 