#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   haya14busa
# URL:      http://haya14busa.com
# License:  MIT License
# Created:  2013-10-31
#

import sys

class Hanoi():
    def __init__(self, towerSize):
        self.towerSize = towerSize
        self.bars = [
                #range(start, stop = None, step = 1)
                range(towerSize, 0, -1), # range(
                [],
                []
        ]
        self.barnames = ['A','B','C']
        self.step = 0
        # Display Option
        self.dispStep      = 1
        self.dispOperation = 1
        self.dispList      = 1
        self.dispVisual    = 0

    ''' View '''
    def show(self, from_, to):
        if self.dispStep == 1:
            self.showStep()
        if self.dispOperation == 1:
            self.showOperation(from_, to)
        if self.dispList == 1:
            self.showList()
        if self.dispVisual == 1:
            self.showVisual()

    def showOperation(self, from_, to):
        print '{from_} -> {to}'.format(
                from_=self.barnames[from_],to=self.barnames[to])
    def showVisual(self):
        pass
    def showList(self):
        for i in xrange(3):
            print '{name} : {content}'.format(
                    name=self.barnames[i],
                    content=self.bars[i])
    def showStep(self):
        print '### Step : {step} ###'.format(step=self.step)
    ''' End of View '''

    def start(self):
        self.showList()
        self.solve(self.towerSize,0,1,2)

    def move(self, from_, to):
        self.bars[to].append(
                self.bars[from_].pop()
        )
        self.step += 1
        self.show(from_, to)

    def solve(self, n, from_, to, via):
        ''' Solve Tower Of Hanoi '''
        if n == 0:
            # Do Nothing
            pass
        else:
            # Solve & Move (n-1) Tower to Via
            self.solve(n-1, from_, via, to)

            # Move bottom to Destination
            self.move(from_, to)

            # Move (n-1) Tower to Destination from Via
            self.solve(n-1, via , to, from_)

def getHanoiSize():
    if(len(sys.argv) > 1 and sys.argv[1] > 0):
        try:
            return int(sys.argv[1])
        except ValueError:
            print 'Oops! That was no valid number.'
            return inputHanoiSize()
    else:
        return 3
def inputHanoiSize():
    while True:
        try:
            size = int(raw_input('Plese input valid number: '))
            if size > 0:
                return size
            else:
                print 'Hanoi size must be Natural Number'
                continue
        except ValueError:
            print 'Oops! That was no valid number. Try again...'

if __name__ == '__main__':
    size = getHanoiSize()
    hanoi = Hanoi(size)
    hanoi.start()
