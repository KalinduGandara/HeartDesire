def getPersonality(data):
    letter1 , rate1 = introvert(data[0])
    letter2 , rate2 = intitive(data[1])
    letter3 , rate3 = thinking(data[2])
    letter4 , rate4 = judging(data[3])
    personality = letter1+letter2+letter3+letter4
    return (rate1,rate2,rate3,rate4,personality)

def precentage(x):
    return x.count('1')/10


def introvert(data):
        matching_rate = precentage(data)
        if (matching_rate >= 0.5):
            return ("I",matching_rate)
        else :
            return ("E",matching_rate)
        
def intitive(data):
        matching_rate = precentage(data)
        if (matching_rate >= 0.5):
            return ("S",matching_rate)
        else :
            return ("N",matching_rate)


def thinking(data):
        matching_rate = precentage(data)
        if (matching_rate >= 0.5):
            return ("F",matching_rate)
        else :
            return ("T",matching_rate)

def judging(data):
        matching_rate = precentage(data)
        if (matching_rate >= 0.5):
            return ("P",matching_rate)
        else :
            return ("J",matching_rate)
