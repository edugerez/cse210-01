 
from sre_compile import isstring
from tkinter import N
from token import AT
from tokenize import Number



#I start creating a list as a global variable to be use in all the functions
matrix=[[1,2,3],[4,5,6],[7,8,9]]

# I try to make the colors to be funnier
b="\033[34m"
c0="\033[0m"
y="\033[33m"
r="\033[31m"
back="\033[32;47m"

def main():
  attemps=0
  create_matriz(matrix)
  while True:
   attemps=attemps+1
   play_x()
   if 'X'== matrix[0][0] and 'X'== matrix[0][1] and 'X'== matrix[0][2] or 'X'== matrix[1][0] and 'X'== matrix[1][1] and 'X'== matrix[1][2] or 'X'== matrix[2][0] and 'X'== matrix[2][1] and 'X'== matrix[2][2]:   
    print(back+'X Wins'+c0)
    break
   elif 'X'== matrix[0][0] and 'X'== matrix[1][0] and 'X'== matrix[2][0] or 'X'== matrix[0][1] and 'X'== matrix[1][1] and 'X'== matrix[2][1] or 'X'== matrix[0][2] and 'X'== matrix[1][2] and 'X'== matrix[2][2]:
    print(back+'X Wins'+c0)
    break
   elif 'X'== matrix[0][0] and 'X'== matrix[1][1] and 'X'== matrix[2][2] or 'X'== matrix[2][0] and 'X'== matrix[1][1] and 'X'== matrix[0][2]:
    print(back+'X Wins'+c0)
    break


   play_o()
   if 'O'== matrix[0][0] and 'O'== matrix[0][1] and 'O'== matrix[0][2] or 'O'== matrix[1][0] and 'O'== matrix[1][1] and 'O'== matrix[1][2] or 'O'== matrix[2][0] and 'O'== matrix[2][1] and 'O'== matrix[2][2]:   
    print(back+'O Wins'+c0)
    break
   elif 'O'== matrix[0][0] and 'O'== matrix[1][0] and 'O'== matrix[2][0] or 'O'== matrix[0][1] and 'O'== matrix[1][1] and 'O'== matrix[2][1] or 'O'== matrix[0][2] and 'O'== matrix[1][2] and 'O'== matrix[2][2]:
    print(back+'O Wins'+c0)
    break
   elif 'O'== matrix[0][0] and 'O'== matrix[1][1] and 'O'== matrix[2][2] or 'O'== matrix[2][0] and 'O'== matrix[1][1] and 'O'== matrix[0][2]:
    print(back+'O Wins'+c0)
    break
   else: 
    if attemps>4:
      print(r+'Game Over'+c0)
   




# this fucntion should be creating a new matrix in list all the time acording to the input from users.
def create_matriz(matrix):
     for m in matrix:
        print(m)


def play_x():
 while True:
  try:
    X_option=int(input(b+"X's option from 1 to 9"+c0))
    if X_option == X_option>9 or X_option<1:
     print(r+'You have to enter a number from 1 to 9 position, Tray again!'+c0)
     continue
  except ValueError:
    print(r+'enter a number please'+c0)
    continue
  if X_option==1 and  matrix[X_option - 1][X_option - 1]!= 'O':
       matrix[X_option - 1][X_option - 1] ='X'

  elif  X_option==2 and matrix[X_option - 2][X_option - 1]!='O':
        matrix[X_option - 2][X_option - 1]='X'

  elif  X_option==3 and matrix[X_option - 3][X_option - 1]!='O':
     matrix[X_option - 3][X_option - 1]='X'

  elif  X_option==4 and matrix[X_option - 3][X_option - 4]!='O':
     matrix[X_option - 3][X_option - 4]='X'  

  elif  X_option==5 and matrix[X_option- 4][X_option - 4]!='O':
     matrix[X_option - 4][X_option - 4]='X'  

  elif  X_option==6 and matrix[X_option - 5][X_option - 4]!='O':
     matrix[X_option - 5][X_option - 4]='X' 

  elif  X_option==7 and matrix[X_option - 5][X_option - 7]!='O':
     matrix[X_option - 5][X_option - 7]='X' 

  elif  X_option==8 and matrix[X_option - 6][X_option - 7]!='O':
     matrix[X_option - 6][X_option - 7]='X' 

  elif  X_option==9 and matrix[X_option - 7][X_option - 7]!='O':
     matrix[X_option - 7][X_option - 7]='X' 
  else:
     print()
     print(r+'position already chosen, try again!'+c0)
     print()
     continue
  create_matriz(matrix)
  break

    

def play_o():
 while True:
  try:
    O_option=int(input(y+"O's option from 1 to 9"+c0))
    if O_option ==str:
     print(r+'You have to enter a number from 1 to 9 position, Tray again!'+c0)
     continue
  except ValueError:
   print(r+'enter a number please'+c0)
   continue
  if O_option==1 and  matrix[O_option - 1][O_option - 1]!= 'X':
     matrix[O_option - 1][O_option - 1]='O'

  elif  O_option==2 and matrix[O_option - 2][O_option - 1]!= 'X':
     matrix[O_option - 2][O_option - 1]='O'

  elif  O_option==3 and matrix[O_option - 3][O_option - 1]!= 'X':
     matrix[O_option - 3][O_option - 1]='O'

  elif  O_option==4 and matrix[O_option - 3][O_option - 4]!= 'X':
     matrix[O_option - 3][O_option - 4]='O'

  elif  O_option==5 and matrix[O_option - 4][O_option - 4]!= 'X':
     matrix[O_option - 4][O_option - 4]='O'

  elif  O_option==6 and matrix[O_option - 5][O_option - 4]!= 'X':
     matrix[O_option - 5][O_option - 4]='O'

  elif  O_option==7 and matrix[O_option - 5][O_option - 7]!= 'X':
     matrix[O_option - 5][O_option - 7]='O'

  elif  O_option==8 and matrix[O_option - 6][O_option - 7]!= 'X':
     matrix[O_option - 6][O_option - 7]='O'

  elif  O_option==9 and matrix[O_option - 7][O_option - 7]!= 'X':
     matrix[O_option - 7][O_option - 7]='O'
  else:
     print()
     print(r+'position already chosen, try again!'+c0)
     print()
     continue
  create_matriz(matrix)
  break


if __name__ == "__main__":
    main()


