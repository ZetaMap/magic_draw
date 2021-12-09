from math import *
from kandinsky import *
 
def draw(index, loop):
  exec("""draw_string("{}", 5, 5, (100,100,100))
draw_string("<", 219, 200, (100,100,100))
fill_rect(220, 215, 15, 1, (100,100,100))
fill_rect(235, 216, 1, -7, (100,100,100))
fill_rect(236, 208, -15, 1, (100,100,100))
draw_string("to skip", 245, 202, (100,100,100))

for p in range({}):
  for i in range(496): 
    try: set_pixel(160+round({}), 110+round({}), 
      (cos(p)*1000,sin(i)*1000,log10(i-p)*1000))
    except KeyboardInterrupt: raise RuntimeError
    except SyntaxError: raise
    except: continue
  """.format(1+(len(_list)+index if index < 0 else index),
   loop, _list[index][0], _list[index][1]))
     
_list=[
#           for x                          for y
  ("cos(i)*111/(cos(p)+1)", "sin(i)*111/(sin(p)+1)"      ), #1
  ("cos(i)*111+p"         , "sin(i)*111+p"               ), #2
  ("cos(i)*111/(tan(p)+1)", "sin(i)*111/(sin(p)+1)"      ), #3
  ("cos(i)*111/(tan(p)+1)", "tan(i)*111/(sin(p))"        ), #4
  ("cos(i)*111/(1-cos(p)+1)", "sin(i)*111/(-sin(p)+1)"   ), #5
  ("cos(i)*111/(cos(p)+1)", "sin(i)/(sin(p)+1)"          ), #6
  ("cos(i)*111/(cos(p)+1)", "sin(i)*111/cos(p)**2"       ), #7
  ("cos(i)*111/(cos(p)+1)", "sin(i)*111/(cos(p)**2+1)"   ), #8
  ("cos(i)*111/(cos(p)+1)", "sin(i)*111/(tan(tan(p))**2)"), #9
  ("tan(tan(i))*111/sin(p)", "tan(i)*111/cos(sin(p))"    ), #10
  ("cos(i)*p"             , "sin(i)*p"                   ), #11
  ("tan(tan(i))*p"        , "sin(i)*p"                   ), #12  
  ("cos(p)*i"             , "tan(p)*i"                   ), #13
  ("tan(tan(tan(i)))/tan(p)", "tan(i)*p/sin(p)"          ), #14
  ("cos(tan(i))*p"        , "cos(i)*p"                   ), #15
  ("sin(i)*p*cos(sin(i))" , "sin(p)*111/cos(tan(i))"     ), #16
  ("cos(p)*i*tan(cos(p))-111", "cos(i)*p/tan(i)"         ), #17
  ("sin(cos(tan(p)))*i"   , "tan(i)*p"                   ), #18
  ("exp(abs(log(p)))*sin(i)", "log(p)/cos(i)*10"         ), #19
  ("exp(abs(log(p,i)))*64*sin(i)", "log(p)/cos(i)*5"     ), #20
  ("exp(abs(log(p)))*sin(i)", "sin(i)*50/sin(p)"         ), #21
  ("cos(p)*50/(sin(i)+1)" , "abs(p)/cos(i)"              ), #22
  ("asinh(p)/cos(i)"      , "cos(p)*111*sin(i)"          ), #23
  ("acosh(p)*111/(tan(i)+1)", "cos(p)*150/asinh(i)"      ), #24
  ("abs(acosh(p))/sin(i)", "acosh(p)*50/-atan(i)+125"    ), #25
  ("acosh(p)*20/(log10(i)+1)", "acosh(p)*20/cos(i)"      ), #26
]

x, loop = input("""{} equations found in the list.
Let empty to run all.
|-> """.format(len(_list))), input("""
Let empty for default value.
Loop: """)
loop = 400 if loop == '' else int(loop)
r = range(len(_list)) if x == '' else range(int(x)-1, int(x))

for ii in r:
  try: draw(ii, loop)
  except SyntaxError: raise
  except:
    try: draw(ii, 1)
    except: pass
  fill_rect(0, 0, 350, 250, (255,255,255))
draw_string("End", 5, 5, (100,100,100))
