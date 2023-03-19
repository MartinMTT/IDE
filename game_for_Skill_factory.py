import numpy as np

def gen_half_int(men,viac):                                 # generuje polovicu medzi menej a viac

    return (men+viac)//2        

def half_interval(number:int=1) -> int :                   # zisti na kolkokrat najde number
                                                            # half interval alghoritmus    
    count=0
    predict_number=gen_half_int(1,100)
#    print(number,count,predict_number)                      # aby clovek videl
    mensie=1
    vacsie=100

    while True :
        count+=1                                            # pocita pokusy
        if predict_number==number:                          # algoritmus zmensenia intervalu
            break
        elif predict_number < number:
            mensie=predict_number                           # zmensi interval
            predict_number=gen_half_int(mensie,vacsie)
#            print(number,count,predict_number)             # man to see
        elif predict_number > number:
            vacsie=predict_number
            predict_number=gen_half_int(mensie,vacsie)
#            print(number,count,predict_number)
            
    return count


def score_game(half_interval) -> int:                      # rata priemer hladani
      
    count_ls = [] 
#    np.random.seed(11)                                     # neviem naco to chcu
                                                            # /why? it false output
    random_array = np.random.randint(1, 100, size=(1000))    # generuje zoznam 1000 nahodnych cisel
    
    pocitadlo=0
    for num in random_array:                                
        pocitadlo+=1
        count_ls.append(half_interval(num))                # ulozi do zoznamu pocet hladani

    score = int(np.mean(count_ls))                          # priemer hladani

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')    # vysledok/average
    return(score)


score_game(half_interval)                                  # run