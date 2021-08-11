
from typing import ForwardRef



number = 1000



multiple = [i for i in range(number) if i%3 == 0 or i%5 == 0]
print(sum(multiple))





