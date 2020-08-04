def season(month):
    #если меньше 3, то будет зима. month ровняю к 12. значит меньще 3(12,1,2)
    if month <=2 and month>=1 or month==12:
        return "Winter"
    #дою альтернативное условия если меньше или равно 5ти
    elif month <=5 and month>=3:
        return "Spring" 
    #если меньше или равно 8
    elif month <=8 and month>=6:
        return "Summer" 
    #если меньше или равно 11 
    elif month <=11 and month>=9: 
        return "Autumn" 
    else:
        return "Error"
month=int(input("Enter month number: ")) 
num_month=season(month) 
print("Time year -",num_month)
