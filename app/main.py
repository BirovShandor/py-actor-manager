from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

Actor.objects.create(first_name="Emma", last_name="Watson")
Actor.objecastts.create(first_name="Daniel", l_name="Radclife")
print(Actor.objects.all())
Actor.objects.update(2, "Daniel", "Radcliffe")
print(Actor.objects.all())
Actor.objects.delete(1)
print(Actor.objects.all())
