import random, sys, string, time

def c(text):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
    
def co(r, g, b, text):

    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


result_str = ''.join((random.choice(string.hexdigits) for i in range(random.randint(14, 23))))
essai = 0
while True:
    essai = essai + 1
    a = random.randint(1, 10000)
    rqred = random.randint(1, 1000)
    if a == rqred:
        sys.stdout.write(co(255, 215, 0, f"\rNuméro gagnant!!! attendu : {rqred}, tiré {a} au bout de {essai} essais!"))
        break
    else:
        sys.stdout.write(f"\rattendu = {rqred}, tiré = {a}")
    time.sleep(0.001)
