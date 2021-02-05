def qb(y,x,z):
    if y > 0 and x > 0:
        z = z
    elif y > 0 and x < 0:
        z = z + 200
    elif y < 0 and x < 0:
        z = z + 200
    elif y < 0 and x > 0:
        z = z + 400

    return z