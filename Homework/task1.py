#def compute_series(n,num_terms):
    #result = 0
    #current_term = n

    #for _ in range (num_terms):
     #   result += current_term
    #    current_term = current_term *10 + n
   # return result

#n= int(input("Enter an interger(n):"))
#num_terms = int(input("Enter the number of terms (k):"))

#sum_of_series = compute_series(n,num_terms)
#print("the sum of the series is : sum_of_series")



#n = int(input("Enter an integer (n) : "))
#num_terms= int(input("Enter the numbers of terms (k): "))

#result = 0
#current_term = n
#multiplier = 1

#for _ in range (num_terms):
   # current_term = str(current_term * 10) + "n"
    #multiplier *= 10

#print(current_term)




#def calculate_term(n,term_number):
 #   return int(str(n) * term_number)
#def cumpute_series(n,num_terms):
    #series = [calculate_term(n,i)for i in range (1,num_terms +1)]
    #return sum(series)

#n= int(input("Enter an integer (n): "))
#num_terms=int(input("Enter the number of term (k): "))


#sum_of_series=cumpute_series(n,num_terms)
#print("The sum of the series is :",sum_of_series)




def generate_series (n,num_terms):
    series = [int (str(n)*i) for i in range(1,num_terms +1)]
    return series

n= int(input("Enter an integer (n): "))
num_terms=int(input("Enter the number of term (k): "))

series = generate_series(n,num_terms)

print(f"the series is :{'+'.join(map(str,series))}")
