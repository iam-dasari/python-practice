# A Module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py added. Within a module, 
# the module's name (as a string) is available as the value of the global variable __name__.

import math
import module1

x = math.sqrt(16)
print(x)
y = math.pow(2, 3)
print(y)

add = module1.add(10, 20)
print(add)
sub = module1.sub(10, 20)
print(sub)
mul = module1.mul(10, 20)
print(mul)
div = module1.div(10, 20)
print(div)