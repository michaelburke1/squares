#!/usr/bin/python

import os
import pydot
import sys
from random import SystemRandom

def usage(program):
    print 'Usage: {} league'.format(program)

def buildSquares(sg):
	for i in range(10):
		sg.append([]);
		for j in range(10):
			sg[i].append('');
	return sg;

def loadInSquareNames(fn, sg):
    rows = [];
    with open(fn) as f:
        for line in f:
        # strip whitespace
            line = line.strip()
        # separate the columns
            line = line.split(',')
        # save the line for use later
            currRow = [];
            for i in line:
                currRow.append(i)
            sg.append(currRow)
    return sg


def printBoard(rN, bN, sg):
    print '\t\t\t\t\t\tCINCINNATI\n',
    lenB = len(bN);
    print '\t',

    for i in range(lenB):
        print'\t',
        print bN[i],
    for x in range(10 - lenB):
        print '\t',
    print '\n',

    for x in range(2):
        print'\t',
        if x < len(rN):
            print rN[x],
        print '\t',
        for i in sg[x]:
            print i,
            print '\t',
        print '\n',

    print 'L\t',
    if 2 < len(rN):
        print rN[2],
    print '\t',
    for i in sg[2]:
        print i,
        print '\t',
    print '\n',

    print 'A\t',
    if 3 < len(rN):
        print rN[3],
    print '\t',
    for i in sg[3]:
        print i,
        print '\t',
    print '\n',

    print ' \t',
    if 4 < len(rN):
        print rN[4],
    print '\t',
    for i in sg[4]:
        print i,
        print '\t',
    print '\n',

    print 'R\t',
    if 5 < len(rN):
        print rN[5],
    print '\t',
    for i in sg[5]:
        print i,
        print '\t',
    print '\n',

    print 'A\t',
    if 6 < len(rN):
        print rN[6],
    print '\t',
    for i in sg[6]:
        print i,
        print '\t',
    print '\n',

    print 'M\t',
    if 7 < len(rN):
        print rN[7],
    print '\t',
    for i in sg[7]:
        print i,
        print '\t',
    print '\n',

    print 'S\t',
    if 8 < len(rN):
        print rN[8],
    print '\t',
    for i in sg[8]:
        print i,
        print '\t',
    print '\n',

    for x in range(1):
        print'\t',
        if x + 9 < len(rN):
            print rN[x+9],
        print '\t',
        for i in sg[x + 9]:
            print i,
            print '\t',
        print '\n',

    print '\n\n'

def play(rN, bN, cg, sg):
    print 'play'
    #val = raw_input('Auto Complete grid? (Y/N)\n');
    val = 'N';

    if val == 'Y':
        print 'Auto'
        while(1):
            if len(rN) == 10:
                break
            else:
                randN = cg.randrange(10)
                #print randN
                #print 'randN^'
                if not(randN in rN):
                    rN.append(randN)
                    #print rN
                    #print 'rN ^'
        while(1):
            if len(bN) == 10:
                break
            else:
                randN = cg.randrange(10)
                if not (randN in bN):
                    bN.append(randN)
        print rN
        print bN

    elif val == 'N':
        print 'N'
        while(1):
            if (len(rN) == 10 and len(bN) == 10):
                print 'Board is full. Congrats!\n'
                printBoard(rN, bN, sg)
                break
            clear = "\n" * 100
            print clear
            print val
            printBoard(rN, bN, sg);
            val = raw_input('Welcome to rando squares grid! Enter B for Bengals pick, R for Rams, and Ran for random (B,R,Ran)\n');
            

            if val == 'B':
                if len(bN) == 10:
                    os.system('clear')
                    val = 'You selected B. Sorry, you\' already picked all for Bengals. Select again\n'
                else:
                    while(1):
                        randN = cg.randrange(10)
                        if not(randN in bN):
                            bN.append(randN)
                            break
            elif val == 'R':
                if len(rN) == 10:
                    os.system('clear')
                    print 'You selected R. Sorry, you\' already picked all for Rams. Select again\n'
                else:
                    while(1):
                        randN = cg.randrange(10)
                        if not(randN in rN):
                            rN.append(randN)
                            break
            elif val == 'Ran':
                while(1):   
                    valN = cg.randrange(2)
                    if (valN % 2 and len(bN) != 10):
                        randN = cg.randrange(10)
                        if not(randN in bN):
                            bN.append(randN)
                            break
                    elif (valN % 2 == 0 and len(rN) != 10):
                        randN = cg.randrange(10)
                        if not(randN in rN):
                            rN.append(randN)
                            break
                    elif (len(rN) == 10 and len(bN) == 10):
                        print 'Board is full! Congrats!\n'
                        break
            else:
                print "Yo wtf, you typed nonsense, try again\n"
            print 'Rams'
            print rN
            print 'Bengals'
            print bN

                            
    else:
        print 'bruh wtf'

if __name__ == '__main__':

    mySquaresGrid = [];
    rN = [];
    bN = [];
    cg = SystemRandom();
    print cg.randrange(10)
    os.system('clear')

    if len(sys.argv) == 2:
        mySquaresGrid = loadInSquareNames(sys.argv[1], mySquaresGrid)

    if len(sys.argv) == 1:
        mySquaresGrid = buildSquares(mySquaresGrid)

    play(rN, bN, cg, mySquaresGrid)

