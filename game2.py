import numpy as np

def random_predict(number:int=1) -> int :
    count=0
    while True :
        count+=1
        predict_number=np.random.randint(1,100)
        if predict_number==number:
            break
    return count


print(f'pocet pokusov je {random_predict(10)}')