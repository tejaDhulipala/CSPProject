def intInput(prompt):
    ans = input(prompt)
    breakLoop = False
    while not breakLoop:
        try:
            final = int(ans)
            breakLoop = True
        except ValueError:
            ans = input("Please Try Again! " + prompt)
    return final


def toScreenPos(pos, screenPos):
    return (pos[0] - screenPos[0], pos[1] - screenPos[1])