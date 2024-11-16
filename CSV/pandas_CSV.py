import pandas as pd
import sys


sys.path.append('D:')
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)

baca = pd.read_csv("D:\\data.txt")

print(baca)