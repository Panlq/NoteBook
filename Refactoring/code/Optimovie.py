#!/usr/bin/python3
# -*- coding:utf-8 –*-


"""
顾客租赁, 租了那些影片, 租期多长, 程序根据租赁时间和影片类型算出费用,
影片分类 普通, 儿童, 新片, 除了计算费用, 还要为常客累计积分(积分根据租片种类是否为新片而有不同)
"""

"""
1. 功能归属明确
    Move Method, Move Field, Extract Class 抽离/封装
2. Replace Temp with Query() 以查询取代临时变量
3. Inline Temp   临时变量内联化
"""


from baseClass import AbcMovie, ChildrenPrice, NewReleasePrice, RegularPrice


class Movie(object):
    def __init__(self, title, price):
        self._title = title
        self._price = price()

    def getPriceCode(self):
        return self._price.getPriceCode()

    def setPriceCode(self, arg):
        if arg == AbcMovie.REGULAR:
            self._price = RegularPrice()
        elif arg == AbcMovie.CHILDRENS:
            self._price = ChildrenPrice()
        elif arg == AbcMovie.NEW_RELAEASE:
            self.price = NewReleasePrice()
        else:
            raise ValueError

    def getTitle(self):
        return self._title

    def getCharge(self, daysRented):
        return self._price.getCharge(daysRented)

    def getFrequentRenterPoints(self, daysRented):
        return self._price.getFrequentRenterPoints(daysRented)


class Rental(object):
    def __init__(self, movie, daysRented):
        self._movie = movie
        self._daysRented = daysRented

    def getDaysRented(self):
        return self._daysRented

    def getMovie(self):
        return self._movie

    def getCharge(self):
        return self._movie.getCharge(self._daysRented)    

    def getFrequentRenterPoints(self):
        return self._movie.getFrequentRenterPoints(self._daysRented)


class Customer(object):
    def __init__(self, name):
        self._name = name
        self._totalCharge = 0
        self._frequentRenterPoints = 0
        self._rentals = []

    def addRental(self, arg):
        self._rentals.append(arg)

    def getName(self):
        return self._name

    def getTotalCharge(self):
        pass

    def getTotalFrequentRenterPoints(self):
        pass

    def statement(self):
        result = f'Rental Recora for {self.getName()} \n'
        for rental in self._rentals:
            thisAmount = rental.getCharge()
            movieTitle = rental.getMovie().getTitle()
            self._frequentRenterPoints += rental.getFrequentRenterPoints()
            # show figures for this rental
            result += f'\t {movieTitle} \t {thisAmount} \n'
            self._totalCharge += thisAmount
        # add footer lines
        result += f'Amount owed is {self._totalCharge} \n'
        result += f'You earned {self._frequentRenterPoints} frequent renter points'
        return result

    def htmlStatement(self):
        result = f'<H1>Rental for <EM> {self.getName()} </EM></H1><P>\n;'
        for rental in self._rentals:
            result += rental.getMovie().getTitle() + ': ' + str(rental.getCharge()) + '<BR>\n'
            result += f'<P>You own <EM>{self._totalCharge}</EM><P>\n'
            result += f'On this rental you earned <EM>{self._frequentRenterPoints}</EM> frequent renter points<P>' 
        return result


if __name__ == '__main__':
    ha = Movie('Dream1', ChildrenPrice)
    hb = Movie('Dream2', NewReleasePrice)
    hc = Movie('Dream3', ChildrenPrice)
    hd = Movie('Dream4', RegularPrice)
    he = Movie('Dream5', RegularPrice)
    hf = Movie('Dream6', NewReleasePrice)
    a = Customer('Mark')
    b = Customer('Jon')
    c = Customer('Jack')
    a.addRental(Rental(ha, 3))
    a.addRental(Rental(hb, 5))
    c.addRental(Rental(hd, 1))

    res = a.statement()
    print(res)
    # b.statement()
    res = c.statement()
    print(res)