 
from colorama import init, Fore, Back, Style

matrix=[[1,2,3],[4,5,6],[7,8,9]]

b=Fore.BLUE
r=Fore.RED

def main():

 create_matriz(matrix)
 play()
 init()


def create_matriz(matrix):
     for m in matrix:
        print(m)
def play():
  Attempts=0
  while True:
 
    X_option=int(input(b+"X's option from 1 to 9"))
    if X_option==1 and  matrix[X_option - 1][X_option - 1] != 'O':
       matrix[X_option - 1][X_option - 1] ='X'
    elif  X_option==2 and matrix[X_option - 2][X_option - 1]!='O':
        matrix[X_option - 2][X_option - 1]="X"
    elif  X_option==3:
     matrix[X_option - 3][X_option - 1]="x" 
    elif  X_option==4:
     matrix[X_option - 3][X_option - 4]="x"  
    elif  X_option==5:
     matrix[X_option - 4][X_option - 4]="x"  
    elif  X_option==6:
     matrix[X_option - 5][X_option - 4]="x" 
    elif  X_option==7:
     matrix[X_option - 5][X_option - 7]="x" 
    elif  X_option==8:
     matrix[X_option - 6][X_option - 7]="x" 
    elif  X_option==9:
     matrix[X_option - 7][X_option - 7]="x" 
    create_matriz(matrix)
    Attempts=Attempts+1
    if Attempts==91:
        print("thanks, Good Game") 
        break
    
    
    
    O_option=int(input(r+"O's option from 1 to 9"))
    if O_option==1:
     matrix[O_option - 1][O_option - 1]='O'
    elif  O_option==2:
     matrix[O_option - 2][O_option - 1]='O'
    elif  O_option==3:
     matrix[O_option - 3][O_option - 1]='O'
    elif  O_option==4:
     matrix[O_option - 3][O_option - 4]='O'
    elif  O_option==5:
     matrix[O_option - 4][O_option - 4]='O'
    elif  O_option==6:
     matrix[O_option - 5][O_option - 4]='O'
    elif  O_option==7:
     matrix[O_option - 5][O_option - 7]='O'
    elif  O_option==8:
     matrix[O_option - 6][O_option - 7]='O'
    elif  O_option==9:
     matrix[O_option - 7][O_option - 7]='O'
    create_matriz(matrix)
    Attempts=Attempts+1
    if Attempts==8:
        print("thanks, Good Game") 
        break
    
   
  
  



if __name__ == "__main__":
    main()


