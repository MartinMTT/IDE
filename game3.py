import numpy as np

def gen_1_100int(men,viac):                                 # generuje medzi menej a viac
    return np.random.randint(men,viac+1)                

def random_predict(number:int=1) -> int :                   # zisti na kolkokrat najde
                                                            # generuje random    
    count=0
    predict_number=gen_1_100int(1,101)
    mensie=1
    vacsie=100

    while True :
        count+=1                                            # pocita pokusy
#        print(number,count,predict_number)                 # aby clovek videl/man to see
        if predict_number==number:                          # algoritmus zmensenia intervalu
            break
        elif predict_number < number:
            mensie=predict_number                           # zmensi interval
            predict_number=gen_1_100int(mensie,vacsie)
        elif predict_number > number:
            vacsie=predict_number
            predict_number=gen_1_100int(mensie,vacsie)
            
    return count


def score_game(random_predict) -> int:                      # rata priemer hladani
      
    count_ls = [] 
#    np.random.seed(11)                                     # neviem naco to chcu
                                                            # why? it false output
    random_array = np.random.randint(1, 101, size=(100))    # generuje zoznam 100 nahodnych cisel
    pocitadlo=0
    
    for num in random_array:                                
        pocitadlo+=1
        count_ls.append(random_predict(num))                # ulozi do zoznamu pocet hladani

    score = int(np.mean(count_ls))                          # priemer hladani

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')    # vysledok/average
    return(score)


score_game(random_predict)                                  # run