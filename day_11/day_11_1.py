# scope

# local scope
# local scopes can only be used when you the inside the function


def portion():
    portion_strength = 2
    print(portion_strength)


portion()


# global scopoe

# global scope can be used outside the function

health = 10


def portion():
    portion_strenght = 2
    print(health)


portion()

# modify global scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside functions: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# or you can also modify using 'return'
enemies = 1


def increase_enemies():
    print(f"enemies inside functions: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# global contants

PI = 3.14159
URL = "http://www.google.com"
TWITTER_HANDLE = "@ray_billz"


def calc():
    PI
