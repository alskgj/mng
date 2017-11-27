moves = 0


def move(start, help, end, n):
    global moves
    if n == 1:
        moves += 1
        print("Lege oberste Scheibe von Turm %s auf Turm %s." % (start, end))

    else:
        move(start, end, help, n-1)  # move n-1 pieces to mid
        move(start, help, end, 1)    # move remaining piece to end
        move(help, start, end, n-1)  # move n1 pieces form mid to end

move('a', 'b', 'c', 4)
print("anzahl bewegungen: %s" % moves)
