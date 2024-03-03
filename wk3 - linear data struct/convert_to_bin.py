from stack import Stack

def conv_bin(dec_num):
    remainders = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        remainders.push(remainder)
        dec_num = dec_num // 2

    #print(remainders.get_stack())

    # need to reverse the stack and turn it into a string
    bin_string = ""
    while not remainders.is_empty():
        bin_string = bin_string + str(remainders.pop())

    return bin_string

print(conv_bin(233))
print(conv_bin(233) == "11101001")
print(conv_bin(255))
print(conv_bin(256))
