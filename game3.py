import numpy as np

def gen_1_100int(men,viac):
    return np.random.randint(men,viac+1)

def random_predict(number:int=1) -> int :
    
    count=0
    predict_number=gen_1_100int(1,101)
    mensie=1
    vacsie=100

    while True :
        count+=1 
#        print(number,count,predict_number)
        if predict_number==number:
            break
        elif predict_number < number:
            mensie=predict_number
            predict_number=gen_1_100int(mensie,vacsie)
        elif predict_number > number:
            vacsie=predict_number
            predict_number=gen_1_100int(mensie,vacsie)
            
    return count


def score_game(random_predict) -> int:
      
    count_ls = [] 
#    np.random.seed(11) 
    random_array = np.random.randint(1, 101, size=(100)) 
    pocitadlo=0
    
    for num in random_array:
        pocitadlo+=1
        count_ls.append(random_predict(num))

    score = int(np.mean(count_ls)) 

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


score_game(random_predict)