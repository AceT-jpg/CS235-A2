import pytest
from domainmodel.actor import Actor

class TestDirectorMethods:

    def test_init(self):
        actor1 = Actor("Angelina Jolie")
        assert repr(actor1) == "<Actor Angelina Jolie>"
        actor2 = Actor("")
        assert actor2.actor_full_name is None
        actor3 = Actor(42)
        assert actor3.actor_full_name is None

    def test_eq(self):
        actor1 = Actor(None)
        actor2 = Actor("Robert Downey")
        actor3 = Actor("Scarlette Johansson")
        assert actor2.__eq__(actor3) == False
        assert actor3.__eq__(actor3) == True
        assert actor1.__eq__(actor3) == False

    def test_lt(self):
        actor1 = Actor("Cameron Diaz")
        actor2 = Actor("Arnold Shwarzeneger")
        actor3 = Actor("Brad Pitt")
        assert actor2.__lt__(actor1) == True
        assert actor3.__lt__(actor1) == True
        assert actor2.__lt__(actor3) == True
        assert actor3.__lt__(actor2) == False
        assert actor2.__lt__(actor1) == True

    def test_hash(self):
        actor1 = Actor(None)
        actor2 = Actor("Angelina Jolie")
        actor3 = Actor("Robert Downey")
        assert actor1.__hash__() == 0
        assert actor2.__hash__() == 14
        assert actor3.__hash__() == 13

    def test_add_actor_colleague(self):
        actor1 = Actor("Brad Pitt")
        assert actor1.add_actor_colleague("Robert Downey") == None

    def test_check_if_this_actor_worked_with(self):
        actor1 = Actor("Brad Pitt")
        actor1.add_actor_colleague("Robert Downey")
        assert actor1.check_if_this_actor_worked_with("Robert Downey") == True
        actor2 = Actor("Robert Downey")
        assert actor2.check_if_this_actor_worked_with("Brad Piit") == False
