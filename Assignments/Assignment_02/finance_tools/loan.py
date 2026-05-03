def calculate_emi(principal,annual_rate,years):
    r= (annual_rate/12)/100
    n= years*12
    emi =(principal *1*(1+r)**n)/((1+r)**n -1)
    return emi