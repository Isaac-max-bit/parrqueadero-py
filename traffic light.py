import random

color = ('red', 'yellow', 'green')

action = ('STOP', 'CAUTION', 'GO')

status = random.choice(color)


if status == color[0]:
    print(status.upper() + ' means ' + action[0])
elif status == color[1]:
    print(status.upper() + ' means ' + action[1])
else:
    print(status.upper() + ' means ' + action[2])
