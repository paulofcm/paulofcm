import diretorio
import imagens

menu = True
while menu != 0:
    print('''
    0 - Sair. 
    1 - Criar Diretório.
    2 - Deletar Diretório
    3 - Carregar Imagem.
    4 - Deletar Imagem.
    5 - Comparar Imagens.
    6 - Achar Similaridade.
    ''')
    menu = int(input("Escolha um item do menu:"))

    if menu == 0:
        menu = False
    elif menu == 1:
        diretorio.criar_diretorio()
    elif menu == 2:
        diretorio.deletar_diretorio()
    elif menu == 3:
        imagens.carregar_imagens()
    elif menu == 4:
        imagens.deletar_imagens()
    elif menu == 5:
        imagens.comparar_imagens()
    elif menu == 6:
        imagens.achar_similaridade()

