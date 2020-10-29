# nHentai collection maker by Bianca
# Inspired by RedMemz

# 'hentai' module found on PyPi.
# For installing, use 'pip install hentai'
# pypi.org/project/hentai
import hentai

def d_h(hentai = hentai.Utils.get_random_hentai()):
    hentai.download()

    return f'Downloaded {hentai}'

r = str(input('Do you want INF downloads or a limited amound (I/L)?: '))

if r == 'I' or r == 'i':
    while True:
        d_h()

elif r == 'L' or r == 'l':
    r = int(input('How much random nhentai do you need?: '))

    for i in range(r):
        d_h()

else:
    print(f'{r} isnt a valid option!')
