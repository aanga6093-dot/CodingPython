import itertools #liblari blue force 

matrix = [
    [1,1,1],
    [2,-1,1],
    [1,2,-1]
]

result = [6,3,2]
#kali vektor matrix dan combo vektor dan di total
def kali_matrix(vec, mat_row):
    return sum(a*b for a,b in zip(vec, mat_row))

def brute():
    #biat list angka jeng syarat kombinasi 
    numbers = range(-20, 20)
    #loop kombinasi hasil kan combo nu panjang nya matrix[0]
    for combo in itertools.product(numbers, repeat=len(matrix[0])):
        #loop lost vaktor in matrin input ka kali_matrix() jeng combo
        output = [kali_matrix(combo, row) for row in matrix]
        #bangding ken ouput jeng result 
        if output == result:
            return combo
            break  
    print("tidak ketemu")
print(brute())  
