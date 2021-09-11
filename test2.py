"""
    до 300г - мелкие 
    до 500г - средние
    до 1000г - большие
"""

tomato_small = 300
tomato_medium = 500
tomato_big = 1000

tomato_user = int(input ("Сколько весит помидор \n"))
if tomato_user < tomato_small:
    print ("Кетчуп")
elif tomato_user >= tomato_small and tomato_user  < tomato_medium :
    print ("Помидор является мелким классом")
elif tomato_user >= tomato_medium and tomato_user < tomato_big :
    print ("Средний помидор")
elif tomato_user >= tomato_big:
    print ("Большой помидр")

    
