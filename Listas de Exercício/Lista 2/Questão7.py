estoque = int(input('Quantidade de Coca-Cola em estoque: '))
estoque_max = int(input('Quantidade máxima de Coca-Cola que o estoque suporta: '))
estoque_min = int(input('Quantidade minims de Coca-Cola para o estoque funcionar: '))
quantidade_media = (estoque_max + estoque_min) / 2

if quantidade_media >= estoque:
    print('Não é necessário comprar mais Coca-Cola.')
else:
    print('É necessário compar mais Coca-Cola.')