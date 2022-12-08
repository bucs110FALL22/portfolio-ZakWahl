import pygame

pygame.init()
display = pygame.display.set_mode()
font = pygame.font.Font('freesansbold.ttf', 20)

upper_limit = 20
iters = {}
start = 2
n = start
count = 0
max_so_far = 0
max_val = 0
scale = 10

#for x in range(start,upper_limit):
x = 101
while x != 1:
    count += 1
    if x % start == 0:
        x = x / 2
    else:
        x = (x * 3) + 1
    print(x)
print('Number of Iterations: ', count)

for n in range(start, upper_limit + 1):
    x = n
    count = 0
    while x != 1:
        count += 1
        if x % start == 0:
            x = x / 2
        else:
            x = (x * 3) + 1
        print(x)
    # add item to dictionary
    iters[n] = count
    #drawline
    # find max count or set
    if count > max_so_far:
        max_so_far = count
        max_val = n
    print('Number of Iterations: ', count)
    print(iters.items())
    print(max_so_far, max_val)
    display.fill("blue")
    if len(iters.items()) >= 2:
        coords = [(x * scale, y * scale) for x, y in list(iters.items())]
        pygame.draw.lines(display, 'white', False, coords)
        new_display = pygame.transform.flip(display, False, True)
        display.blit(new_display, (10, 10))
        pygame.display.flip()

    string = f"The max iterations so far is {max_val} with {max_so_far} iterations"
    msg = font.render(string, True, "white")
    display.blit(msg, (10, 10))
    pygame.display.flip()
    pygame.time.wait(3000)
