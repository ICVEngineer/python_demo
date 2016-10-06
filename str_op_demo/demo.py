#!/usr/bin/python

print("opcode demo")

print("====== (string cmp ======")
str_info0 = "aabb"
str_info1 = "aacc"
str_info2 = "aacc"

i_rslt = (str_info0 < str_info1)
print("%s < %s == %s" %(str_info0, str_info1, i_rslt))
i_rslt = (str_info0 <= str_info1)
print("%s <= %s == %s" %(str_info0, str_info1, i_rslt))
i_rslt = (str_info1 > str_info0)
print("%s > %s == %s" %(str_info1, str_info0, i_rslt))
i_rslt = (str_info1 >= str_info0)
print("%s >= %s == %s" %(str_info1, str_info0, i_rslt))
i_rslt = (str_info1 == str_info2)
print("%s == %s == %s" %(str_info1, str_info2, i_rslt))
i_rslt = (str_info0 != str_info1)
print("%s != %s == %s" %(str_info0, str_info1, i_rslt))

#print("====== (string join ======")
#str_rslt = {str_info0}.str_info1
#print("{str_info0}.str_info1 == (str_rslt")
