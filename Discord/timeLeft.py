import datetime

def timeLeft():
    beta = datetime.date(2017,7,18)
    release = datetime.date(2017,9,6)
    today = datetime.date.today()
    untilBeta = str((beta-today).days)
    untilRelease = str((release-today).days)
    output = "There are "+untilBeta+" days until the beta, and "+untilRelease+" days until release!"
    return output

if __name__ == "__main__":
    print (timeLeft())
