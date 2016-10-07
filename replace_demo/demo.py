#!/usr/bin/python

import re

print("replace demo")

str_cur_info = "int_mask 4 RW 3-0 4'Hf mask int"

cur_pattern = re.compile("\d+\'h", re.IGNORECASE)

str_cur_info = re.sub(cur_pattern, "0x", str_cur_info)
print("str_cur_info == %s" %str_cur_info)
