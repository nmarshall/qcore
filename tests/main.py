import settings #will add qcore.pyd folder to the path

import datetime

import qcore
def test_calcDates_wrap():
    import datetime
    start = datetime.date(2010,2,10)
    end = datetime.date(2020,2,10)
    freq = 'A'
    holidays = 'LON'
    bizConv = qcore.BizDayConv.foll
    
    cdts = qcore.calcDates('abc',start,end,freq,holidays,bizConv)
    
    print cdts
    


if __name__ == '__main__':
    test_calcDates_wrap()
    


