def Main():
    score = input()
    for _ in range(int(score)):
        score = list(map(int, input().split(' ')))

        n = score.pop(0)

        i = 0
        above_avg = 0
        avg = sum(score) / int(n)

        for i in range(0, int(n)):
            if score[i] > avg:
                above_avg += 1
            i += 1
    
        ratio = 100 * above_avg / int(n)

        print('%.3f' %ratio, end='%\n')
        

if __name__ == '__main__':
    Main()