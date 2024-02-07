#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    if 'Jan' in month:
        return '01'
    elif 'Feb' in month:
        return '02'
    elif 'Mar' in month:
        return '03'
    elif 'Apr' in month:
        return '04'
    elif 'May' in month:
        return '05'
    elif 'Jun' in month:
        return '06'
    elif 'Jul' in month:
        return '07'
    elif 'Aug' in month:
        return '08'
    elif 'Sep' in month:
        return '09'
    elif 'Oct' in month:
        return '10'
    elif 'Nov' in month:
        return '11'
    else:
        return '12'
#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(bad_date):
    bad_date = bad_date.replace(',', ' ')
    bad_date = bad_date.split()
    month = bad_date[0]
    month = str(parse_month(month))
    if len(bad_date[1]) != 2:
        bad_date[1] = '0'+ bad_date[1]
    bad_date[0] = month
    user_string = '/'.join(bad_date)
    return user_string

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    bad_date = input()
    #bad_date = bad_date.replace(',', ' ')
    #bad_date = bad_date.split()
    #month = bad_date[0]
    #month = str(parse_month(month))
    #if len(bad_date[1]) != 2:
    #    bad_date[1] = '0'+ bad_date[1]
    #bad_date[0] = month
    print(parse_date(bad_date))
    #test2