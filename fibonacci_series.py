import matplotlib.pyplot as plt

N = int(input("Enter required no. of terms: "))

def Fibonacci(N):
    
    starting_sequence = [0, 1]
    
    for i in range(2, N):
        next_number = starting_sequence[-1] + starting_sequence[-2]
      
        starting_sequence.append(next_number)
    
    return starting_sequence

print(Fibonacci(N))

plt.plot(Fibonacci(N))
plt.title("Fibonacci_Series")

plt.show()