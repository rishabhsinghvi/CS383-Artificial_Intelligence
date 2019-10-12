from constraint import *

courses = [234, 248, 388, 622, 400, 457, 126, 383, 635]

# Requirements
air = [[234, 248], [234, 388], [622, 457]]
adver = [[388], [622], [400]]
core = [[457], [383], [126]]
malic = [[388], [635]]

# Can't take too many
too_evil = [388, 622, 635]
wizard_basic = [234, 126]
witchcraft = [457, 383]

# Already taken
taken = [635, 234]


# Constraint to guarantee no course is taken for multiple requirements
def unique_courses(a, b, c, d):
    common_elements = 0
    
    common_elements += len(set(a) & set(b))
    common_elements += len(set(a) & set(c))
    common_elements += len(set(a) & set(d))

    common_elements += len(set(b) & set(c))
    common_elements += len(set(b) & set(d))
    
    common_elements += len(set(c) & set(d))

    return common_elements == 0



def good_wizard(a, b, c, d):
    
    list = set([388, 622, 635])

    return len(list & set(a)) + len(list & set(b)) + len(list & set(c)) + len(list & set(d)) in [0, 1]
    

        
def wizardry_basic(a, b, c, d):
    
    list = set([234, 126])

    return len(list & set(a)) + len(list & set(b)) + len(list & set(c)) + len(list & set(d)) in [0, 1]
    

def witchcraft_res(a, b, c, d):
    
    list = set([457, 383])

    return len(list & set(a)) + len(list & set(b)) + len(list & set(c)) + len(list & set(d)) in [0, 1]
    


def taken_malic(a):
    return 635 in a

def taken_air(a):
    return 234 in a



scheduling = Problem()

scheduling.addVariable('air', air)
scheduling.addVariable('adver', adver)
scheduling.addVariable('core', core)
scheduling.addVariable('malic', malic)

scheduling.addConstraint(unique_courses, ['air', 'adver', 'core', 'malic'])
scheduling.addConstraint(good_wizard, ['air', 'adver', 'core', 'malic'])
scheduling.addConstraint(wizardry_basic, ['air', 'adver', 'core', 'malic'])
scheduling.addConstraint(witchcraft_res, ['air', 'adver', 'core', 'malic'])

scheduling.addConstraint(taken_malic, ['malic'])
scheduling.addConstraint(taken_air, ['air'])

solutions = scheduling.getSolutions()
for sol in solutions:
    print(sol)

print('\n\n\n')
print(len(solutions))