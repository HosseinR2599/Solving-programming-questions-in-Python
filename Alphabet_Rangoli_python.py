def print_rangoli(size):
    
    if 0 < size < 27:
        
        Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        pattern = []
        
        for i in range(size):
            
            left = Alphabet[size-1:i:-1]
            right = Alphabet[i:size]
            
            s = '-'.join(left + right)
            
            pattern.append(s.center(4*size-3, '-'))
            
        print('\n'.join(pattern[::-1] + pattern[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
