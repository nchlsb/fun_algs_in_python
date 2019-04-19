def scale_ascii(string, scale):

    ret_string = ""
    
    for line in string.splitlines(): # why is this not split_lines()?
        line_to_scale = ""
        
        for char in line:   
            for i in range(0, scale):
                line_to_scale += char
                
        for i in range(0, scale):
            ret_string += line_to_scale + "\n" # not sure if this needs to differ between OSs   

    return ret_string        


string = ""

with open("art.txt", 'r') as file:
    for line in file:
        string += line


print(scale_ascii(string, 2))
