# Here you can see what ball is what colour. And in T it is the relation of all balls that touch each other.

White = {2,5,7}
Orange = {1,6}
Black = {3,4,9}
Green = {8,10}
Blue = {0}

T = {(0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),
(0,8), (0,9), (1,0), (1,2), (1,6), (1,7), (2,0),
(2,1), (2,3), (2,8), (3,0), (3,2), (3,4), (3,8),
(4,0), (4,3), (4,5), (4,9), (5,0), (5,4), (5,6),
(5,9), (6,0), (6,1), (6,5), (6,7), (7,0), (7,1),
(7,6), (7,8), (7,9), (7,10), (8,0), (8,2), (8,3),
(8,7), (8,9), (8,10), (9,0), (9,4), (9,5), (9,7),
(9,8), (9,10), (10,7), (10,8), (10,9)}

# my code is the following:
def touching(colour1, colour2):
    produkt = set({})
    for a in colour1:
        for b in colour2:
            produkt.add((a,b))
    if produkt in T:
      print("Erfüllt")
    else:
      print("Nicht erfüllt")
