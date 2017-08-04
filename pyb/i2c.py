import pyb
from pyb import I2C

# test we can correctly create by id or name
for bus in (-1, 0, 1, 2, 3, "Z"):
    try:
        I2C(bus)
        print("I2C", bus)
    except ValueError:
        print("ValueError", bus)
