while True:
    print('Hallo komisches Wesen, ich bin ein Alien. Um genau zu sein Alien, das Alien.')
    print('Ich habe mich dir vorgestellt, also sei nicht respektlos und sage mir deinen Namen.')

    name = input('Sage dem unfreundlichen Alien namens "Alien" deinen Namen.\n')

    if name == 'Alien':
        print('Hey, ich merke sofort, wenn du lügst. Mein Name ist nämlich schon Alien, das Alien.')
        name = input('Sage mir jetzt deinen richtigen Namen!\n')
    else:
        print('Hallo', name)

    erklaerung = input('Jetzt erklär mir mal, was das für ein komischer Name ist.\n')

    print(erklaerung + '...', 'interessante Aussage. Von welcher Art bist du denn?')

    art = input('Sag dem Alien von welcher Art du bist (Es mag es, wenn man ihm NUR die Art sagt. Achte auf Groß- und Kleinschreibung.)\n')

    if art == 'Alien':
        print('Du siehst aber nicht so aus wie ich.')
    else:
        print('Ich habe noch nie davon gehört.')

    beenden = input('Willst du das Programm beenden? (ja/nein)\n')

    if beenden == 'ja':
        break
