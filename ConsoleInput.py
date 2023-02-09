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