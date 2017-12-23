import random

Noun = "He She I Arnold Jennifer"
Verb = "ran walked spit sang huddled danced hopped skipped juggled skated"
place = "zoo cafeteria hall playground gym alter pool mall"

Noun = Noun.split(" ")
Verb = Verb.split(" ")
place = place.split(" ")

Noun.append("Joseph")

print(f"{random.choice(Noun)} {random.choice(Verb)} all day in the {random.choice(place)}.")
