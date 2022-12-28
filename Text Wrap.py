import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    char_list = wrapper.wrap(string)
    x = ""
    for chars in char_list:
        x = x + chars + "\n"
    return x
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
