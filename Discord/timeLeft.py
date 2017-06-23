from datetime import date

def timeLeft():
    beta = datetime.date(2017,7,18)
    release = datetime.date(2017,9,6)
    today = date.today()
    untilBeta = beta-today
    untilRelease = release-today
    output = "There are "+untilBeta+" days until the beta, and "+untilRelease+" days until release!"
    return output
