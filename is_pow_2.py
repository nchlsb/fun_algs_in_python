def is_pow_2(num):
    return (num & (num-1) == 0) and (num > 0)

def visualize_bitwise_and(num):
    line_len = len(bin(num)) + 2
    format_num_0s = "#0{0}b".format(len(bin(n)))
    ret_string = ""
    
    ret_string += "  {0}\n".format(bin(num))
    ret_string += "& {1}\n".format(n - 1, format(n-1, format_num_0s))
    for i in range(0, line_len):
        ret_string += "="
    ret_string += "\n"
    ret_string += "  {0}\n".format(format(n & n - 1, format_num_0s))
    
    return ret_string

n = 16

print(visualize_bitwise_and(n))

