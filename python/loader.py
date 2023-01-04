import builtins
import functions as do
def start(k = "main.u"):
  for j in open(k, "r").readlines():
    run(j.strip("\n"))
  while True:
    cmd = input(">>  ")
    run(cmd)
def c(str, st):
  return st in str
def run(cmd):
  a = cmd.strip(")").split(" ")
  b = a[0]
  a.remove(b)
  args = ""
  cl = 1
  inqoutes = False
  prfs = ["add", "math", "exp"]
  mss = ["+", "-", "*", "/", "^", ">", "<"]
  for i in a:
    ai = a.index(i)
    if c(i, '"') or inqoutes:
      if i[len(i) - 1] == '"':
        args += f'{i},'
      else:
        args += f'{i} '
        inqoutes = True
    elif i in ["print", "variable", "ask"]:
      args += f"do.{i}("
      cl += 1
    elif a[ai - 1] in ["print", "variable", "ask"]:
      args += f"'{i}'"
    elif ai != len(a) - 1 and a[ai + 1] in mss and a[len(a) - 1] not in mss:
      e = do.math(i, a[ai + 1], a[ai + 2])
      args += str(e)
      a.remove(a[ai + 2])
      a.remove(a[ai + 1])
    elif (b == "print" and a[0] in prfs and ((ai not in [0, 1] and a[1] == "variable") or (ai != 0 and i != 'variable'))) or b in ["variable", "math", 'min', "max",] and ai(i) != 2:
      args += f"'{i}',"
    elif i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
      args += i
    else:
      args += f"do.{i}("
      cl += 1
  newcmd = f"do.{b}({args}{')' * cl}"
  print(newcmd)
  builtins.exec(newcmd)