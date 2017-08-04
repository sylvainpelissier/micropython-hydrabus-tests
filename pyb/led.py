import pyb
from pyb import LED

l1 = pyb.LED(1)
l2 = pyb.LED(2)
l3 = pyb.LED(3)

leds = [LED(i) for i in range(1, 4)]

# test printing
for l in leds:
    print(l)

# test on and off
for l in leds:
    l.on()
    assert l.intensity() == 255
    pyb.delay(100)
    l.off()
    assert l.intensity() == 0
    pyb.delay(100)

# test toggle
for l in 2 * leds:
    l.toggle()
    assert l.intensity() in (0, 255)
    pyb.delay(100)
