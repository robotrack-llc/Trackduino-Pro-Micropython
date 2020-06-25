from plumpx32.executor.led import BuiltinLED
from pyb import delay


BuiltinLED().color = BuiltinLED().Color.GREEN

for _ in range(3):
    BuiltinLED().on()
    delay(100)
    BuiltinLED().off()
    delay(100)
