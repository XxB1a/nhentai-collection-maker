# nHentai collection maker by Bianca
# Inspired by RedMemz

# 'hentai' module found on PyPi.
# For installing, use 'pip install hentai'
# pypi.org/project/hentai
from sys import argv as argument
from hentai import Utils

def d_h(hentais = None):
    hentai = Utils.get_random_hentai()

    if hentais == None:
        try:
            print(f'Downloading {hentai}')
            hentai.download()
        except:
            print(f'Downloading hentai FAILED!')

    else:
        try:
            print(f'#{hentais} | Downloading {hentai}')
            hentai.download()
        except:
            print(f'Downloading hentai #{hentais} FAILED')

if argument[1] == None or argument[1] == 'I' or argument[1] == 'i':
    hentais = 0

    while True:
        hentais = hentais + 1
        d_h(hentais)

elif argument[1] == 'l' or argument[1] == 'l':
    hentais = 0

    for range in range(int(argument[2])):
        hentais = hentais + 1
        d_h(hentais)

else:
    r = str(input('Do you want INF downloads or a limited amound (I/L)?: '))

    if r == 'I' or r == 'i':
        hentais = 0

        while True:
            hentais = hentais + 1
            d_h(hentais)

    elif r == 'L' or r == 'l':
        r = int(input('How much random nhentai do you need?: '))

        for i in range(int(r)):
            hentais = hentais + 1
            d_h(hentais)

    else:
        print(f'{r} isnt a valid option!')
