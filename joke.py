#i will show random jokes
import random
from plyer import notification


print("i think u want to laugh :)")

joke = [
    "What do you call a sleeping bull?A bulldozer.",
    "Why do melons have weddings?They cantaloupe.",
    "How do you make a tissue dance?You put a little boogie in it.",
    "why did the photo go to jail?It was framed.",
    "Why did the golfer bring an extra pair of pants?In case he got a hole in one.",
    "Why did the baby strawberry cry?His parents were in a jam.",
    "Why did the scarecrow win an award?He was outstanding in his field.",
    "What kind of jewelry do rabbits wear?14 carrot gold.",
    "Where do polar bears keep their money?In a snowbank.",
    "What do you call a factory that makes okay products?A satis-factory.",
    "What do you call a sleeping bull?A bulldozer.",
    "Why do melons have weddings?They cantaloupe.",
    "How do you make a tissu#e dance?You put a little boogie in it."
]

random.shuffle(joke)
print("here is your joke \n")
print(random.choice(joke))
