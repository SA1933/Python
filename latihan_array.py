#array  in python
#                    in [1]: list = [1,2,3]
#                           list
#                    out[1]: [1,2,3]
#
#                    in[3]: import numpy as np
#                            arr = np.array([1,2,3])
#                            arr
#                    out[3]: array([1,2,3])

import numpy as np

some_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
some_array = np.asarray(some_list)

print(some_array)
print(type(some_array))