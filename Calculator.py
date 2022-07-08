def calculator():
  first = float(input("What is your first number?: "))
  flag = True
  flags = True
  operation = ['+', '-', '*', '/']
  def calc(f, n):
    if op == '+':
      result = f + n
      return result
    if op == '-':
      result = f - n
      return result
    if op == '*':
      result = f * n
      return result
    if op == '/':
      result = f / n
      return result
  for n in operation:
    print(n)
  while flag is True:
    op = input("Pick an operation: ")
    next = float(input("What's the next number?: "))
    if flags is True:
      result = calc(first, next)
      print(f"The result is: {result}")
    elif flags is False:
      result = calc(result, next)
      print(f"The result is: {result}")
    extra = input(f"Type 'y' to continue calculating with {result}, "
                  f"or type 'n' to start a new calculation, or type 'e' to exit calculation: ").lower()
    if extra == 'y':
      flags = False
    elif extra == 'n':
      flag = False
      calculator()
    elif extra == 'e':
      flag = False
calculator()
