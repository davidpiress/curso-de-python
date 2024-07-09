for i in range(10):
    if i == 2:
        print('pulou o 2 ')
        print('continue pula sempre que for True o if')
        continue
    if i == 8:
        print('sera finalizado')
        
    for j in range(1,4):
        print(i, j)
else:
    print('foi completo com sucesso')