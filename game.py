import numpy as np

number=np.random.randint(1,100)
count=0
while True :
    count+=1
    predict_number=int(input('Uhadni cislo od 1 do 100 : '))
    if predict_number>number:
        print('Cislo je vacsie')
    elif predict_number<number:
        print('Cislo je mensie')
    else:
        print(f"Uhadol si, cislo je {predict_number} na {count} pokusov")
        break