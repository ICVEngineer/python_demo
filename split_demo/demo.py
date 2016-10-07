#!/usr/bin/python

print("split demo")

str_cur_info = "int_mask 4 RW 3-0 4'h0 mask int"
#print(str_cur_info.split(' ', 5))
field_name, field_width, field_type, field_pos, field_default, field_comment = str_cur_info.split(" ", 5)
print("field_name == %s" %field_name)
print("field_width == %s" %field_width)
print("field_type == %s" %field_type)
print("field_pos == %s" %field_pos)
print("field_default == %s" %field_default)
print("field_comment == %s" %field_comment)
