# test pyb module on F405 MCUs

import os, pyb

if not 'HydraBus1.0 with STM32F4' in os.uname().machine:
    print('SKIP')
    raise SystemExit

print(pyb.freq())
print(type(pyb.rng()))
