import builtins
import functions as do
import os
from replit import db
def start(k = "main"):
    if k == "main":
      f = open(".config/u.config")
      list = f.read().strip("entrypoints=").strip("")
    file = open(k, "r")
    c = file.readlines()
    for j in c:
      run(j.split("\n")[0])
    while True:
      cmd = input(">>  ")
      run(cmd)
def c(str, st):
  if st in str:
    return True
  return False
def run(cmd):
  a = cmd.strip("{}()").split(" ")
  b = a[0]
  ci = False
  i = b
  if c(b, "consoleINPUT"):
    b = b.replace("consoleINPUT")
    ci = True
  if b in ["True", "False"] or b[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '"', "'"]:
    b = "print"
  else:
    a.remove(a[0])
  args = ""
  cl = 1
  inqoutes = False
  lastt = False
  for i in a:
    prfs = ["add", "math", "exp"]
    mss = ["+", "-", "*", "/", "^", ">", "<"]
    if c(i, '"') or inqoutes:
      if i[len(i) - 1] == '"':
        args = args + i + ","
      else:
        args = args + i + " "
        inqoutes = True
    elif i in ["print", "variable"]:
      args = args + "do." + i + "("
      cl += 1
    elif a.index(i) != len(a) - 1 and a[a.index(i) + 1] in mss:
      e = do.math(i, a[a.index(i) + 1], a[a.index(i) + 2])
      args = args + str(e)
      a.remove(a[a.index(i) + 2])
      a.remove(a[a.index(i) + 1])
    elif a[a.index(i) - 1] == "variable":
      args = args + "'" + i + "'"
    elif b in ["variable", "math", 'min', "max",] and a.index(i) != 2:
      args = args + "'" + i + "',"
    elif b == "print" and a[0] in prfs and a.index(i) != 0 and a[1] in ["variable"] and a.index(i) != 1:
      args = args + "'" + i + "',"
    elif b == "print" and a[0] in prfs and a.index(i) != 0 and i != 'variable':
      args = args + "'" + i + "',"
    elif i in ["ask", "variable"] and a.index(i) != 0:
      args = args + "do." + i + "(" + a[a.index(i) + 1] + "),"
      a.remove(a[a.index(i) + 1])
    else:
      args = args + "do." + i + "("
      cl += 1
  newcmd = "do." + b + "(" + args + ")" * cl
  builtins.exec(newcmd)