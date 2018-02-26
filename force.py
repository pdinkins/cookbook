import math

def force():
    a = float(input('acceleration: '))
    m = float(input('mass: '))
    f = m * a
    print(f)

def velocity():
    v0 = float(input('initial velocity: '))
    ac = float(input('acceleration: '))
    t = float(input('time: '))
    v = v0 + (ac * t)
    print(v)


while True:
    run = input('[force: f / velocity: v]')
    if run == 'f':
        force()
    elif run == 'v':
        velocity()
