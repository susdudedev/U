import builtins
import loader
inglobals = {}
def execfile(k):
  loader.start(k)
def ci(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
def print(a):
  builtins.print(a)
def ask(a):
  return builtins.input(a + ": ")
def math(a = 0, symbol = 0 ,b = False) :
  if symbol == "+":
    return add(a, b)
  elif symbol == "-":
    return subtract(a, b)
  elif symbol == "*":
    return multiply(a, b)
  elif symbol == "/":
    return divide(a, b)
  elif symbol == "^":
    return exp(a, b)
  elif symbol == ">":
    return gt(a, b)
  elif symbol == "<":
    return lt(a, b)
def variable(name, eqaul = 100, value = 100):
  if eqaul != 100:
    builtins.globals()["in" + name] = value
    inglobals[name] = value
    print(value)
  else:
    return builtins.globals()["in" + name]
def min(a = 0, b = 0):
  return builtins.min(a, b)
def max(a = 0, b = 0):
  return builtins.max(a, b)
def add(a = 0, symbol = 0 ,b = False) :
  if b == False:
    b = symbol
  if ci(a) == True or a == '0':
    a = int(a)
  if ci(b) == True or b == '0':
    b = int(b)
  return a + b
def subtract(a = 0, symbol = 0 ,b = False) :
  if b == False:
    b = symbol
  a = int(a)
  b = int(b)
  return a - b
def multiply(a = 0, symbol = 0 ,b = False) :
  if b == False:
    b = symbol
  if ci(a) == True or a == '0':
    a = int(a)
  if ci(b) == True or b == '0':
    b = int(b)
  return a * b
def divide(a = 0, symbol = 0 ,b = False) :
  if b == False:
    b = symbol
  a = int(a)
  b = int(b)
  return a / b
def exp(a = 0, symbol = 0 ,b = False) :
  if b == False:
    b = symbol
  a = int(a)
  b = int(b)
  return a ** b
def gt(a = 0, symbol = 0 ,b = False) :
  if b == False:
    b = symbol
  a = int(a)
  b = int(b)
  return a > b
def lt(a = 0, symbol = 0 ,b = False) :
  if b == False:
    b = symbol
  a = int(a)
  b = int(b)
  return a < b
def pyglobals():
  print(builtins.globals())
def globals():
  print(inglobals)
def copyright():
  print("Python's modified copyright info is below, if you use U please give credit")
  print(builtins.copyright())
def exec(str):
  loader.run(str)