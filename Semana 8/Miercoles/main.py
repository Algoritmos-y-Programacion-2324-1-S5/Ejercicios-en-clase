# base = 2, power = 3 => 2 * exponential(2,2) => 2 * 2 * 2 * 1
# base = 2, power = 2 => 2 * exponential(2,1) => 2 * 2 * 1
# base = 2, power = 1 => 2 * exponential(2,0) => 2 * 1
# base = 2, power = 0 => 1

def exponential(base, power): 
    if (power < 1):
        return 1
    return base * exponential(base, power -1)

#word = Hola, index =3, word[index] = a => a + invert_word(Hola, 2) => a + l + o + H
#word = Hola, index =2, word[index] = l => l + invert_word(Hola, 1) => l + o + H
#word = Hola, index =1, word[index] = o => o + invert_word(Hola, 0) = o + H
#word = Hola, index =0, word[index] = H => H
def invert_word(word, index):
    if index == 0:
        return word[index]
    return word[index] + invert_word(word, index - 1)

def isPrime(number, aux):
    if number <= 1:
        return False
    if number % aux == 0:
        return False
    if aux == number - 1:
        return True
    return isPrime(number, aux + 1)

def fibo(max, num1=0,num2=1):
    print(num1, end="")
    if num2>max:
        return num2
    return fibo(max,num2,num1 + num2)

def main():
    option = input("Please enter a valid option: \n1-Exponential\n2-Invert a word\n3-Valid Prime number\n4-Fibo\n->")
    if option == "1":
        result = exponential(int(input("Please enter the base: ")), int(input("Please enter the power: ")))
        print(f"The result is: {result}")
    elif option == "2":
        word = input("Please enter a word to invert: ")
        result = invert_word(word,len(word)-1)
        print(f"The result word is : {result}")
    elif option == "3":
        result = isPrime(int(input("Please enter a number to valid:")), 2)
        if result:
            print(f"The number is prime")
        else:
            print(f"The number is not prime")
    elif option == "4":
        fibo(int(input("Please enter the maximum number: ")))
        
        
main()