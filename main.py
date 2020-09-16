# Author: Shang Yuan Lim szl6038@psu.edu

def digit_sum(n):
  if n <= 9:
    return n
  else:
    return n%10 + digit_sum(n//10)
    
    
def run():
  value = input("Enter an int: ")

  value = int(value)

  n = digit_sum(value)

  print(f"sum of digits of {value} is " + str(n) + ".")

if __name__ == "__main__":
  run ()

 