from calendar import Calendar, PeriodicExpression

#elemental calendars
c_basic = Calendar('basic', 0, None, [1])
c_minutes = Calendar('minutes', 0, c_basic, [1])
c_hours = Calendar('hours', 0, c_minutes, [60])
c_days = Calendar('days', 0, c_hours, [24])
c_weeks = Calendar('weeks', 0, c_days, [7])
c_months = Calendar('months', 0, c_days, [31,28,31,30,31,30,31,31,30,31,30,31,
                                          31,28,31,30,31,30,31,31,30,31,30,31,
                                          31,29,31,30,31,30,31,31,30,31,30,31,
                                          31,28,31,30,31,30,31,31,30,31,30,31])
c_years = Calendar('years', 0, c_months, [12])

# print(c_months[0])
# print(c_weeks[1])
# print(c_weeks[1])
# print(c_days[9])
# print(c_hours[224])
# print(c_minutes[13470])
# print(c_days[0])
# print(c_days[1])

#some basic periodic expressions
pe1 = PeriodicExpression("pe1", [[0],[0,2,3],[0,2,6],[0,30]], [c_weeks, c_days, c_hours, c_minutes], 1, c_minutes)
pe_bh = PeriodicExpression("business_hours", [["all"],[0,1,2,3,4],[8],[30]], [c_weeks, c_days, c_hours, c_minutes], 510, c_minutes)

# print("---- PE-BH ----")
# print("pe_bh[0]", pe_bh[0])
# print("pe_bh[1]", pe_bh[0])
# print("pe_bh[2]", pe_bh[2])
# print("pe_bh[3]", pe_bh[3])
# print("pe_bh[4]", pe_bh[4])
# print("pe_bh[5]", pe_bh[5])
# print("pe_bh[6]", pe_bh[6])
# print("pe_bh[7]", pe_bh[7])
# print("pe_bh[8]", pe_bh[8])

print("---- PE-BH Example ----")
print("pe_bh[8]", pe_bh[8])
print("c_weeks[1]", c_weeks[1])
print("c_days[9]", c_days[9])
print("c_hours[224]", c_hours[224])
print("c_minutes[13470]", c_minutes[13470])
print("c_minutes[13979]", c_minutes[13979])

#the basic periodic expressions of the trebla case
pe_wh = PeriodicExpression("Working Hours", [["all"],[0,1,2,3,4],[8],[30]], [c_weeks, c_days, c_hours, c_minutes], 510, c_minutes)
pe_ov = PeriodicExpression("Overtime", [["all"],[0,1,2,3,4],[17],[00]], [c_weeks, c_days, c_hours, c_minutes], 90, c_minutes)
pe_vh = PeriodicExpression("Visiting Hours", [["all"],[0,1,2,3,4],[10]], [c_weeks, c_days, c_hours], 6, c_hours)
pe_gs = PeriodicExpression("Guarding Shifts", [["all"],[0,1,2,3,4,5,6],[18],[30]], [c_weeks, c_days, c_hours, c_minutes], 780, c_minutes)
pe_cs = PeriodicExpression("Cleaning Shifts", [["all"],[2,4],[18],[30]], [c_weeks, c_days, c_hours, c_minutes], 90, c_minutes)

print("c_years[30]", c_years[30])

#determine min_i for wh
# min_i_wh = pe_wh[7827]
# min_i_wh_lower = pe_wh[7826]
# print(c_years[30].contains(min_i_wh.lower))
# print(c_years[30].contains(min_i_wh_lower.lower))

print("pe_wh[7827]", pe_wh[7827])
print("pe_wh[7828]", pe_wh[7828])
print("pe_wh[7829]", pe_wh[7829])
print("pe_wh[7830]", pe_wh[7830])
print("pe_wh[7831]", pe_wh[7831])

#determine min_i for ov
# min_i_ov = pe_ov[7827]
# min_i_ov_lower = pe_ov[7826]
# print(c_years[30].contains(min_i_wh.lower))
# print(c_years[30].contains(min_i_wh_lower.lower))

print("pe_ov[7827]", pe_ov[7827])
print("pe_ov[7828]", pe_ov[7828])
print("pe_ov[7829]", pe_ov[7829])
print("pe_ov[7830]", pe_ov[7830])
print("pe_ov[7831]", pe_ov[7831])

#determine min_i for vh
# min_i_vh = pe_vh[7827]
# min_i_vh_lower = pe_vh[7826]
# print(c_years[30].contains(min_i_vh.lower))
# print(c_years[30].contains(min_i_vh_lower.lower))

print("pe_vh[7827]", pe_vh[7827])
print("pe_vh[7828]", pe_vh[7828])
print("pe_vh[7829]", pe_vh[7829])
print("pe_vh[7830]", pe_vh[7830])
print("pe_vh[7831]", pe_vh[7831])

#determine min_i for gs
# min_i_gs = pe_gs[10957]
# min_i_gs_lower = pe_gs[10956]
# print(min_i_gs)
# print(c_years[30].contains(min_i_gs.lower))
# print(c_years[30].contains(min_i_gs_lower.lower))

print("pe_gs[10957]", pe_gs[10956])
print("pe_gs[10957]", pe_gs[10957])
print("pe_gs[10958]", pe_gs[10958])
print("pe_gs[10959]", pe_gs[10959])
print("pe_gs[10960]", pe_gs[10960])
print("pe_gs[10961]", pe_gs[10961])
print("pe_gs[10962]", pe_gs[10962])
print("pe_gs[10963]", pe_gs[10963])
print("pe_gs[10964]", pe_gs[10964])

#determine min_i for cs
# min_i_cs = pe_cs[3130]
# min_i_cs_lower = pe_cs[3129]
# print(min_i_cs)
# print(c_years[30].contains(min_i_cs.lower))
# print(c_years[30].contains(min_i_cs_lower.lower))

print("pe_cs[3130]", pe_cs[3130])
print("pe_cs[3131]", pe_cs[3131])
