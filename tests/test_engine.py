import unittest

from text_adventure.engine import TextAdventureEngine


class TextAdventureEngineTestCase(unittest.TestCase):
    def test_instance(self):
        e = TextAdventureEngine()
        self.assertEqual(True, isinstance(e, TextAdventureEngine))

    def test_add_room(self):
        e = TextAdventureEngine()
        room1 = e.add_room(name='starting room', description='you wake up in a starting room')
        self.assertEqual(1, e.number_rooms)
        self.assertEqual('starting room', room1.name)

        room2 = e.add_room(name='room 1', description='room after leaving start')
        self.assertEqual(2, e.number_rooms)
        self.assertEqual('room 1', room2.name)

    def test_connect_rooms(self):
        e = TextAdventureEngine()
        room1 = e.add_room(name='starting room', description='you wake up in a starting room')
        room2 = e.add_room(name='room 1', description='room after leaving start')

        self.assertEqual(0, len(room1.connections))
        self.assertEqual(0, len(room2.connections))

        e.connect_rooms(source='starting room', destination='room 1', direction='left')
        self.assertEqual(1, len(room1.connections))
        self.assertEqual(1, len(room2.connections))

        self.assertEqual(room2, room1.connections['left'].get('room'))
        self.assertEqual(room1, room2.connections['back'].get('room'))

        with self.assertRaises(RuntimeError):
            e.connect_rooms(source='starting room', destination='doesnt exist', direction='right')

    def test_state_machine(self):
        e = TextAdventureEngine()
        e.add_room(name='starting room', description='you wake up in a starting room')
        e.add_room(name='room 1', description='room after leaving start')
        e.add_room(name='finish', description='outside world', is_end=True)

        e.connect_rooms(source='starting room', destination='room 1', direction='left', description='you see a door to your left')
        e.connect_rooms(source='room 1', destination='finish', direction='forward', description='the exit is right in front of you')

        e.start()


if __name__ == '__main__':
    unittest.main()
