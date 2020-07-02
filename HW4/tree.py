def Main():
    n_tests = int(input())

    for _ in range(n_tests):
        score = input_tree()

        for i in range(len(score)-1):
                score[i].append(split(score[i][1]))

        for i in range(len(score)-1):
            score[i].append(len(score[i][1]))

        score.pop()
        score.sort(key = lambda score: score[2]) 
        score.sort(key = lambda score: score[3])

        for i in range(len(score)):
            for j in range(len(score)):
                if i == j:
                    break
                if score[i][1] == score[j][1]:
                    status = False
                else:
                    status = True
        
        tree = []

        print(score)
        
        

def split(word): 
    return [char for char in word]  

def input_tree():
    scores = input().split(' ')

    scores = [sub.replace('(', '') for sub in scores] 
    scores = [sub.replace(')', '') for sub in scores] 

    for i in range(len(scores)):
        scores[i] = scores[i].split(",")

    return scores

if __name__ == '__main__':
    Main()