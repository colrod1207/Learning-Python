from art import logo


def add(a, b):
  return (a + b)

def substract(a, b):
  return (a - b)

def multiply(a, b):
  return (a * b)

def divide(a, b):
  return (a/b)

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide  
}

# def operate(a, b, op):
  
#   if(op == "+"):
#     return(add(a, b))
#   if(op == "-"):
#     return(substract(a, b))
#   if(op == "*"):
#     return(multiply(a, b))
#   if (op == "/"):
#     return(divide(a, b))

def calculation():
  print(logo)
  a = input("What's the first number?: ")
  for _op in operations:
    print(_op)
  op = input("Pick an operation: ")
  b = input("What's the next number?: ")
  calculation_function = operations[op]
  result = calculation_function(float(a), float(b))
  #result = operate(int(a), int(b), (op))
  print(f"{a} {op} {b} = {result}")
  
  should_continue = True
  while (should_continue):
    _continue = input(f"Type 'y' to continue calculating with  {result}, or type 'n' to start a new calculation: ")
    if (_continue == "y"):
      a = result
      op = input("Pick an operation: ")
      b = input("What's the next number?: ")
      calculation_function = operations[op]
      result = calculation_function(int(a), int(b))
  #result = operate(int(a), int(b), (op))
      print(f"{a} {op} {b} = {result}")
    else:
      should_continue = True
      calculation()
      
    
calculation() 
  
