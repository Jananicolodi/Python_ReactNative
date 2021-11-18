from datetime import datetime

def is_weekday():
    today = datetime.today()
    return(5 <= today.weekday() < 7)
assert is_weekday()