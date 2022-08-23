from PIL import Image
import os

image1 = Image.open('maya.jpg')

# Mostra a imagem
image1.show()

# Salva no mesmo diretório do script a imagem, percebe-se que dá pra mudar a extensão sem problema
image1.save('maya.png')

# Mostra as imagens do diretório especificado
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        print(f)
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save(f'img/{fn}.png')
