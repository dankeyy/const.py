import const

(BANANA, apple), (pear, poo) = (2, 1), (1,2)

ORANGE: int = 3

def f():
    global BANANA
    print(BANANA)
    BANANA = 3

# always catch the first, so this won't be caught until BANANA's second assignment is removed
ORANGE = 1
