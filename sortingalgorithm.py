    sortedlist = []
    
    def sortTreasures():
        if 'Bronze' in listtreasure:
            sortedlist.append('Bronze')
            listtreasure.pop(listtreasure.index('Bronze'))
            sortTreasures()
        if 'Silver' in listtreasure:
            sortedlist.append('Silver')
            listtreasure.pop(listtreasure.index('Silver'))
            sortTreasures()
        if 'Gold' in listtreasure:
            sortedlist.append('Gold')
            listtreasure.pop(listtreasure.index('Gold'))
            sortTreasures()
        if 'Platinum' in listtreasure:
            sortedlist.append('Platinum')
            listtreasure.pop(listtreasure.index('Platinum'))
            sortTreasures()
        if 'Diamond' in listtreasure:
            sortedlist.append('Diamond')
            listtreasure.pop(listtreasure.index('Diamond'))
            sortTreasures()

    
    while len(listtreasure)>0:
        sortTreasures()

    pygame.draw.rect(screen, WHITE, (120,580,500,100))
    screen.blit(font2.render(str(sortedlist), True, BLACK),(120,580))
