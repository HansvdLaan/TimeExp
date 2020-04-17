import itertools
import math
import portion as P

class Calendar:

    def __init__(self, name: str, reftime: int, basecalendar, period: list):
        from calendar import Calendar
        self.name = name
        self.reftime = reftime
        self.basecalendar = basecalendar
        self.periods = period
        self.period = sum(self.periods)

    def __getitem__(self, key: int):
        if self.basecalendar is None:
            return P.closed(key, key)
        else:
            turns = divmod(key, len(self.periods))
            passed_periods_time = turns[0] * sum(self.periods) #How many times have all periods been passed?
            passed_periods_time += sum([self.periods[x % len(self.periods)] for x in range(0, turns[1])])

            p_key = self.reftime + passed_periods_time
            #print("p:" + str(p_key))
            n_key = self.periods[key % len(self.periods)]
            #print("n:" + str(n_key))

            c_key = P.closed(self.basecalendar[p_key].lower,self.basecalendar[p_key + n_key].lower)
            c_key = list(P.iterate(c_key, step=1, base=int))
            c_key = P.closed(c_key[0], c_key[-1]-1)

            return c_key

class PeriodicExpression:
    def __init__(self, name: str, starting_points: list, calendars:list, duration, duration_calendar):
        from calendar import Calendar
        self.name = name
        self.starting_points = starting_points
        self.calendars = calendars
        self.duration = duration
        self.duration_calendar = duration_calendar

    def __getitem__(self, key: int):

        l = self.calendars[0][ticks(key, 0, self.starting_points, self.calendars)]
        for i in range(1, len(self.calendars)):
            sp = self.calendars[i][ticks(key, i, self.starting_points, self.calendars)]
            l = l.intersection(sp)
        l = l.lower
        #equal to:
        # l = index_C(key, len(self.calendars)-1, self.starting_points, self.calendars)
        u = self.calendars[len(self.calendars)-1][ticks(key, len(self.calendars)-1, self.starting_points, self.calendars) + self.duration - 1].upper
        return P.closed(l, u)

def ticks(i, alpha, startingpoints, calendars):
    sp = startingpoint(i, alpha, startingpoints, calendars)
    if alpha == 0:
        #print("i=" + str(i) + " alpha=" + str(alpha) + " c[" + str(sp) + "]")
        return sp
    else:
        periods = calendars[alpha - 1].periods
        returnval = startingpoints[alpha][sp] \
               + sum([periods[x % len(periods)] for x in range(0, ticks(i, alpha - 1, startingpoints, calendars))])\
               + calendars[alpha - 1].reftime
        #print("i=" + str(i) + " alpha=" + str(alpha) + " c[" + str(returnval) + "]")
        return returnval

def startingpoint(i, alpha, startingpoints, calendars):
    if alpha == 0:
        #return math.floor(i / math.prod([len(startingpoints[x]) for x in range(1, len(startingpoints))]))
        return math.floor(i / len(valid(startingpoints[1:], calendars[1:])))
    if alpha == len(startingpoints)-1:
        return i % len(startingpoints[alpha])
    else:
        return math.floor(i / len(valid(startingpoints[alpha + 1:], calendars[alpha + 1:]))) % len(startingpoints[alpha])

def valid(startingpoints, calendars):
        if len(calendars) == 1:
            return [startingpoints[0]]
        else:
            product = list(itertools.product(startingpoints[0],valid(startingpoints[1:], calendars[1:])))
            result = []
            for combination in product:
                if isinstance(combination[1], int):
                    if(calendars[0].periods[combination[0] % len(calendars[0].periods)] > combination[1]):
                        result.append(list(combination))
                if isinstance(combination[1], list):
                    if(calendars[0].periods[combination[0] % len(calendars[0].periods)] > combination[1][0]):
                        result.append(list(combination))
            return result