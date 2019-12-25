def is_leap(year):
    leap = False
    y=year
    if y<=10**5 and y>=1900:
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        elif year % 4 == 0:
            leap = True
        
    return leap

year = int(input())
print(is_leap(year))
