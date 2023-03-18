import numpy as np

def gen_1_100int(men,vac):
    return np.random.randint(men,vac+1)

def random_predict(number:int=1) -> int :
    print(number)
    count=0
    predict_number=gen_1_100int(1,101)
    mensie=1
    vacsie=100
    print(f'mensie = {mensie},vacsie = {vacsie},generovane = {predict_number}')
#    print(predict_number)
    while True :
        count+=1 
        if predict_number==number:
            break
        elif predict_number < number:
            mensie=predict_number
            predict_number=gen_1_100int(mensie,vacsie)
            print(f'mensie = {mensie},vacsie = {vacsie},generovane = {predict_number}')
        elif predict_number > number:
            vacsie=predict_number
            predict_number=gen_1_100int(mensie,vacsie)
            print(f'mensie = {mensie},vacsie = {vacsie},generovane = {predict_number}')
    return count

'''
hadane_cislo=np.random.randint(1,100)
print(f'*********************** hadane_cislo {hadane_cislo}')
print(f'pocet pokusov je {random_predict(hadane_cislo)}')
'''

def score_game(random_predict) -> int:  
    count_ls = [] 
    np.random.seed(1) 
    random_array = np.random.randint(1, 101, size=(1000)) 
    pocitadlo=0
    for num in random_array:
        pocitadlo+=1
        if pocitadlo==200 :
            MMM=input()
        count_ls.append(random_predict(num))

    score = int(np.mean(count_ls)) 

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# print(f'Количество попыток: {random_predict()}')

score_game(random_predict)