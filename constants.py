mainFont = (0, 0, 0, 255)
urlBasic = 'https://api.genderize.io?name={personName}'
fntSrc = "Fonts/LovelyBalloon.ttf"
wishes1_1 = 'Happy birthday\nto one of the\n'
wishes1_2 = 'most special people\nin my life!'
wishes2_1 = 'Today we\ncelebrate you!\n'
wishes2_2 = 'Happy birthday to\na wonderful person'
wishes3_1 = 'Wishing you a\nfantastic birthday\nand wonderful'
wishes3_2 = '\n year ahead.\n \nMake every \nday count!'

backgroundImages = {
    'buffer':
        {"source": "no",
         "gender": "no"},
    'back_1':
        {"source": "Background_imgs/back_1.jpg",
         "gender": "female"},
    'back_2': {
        "source": "Background_imgs/back_2.jpg",
        "gender": "female"},
    'back_3': {
        "source": "Background_imgs/back_3.jpg",
        "gender": "female"},
    'back_4': {
        "source": "Background_imgs/back_4.jpg",
        "gender": "female"},
    'back_5': {
        "source": "Background_imgs/back_5.jpg",
        "gender": "female"},
    'back_6': {
        "source": "Background_imgs/back_6.jpg",
        "gender": "unisex"},
    'back_7': {
        "source": "Background_imgs/back_7.jpg",
        "gender": "unisex"},
    'back_8': {
        "source": "Background_imgs/back_8.jpg",
        "gender": "unisex"},
    'back_9': {
        "source": "Background_imgs/back_9.jpg",
        "gender": "male"},
    'back_10':
        {"source": "Background_imgs/back_10.jpg",
         "gender": "male"},
    'back_11':
        {"source": "Background_imgs/back_11.jpg",
         "gender": "male"},
    'back_12':
        {"source": "Background_imgs/back_12.jpg",
         "gender": "male"},
}


Wishes = {
    'buffer': {
        'gender': 'buffer'
    },
    'wishes1': {
        'text': f'{wishes1_1}{wishes1_2}',
        'gender': 'unisex',
        'fntSize': 60,
        'shadowColor': (244, 164, 96, 255)
    },
    'wishes2': {
        'text': f'{wishes2_1}{wishes2_2}',
        'gender': 'female',
        'fntSize': 55,
        'shadowColor': (238, 130, 238, 255)
    },
    'wishes3': {
        'text':  f'{wishes3_1}{wishes3_2}',
        'gender': 'male',
        'fntSize': 55,
        'shadowColor': (135, 206, 250, 255)
    }
}

Frames = {
    "buffer": {
        "source": "no",
        "gender": "no"},
    "frame_1": {
        "source": "Frames/frame_1.png",
        "gender": "unisex"},
    "frame_2": {
        "source": "Frames/frame_2.png",
        "gender": "male"},
    "frame_3": {
        "source": "Frames/frame_3.png",
        "gender": "female"},
    "frame_4": {
        "source": "Frames/frame_4.png",
        "gender": "unisex"}
}
