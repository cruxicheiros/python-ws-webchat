import asyncio
import datetime
import random
import websockets

class User:
    def __init__(self, name, websocket):
        self.name = name
        self.websocket = websocket

    def __hash__():
        return self.name

class Room:
    def __init__(self, name):
        self.name = name
        self.users = set()

    def __hash__():
        return self.name

    def add_user(user):
        user_count = len(self.users)
        self.users.add(user)
        user_count_increased = len(self.users) > user_count

        if not room_count_increased:
            raise Exception("User named " + user.name + " already exists in room " + self.name + ".")

    def remove_user(user):
        try:
            self.users.remove(user)

        except KeyError:
            raise Exception("User named " + user.name + " is not present in room " + self.name + ".")

    def get_user_by_name(name):
        for user in self.users:
            if user.name = name:
                return user

        raise Exception("User named " + name + " does not exist in room " + self.name + '.')

class Router:
    def __init__(self):
         self.rooms = set()

    def add_room(room):
        room_count = len(self.rooms)
        self.rooms.add(room)

        room_count_increased = len(self.rooms) > room_count

        if not room_count_increased:
            raise Exception("Room named " + room.name + " already exists.")

    def remove_room(room):
        try:
            self.rooms.remove(room)
        except KeyError:
            raise Exception("Room named " + room.name + " does not exist.")

    def get_room_by_name(name):
        for room in self.rooms:
            if room.name = name:
                return room

        raise Exception("Room named " + name + 'does not exist.')

class Connector:
    async def recieve(self):
        pass

    async def send(self, message, recipients):
        for recipient in recipients:
            recipient.websocket.send(message);

if __name__ == "__main__":
    start_server = websockets.serve(time, '127.0.0.1', 5678)
    router = Router()
    test_room = Room("test")
    test_user = User("test_user")

    test_room.add_user(test_user)
    router.add_room(test_room)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
