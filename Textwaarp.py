import textwrap

def wrap(string, max_width):
    if 0 < len(string) < 1000:
        if 0 < max_width < len(string):
            warpper = textwrap.TextWrapper(width= max_width)
            return warpper.fill(text= string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
