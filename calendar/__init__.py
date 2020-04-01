import itertools
from itertools import chain

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
        self.items = dict()

    def __getitem__(self, key: int):
        if self.basecalendar is None:
            return P.closed(key, key)
        else:
            if key in self.items.keys():
                return self.items[key]
            else:
                passed_periods = [self.periods[x % len(self.periods)] for x in range(0, key)]
                p_key = self.reftime + sum(passed_periods)
                #print("p:" + str(p_key))
                n_key = self.periods[key % len(self.periods)]
                #print("n:" + str(n_key))

                c_key = P.closed(self.basecalendar[p_key].lower,self.basecalendar[p_key + n_key].lower)
                c_key = list(P.iterate(c_key, step=1, base=int))
                c_key = P.closed(c_key[0], c_key[-1]-1)

                self.items[key] = c_key
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
        u = l + self.duration
        return P.closed(self.calendars[-1][l].lower, self.calendars[-1][u].upper)

def ticks(i, alpha, startingpoints, calendars):
    sp = startingpoint(i, alpha, startingpoints, calendars)
    if alpha == 0:
        print("i=" + str(i) + " alpha=" + str(alpha) + " c[" + str(sp) + "]")
        return sp
    else:
        periods = calendars[alpha - 1].periods
        returnval = startingpoints[alpha][sp] \
               + sum([periods[x % len(periods)] for x in range(0, ticks(i, alpha - 1, startingpoints, calendars))])\
               + calendars[alpha - 1].reftime
        print("i=" + str(i) + " alpha=" + str(alpha) + " c[" + str(returnval) + "]")
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
            return startingpoints[0]
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

    # def calculate_(self, amount):
    #     intervals = list()
    #     for calendar_number in range(1, len(self.starting_points)):
    #         intervals.append(list())
    #         for starting_point in range(0, len(self.starting_points[calendar_number])):
    #             for count in range(0,amount + 5 ** calendar_number):
    #                 intervals[calendar_number-1].append(
    #                 self.calendars[calendar_number]
    #                 [self.starting_points[calendar_number][starting_point] + self.calendars[calendar_number].period * count].lower)
    #     #for i in range(0, len(intervals)):
    #         #for j in range(0, len(intervals[i])):
    #             #intervals[i][0] = intervals[i][0].union(intervals[i][j])
    #         #print(intervals[i][0])
    #     return intervals

# def X(i: int, n:int, starting_points:list):
#     #print(i,n)
#     return math.floor( i /
#                        max(1,sum([len(starting_points[x]) for x in range(n+1, len(starting_points))]))
#                       ) \
#            % len(starting_points[n])
#
# def Counts(i,n, starting_points, calendars):
#     if n == 0:
#         r_val =  math.floor( i /
#                        max(1,sum([len(starting_points[x]) for x in range(n+1, len(starting_points))]))
#                       )
#         print("number of C0: " + str(r_val) + calendars[0].name)
#         return r_val
#     else:
#         r_val =  starting_points[n][X(i,n,starting_points)] \
#            + sum([calendars[n-1].periods[x % len(calendars[n-1].periods)] for x in range (0, Counts(i, n-1, starting_points, calendars) )])
#         print("number of C" + str(n) + ":" + str(r_val) + calendars[n].name)
#         return r_val
