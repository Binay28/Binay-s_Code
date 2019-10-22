import operator

def person_lister(f):
    def inner(people):
        # complete the function
        return(map(f,sorted(people,key= lambda x:int(x[2]))))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
#need to study this code thoroughly for decorators part 
#decorated_results = sorted(people, key=operator.itemgetter(2))
  #      return [f(p) for p in decorated_results]
#can use itemgetter function instead of that lambda keyword for the age
