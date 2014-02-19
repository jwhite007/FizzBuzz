#!/usr/bin/env python

fb_dict = {3: 'Fizz', 5: 'Buzz'}

def fizzbuzz(num):
    #pass
    fb_dict_keylist = list(fb_dict.keys())
    s_list = sorted(fb_dict_keylist)
    fb_string = ''
    if num <= 1:
        return str(num)
    else:
        for i in s_list:
            if num % i == 0:
                fb_string = fb_string + fb_dict[i]
            else:
                fb_string = fb_string
        if len(fb_string) != 0:
            return fb_string
        else:
            return str(num)


def extend_fizzbuzz(key, string):
    #pass
    if key in fb_dict:
        return "Your number is already used by FizzBuzz"
    else:
        fb_dict[key] = string

if __name__ == '__main__':
    """Documentaion and tests"""


    additional={}

