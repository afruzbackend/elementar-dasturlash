"""Shu nusxadagi darslik (fan) ma'lumotlari.

Boshqa fan uchun sayt yasashda loyiha nusxalanadi va faqat shu fayl hamda data/maruza.docx almashtiriladi:
bo'limlar, har bir mavzuning 3D ko'rgazmasi, muallif va YouTube video darslari shu yerda.
"""
from pathlib import Path

SLUG = 'elementar-dasturlash'   # docx dagi fan nomidan: «Elementar dasturlash»
AUTHOR = 'Oydin Tashtemirova'

IMG = Path(__file__).resolve().parent / 'static' / 'lectures' / 'img'
PHOTO = IMG / 'muallif.jpg'   # ustoz (portret)
COVER = IMG / 'muqova.jpg'    # bosh sahifa foni: ustoz dars o'tayotgan payt

# (bo'lim nomi, birinchi mavzu, oxirgi mavzu, rang, belgi)
PARTS = [
    ('Algoritmlash asoslari', 1, 3, '#C2562D', 'layers'),
    ('Python tili va o‘zgaruvchilar', 4, 7, '#0E7C7B', 'hash'),
    ('Kiritish-chiqarish va operatorlar', 8, 12, '#9E2A3A', 'target'),
    ('Shart va takrorlash operatorlari', 13, 21, '#24508F', 'refresh'),
    ('Xatolarni aniqlash va tuzatish', 22, 26, '#B07D1E', 'wrench'),
    ('Algoritmdan tayyor dasturgacha', 27, 30, '#3F7D4E', 'graduation'),
]

# mavzu raqami -> 3D ko'rgazma (lectures/scenes.py)
SCENES = {
    1: 'flow', 2: 'gear', 3: 'flow', 4: 'code', 5: 'monitor', 6: 'vars', 7: 'vars', 8: 'monitor', 9: 'code',
    10: 'ops', 11: 'ops', 12: 'branch', 13: 'branch', 14: 'code', 15: 'branch', 16: 'loop', 17: 'loop',
    18: 'loop', 19: 'gear', 20: 'branch', 21: 'ops', 22: 'bug', 23: 'bug', 24: 'pulse', 25: 'bug', 26: 'tools',
    27: 'flow', 28: 'code', 29: 'pulse', 30: 'monitor',
}

# mavzu raqami -> [(YouTube video ID, tili)]   tanlov: mavzuga mosligi, o'zbek tilidagilar birinchi
VIDEOS = {
    1: [('RrgmcE8mX0Q', 'uz'), ('WaNVfuHXxhw', 'uz'), ('X74vxH4GtgE', 'uz')],
    2: [('cpmcazIZS0o', 'uz'), ('NMETWvjb1yA', 'uz'), ('XxmZApILYZg', 'uz')],
    3: [('Kru5EkEaff0', 'uz'), ('dhIRRd8UiRg', 'uz'), ('XgryIjomW5g', 'uz')],
    4: [('7jjlMEcQYyI', 'uz'), ('Th2ESF-T0_U', 'uz'), ('ZIWnJNbTlkE', 'uz')],
    5: [('ABgjR9dNPVU', 'uz'), ('uBysPnOoO5U', 'uz'), ('dguiNk8eHPY', 'uz')],
    6: [('aCrFMSOGLFI', 'uz'), ('oM8f4xa4AJ8', 'uz'), ('Hyw7CGz6wm8', 'uz')],
    7: [('Q3H1OUj_XU8', 'uz'), ('c3MY2cUQa8c', 'uz'), ('OmZvDXOrC1c', 'ru')],
    8: [('cok0xiUIG7g', 'uz'), ('AOBGwC52B0Y', 'uz'), ('MqvrE0___DI', 'uz')],
    9: [('5poQckSAyPU', 'uz'), ('rzWk17_MBz4', 'uz'), ('DB9Cq6TSTuQ', 'en')],
    10: [('uhOI-zY-5AY', 'uz'), ('l3pZd0zZPns', 'uz'), ('_Dco_yWOWjs', 'uz')],
    11: [('djtv5NMIBSY', 'uz'), ('9UlEebmqKpQ', 'uz'), ('htRlbsGnlJI', 'uz')],
    12: [('lLAWjm6wvx0', 'uz'), ('Knttuj9BlkI', 'uz'), ('MZWQHiFCCqY', 'uz')],
    13: [('xWhTF00jyvs', 'uz'), ('fXgMxeir2VE', 'uz'), ('suDnCccsXkc', 'uz')],
    14: [('evTa5bQ393A', 'uz'), ('2Qka5TH4dK8', 'uz'), ('FvMPfrgGeKs', 'en')],
    15: [('QH5Q_dyj3dI', 'uz'), ('PQTJT44_5L8', 'uz'), ('QSQ4JWqKBYk', 'uz')],
    16: [('p31oOSeQvE0', 'uz'), ('2eNHjdiS3mw', 'uz'), ('vMD6-jzgDvI', 'ru')],
    17: [('982dbRh0Efg', 'uz'), ('Q5V1H2Bbwy8', 'uz'), ('z0dA5EuQhCo', 'uz')],
    18: [('Wpp6tXpMGgM', 'uz'), ('LneKLfVrqis', 'uz'), ('ibnZpOfp7aQ', 'uz')],
    19: [('hYlKO_pSCHM', 'uz'), ('ny5w4-2BQlI', 'uz'), ('A_MGbcYzdcc', 'uz')],
    20: [('S0PgNUZDFZc', 'uz'), ('WIJaaDi2QkE', 'uz'), ('97NdNoA3XUQ', 'en')],
    21: [('n0vqVJWefbU', 'uz'), ('nn91xKyVzJo', 'uz'), ('YYF0mfa-EAU', 'uz')],
    22: [('Zp8hhWN_qwQ', 'uz'), ('Ybm7fJewzDk', 'uz'), ('ToPP5UGgJUM', 'en')],
    23: [('-fpxjTiQ9-k', 'uz'), ('7BNI4r-LHzQ', 'ru'), ('dIwYoA77dJo', 'en')],
    24: [('UIfY8CpC8Ic', 'uz'), ('QIhoaxSHvwg', 'ru'), ('XMhR40LZz9k', 'en')],
    25: [('e8772EBMS50', 'uz'), ('67BjHoN-VKg', 'en'), ('JG1livF44_E', 'en')],
    26: [('xgXGCaMX_sY', 'uz'), ('YPoyHMAUQnc', 'uz'), ('P22Abeloyhw', 'uz')],
    27: [('oPVp3OJhgH0', 'uz'), ('ws5jEhs3ZCA', 'uz'), ('Gn7tvLGqyXg', 'uz')],
    28: [('ixc2mq0FKHA', 'uz'), ('fSyt94R5tlY', 'uz'), ('fj_GLU344bQ', 'uz')],
    29: [('cDBg16PRvDU', 'uz'), ('WSabR3CC3Fo', 'uz'), ('96mDQrlceEk', 'en')],
    30: [('wdnXs41EgxI', 'uz'), ('p_zRQcMeXVM', 'uz'), ('qW11HgDmhuI', 'uz')],
}

# Qo'shimcha materiallar: (mavzu raqami yoki None — butun darslik uchun, nomi, havola yoki data/materiallar/ dagi fayl, izoh)
MATERIALS = [
    (None, 'Python: qisqa ma’lumotnoma', 'python-qisqa-malumotnoma.pdf',
     'Kiritish-chiqarish, turlar, operatorlar, shart, takrorlash va ko‘p uchraydigan xatolar — 2 bet'),
    (None, 'Blok-sxema: belgilar va algoritm tuzish tartibi', 'blok-sxema-qollanma.pdf',
     'Belgilar jadvali, namunaviy blok-sxemalar va ularning Python kodi'),
    (None, 'Amaliy mashqlar to‘plami (30 ta masala)', 'amaliy-mashqlar.pdf',
     'Mavzular bo‘yicha masalalar, tekshirish qiymatlari bilan'),
    (None, 'Python rasmiy qo‘llanmasi (The Python Tutorial)', 'https://docs.python.org/3/tutorial/index.html',
     'docs.python.org · ingliz tilida, brauzerda tarjima qilish mumkin'),
    (None, 'Onlayn Python kompilyatori', 'https://www.programiz.com/python-programming/online-compiler/',
     'Kompyuterga hech narsa o‘rnatmasdan, brauzerda kod yozib ishga tushirish'),
    (3, 'diagrams.net — blok-sxema chizish', 'https://app.diagrams.net/',
     'Bepul onlayn dastur: oval, romb, parallelogramm va strelkalar tayyor'),
    (4, 'Python sintaksisi va birinchi qadamlar', 'https://docs.python.org/3/tutorial/introduction.html',
     'Rasmiy qo‘llanma: sonlar, satrlar, birinchi dasturlar'),
    (5, 'Python’ni yuklab olish (python.org)', 'https://www.python.org/downloads/',
     'Rasmiy sayt · o‘rnatishda «Add python.exe to PATH» belgisini qo‘ying'),
    (5, 'Thonny — boshlang‘ichlar uchun Python muhiti', 'https://thonny.org/',
     'Bepul, oddiy interfeys, o‘zgaruvchilar oynasi va qadamma-qadam debugger'),
    (5, 'PyCharm Community — dasturlash muhiti', 'https://www.jetbrains.com/pycharm/download/',
     'Bepul Community versiyasi · kodni tekshirish va avtomatik to‘ldirish'),
    (5, 'Visual Studio Code', 'https://code.visualstudio.com/',
     'Bepul muharrir · Python kengaytmasi bilan ishlatiladi'),
    (6, 'Python bo‘yicha interaktiv darslar (W3Schools)', 'https://www.w3schools.com/python/',
     'O‘zgaruvchilar, turlar, operatorlar — har bir misolni saytning o‘zida sinash mumkin'),
    (8, 'Kiritish va chiqarish (rasmiy qo‘llanma)', 'https://docs.python.org/3/tutorial/inputoutput.html',
     'print(), f-satrlar va natijani chiroyli chiqarish'),
    (11, 'Python’ning tayyor funksiyalari', 'https://docs.python.org/3/library/functions.html',
     'abs(), round(), min(), max(), int(), float(), input(), print() va boshqalar'),
    (21, 'Amallarning bajarilish tartibi (operator precedence)', 'https://docs.python.org/3/reference/expressions.html#operator-precedence',
     'Rasmiy jadval: ** dan or gacha'),
    (13, 'Shart va takrorlash operatorlari (rasmiy qo‘llanma)', 'https://docs.python.org/3/tutorial/controlflow.html',
     'if, for, range(), break va continue — misollar bilan'),
    (22, 'Xatolar va istisnolar (rasmiy qo‘llanma)', 'https://docs.python.org/3/tutorial/errors.html',
     'SyntaxError, xato xabarini o‘qish, try-except'),
    (24, 'Python Tutor — kodni qadamma-qadam ko‘rish', 'https://pythontutor.com/visualize.html',
     'Har qadamda o‘zgaruvchilar qiymatini ko‘rsatadi — mantiqiy xatoni topishga qulay'),
    (27, 'Flowgorithm — blok-sxemadan dastur', 'http://www.flowgorithm.org/',
     'Blok-sxemani chizib, uni ishga tushirish va Python kodiga o‘girish mumkin'),
    (28, 'PEP 8 — Python kodini yozish uslubi', 'https://peps.python.org/pep-0008/',
     'Nomlash, chekinish va bo‘shliqlar bo‘yicha rasmiy tavsiyalar'),
    (30, 'Robocontest.uz — masalalar to‘plami', 'https://robocontest.uz/',
     'O‘zbek tilidagi dasturlash masalalari, yechim avtomatik tekshiriladi'),
]
