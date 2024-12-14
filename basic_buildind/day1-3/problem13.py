print('''1: IDLY
      2: VADA
      3: DOSA
      3: PURI
      
      ENTER YOUR DISH''')
c=int(input())
r="Serving IDLY"if(c==1)else "Serving VADA"if(c==2)else "Serving DOSA"if(c==3)else "Serving PURI"if(c==3)else "You enter the incorrect dish"
print(r)