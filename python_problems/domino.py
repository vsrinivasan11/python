f = open('domino-input.txt','r')
numDominos = f.readline()

dominoList = []
for line in f:
    currentLine = line.split(' ')
    domino = [int(e) for e in currentLine]
    dominoList.append(domino)

print dominoList

# for output
#fo = open('domino-output.txt', 'w')

# now logic
############## some useful functions ####################
def checkMatchExists(index):
    domino = dominoList[index]
    answer = False

    for j in range(len(dominoList)):
        if j == index: # so we don't check domino against itself
            continue
        currentDomino = dominoList[j] # any other domino
        if domino[0] in currentDomino or domino[1] in currentDomino:
            #match exists
            answer = True
            break

    return answer

def checkSingleMatch(index):
    domino = dominoList[index]
    answer = False

    for j in range(len(dominoList)):
        if j == index: # so we don't check domino against itself
            continue
        currentDomino = dominoList[j] # any other domino
        #first, check xor (single) match
        if domino[0] in currentDomino != domino[1] in currentDomino:
            #match exists
            answer = True
        else:
            #else, either 0 or both match, so change answer back
            answer = False
    return answer

def findMatches(index):
    domino = dominoList[index]
    matches = []

    for j in range(len(dominoList)):
        if j == index:
            continue
        currentDomino = dominoList[j]
        if domino[0] in currentDomino or domino[1] in currentDomino:
            matches.append(j)

    return matches

############ checking unsolvability conditions ##############
solvable = True

# check first condition
for i in range(len(dominoList)):
    if not checkMatchExists(i):
        solvable = False
        print 'unsolvable'
        #fo.write('unsolvable')
        #fo.close()
        break

# 2nd condition: >2 single-matched dominos
numSinglyMatched = 0
for i in range(len(dominoList)):
    if checkSingleMatch(i):
        numSinglyMatched += 1
if numSinglyMatched > 2:
    solvable = False
    print 'unsolvable'


############### solving logic #####################
def dfs(start, stack=None, visited=None):
    if visited is None:
        visited = []
    if stack is None:
        stack = []

    visited.append(start)
    stack.append(start)
    //TODO
    matchList = findMatches(start)
    if len(matchList) > 0:
        for match in matchList:
            dfs(match, visited)

if solvable:
    startDominoIndex = None
    for i in range(len(dominoList)):
        if checkSingleMatch(i):
            startDominoIndex = i
            break

    # now do the depth-first search
    hasAnswer = False



