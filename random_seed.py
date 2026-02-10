# Data can be regenerated when using randoms
import random

random.seed(1)
print(random.random()) # OP: 0.13436424411240122

random.seed(1)
print(random.random()) # OP: 0.13436424411240122

random.seed(2)
print(random.random()) # OP: 0.9560342718892494

random.seed(1)
print(random.random()) # OP: 0.13436424411240122

random.seed(2)
print(random.random()) #OP: 0.9560342718892494

