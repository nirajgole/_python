

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None

person = {'name':'John','city':'Pune'}
person['city']
get(person,"name")

#try-except-else-finally
def divide(a,b):
    try:
        result=a/b
    except (ZeroDivisionError,TypeError):
        print('It\'s Error')
    else:
        print('Result is',result)
    finally:
        print('Done')

divide(1,0)
divide(1,2)