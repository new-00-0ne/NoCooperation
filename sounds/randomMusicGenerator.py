import random
print(random.choice(("a flat", "a", "b flat", "b", "c",\
    "c sharp", "d", "e flat",  "e", "f", "f sharp", "g")))
print(random.choice(("major", "minor")))
for i in range(8):
	print("Chord Number:", random.choice((1, 1, 2, 3, 4, 4, 5, 5, 6, 7)),\
	 "   For ", random.randint(1,6), " beats")
random.randint
input("press Enter to exit")