#!/usr/bin/python

print("def demo")

print("======================")
print("======= no arg =======")
print("======================")
def call_hello():
    print("hello world")

call_hello()

print("====================")
print("====== return ======")
print("====================")
def call_return():
    rslt_info = 3 * 5
    return rslt_info

rslt_call_return = call_return()
print("rslt_call_return = %d" %rslt_call_return)

print("====================")
print("======= para =======")
print("====================")
def call_shift(para_0, para_1):
    rslt_info = para_0 * para_1
    return rslt_info

rslt_call_shift = call_shift(2, 6)
print("rslt_call_shift = %d" %rslt_call_shift)
