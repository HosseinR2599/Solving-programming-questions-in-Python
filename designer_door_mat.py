def STDOUT(N, M):
    if 5 < N < 101:
        if 15 < M < 303:
            for i in range(1, N, 2):
                pattern = '.|.' * i
                print(pattern.center(M, '-'))
            
            print("WELCOME".center(M, '-'))
            
            for j in range(N-2, 0, -2):
                pattern = '.|.' * j
                print(pattern.center(M, '-'))

if __name__ == '__main__':
    N, M = map(int, input().split())
    STDOUT(N , M)
