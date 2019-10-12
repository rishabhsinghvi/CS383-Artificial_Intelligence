from constraint import *


# Requirements
air = [[234, 248], [234, 388], [622, 457]]
adver = [[388], [622], [400]]
core = [[457], [383], [126]]
malic = [[388], [635]]


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



def good_wizard_restriction(a, b, c, d):   
    list = set([388, 622, 635])
    return len(list & set(a)) + len(list & set(b)) + len(list & set(c)) + len(list & set(d)) in [0, 1]
    

        
def wizardry_basic_restriction(a, b, c, d):
    list = set([234, 126])
    return len(list & set(a)) + len(list & set(b)) + len(list & set(c)) + len(list & set(d)) in [0, 1]
    

def witchcraft_restriction(a, b, c, d):
    list = set([457, 383])
    return len(list & set(a)) + len(list & set(b)) + len(list & set(c)) + len(list & set(d)) in [0, 1]
    


def taken_malicious_magic_requirement(a):
    return 635 in a

def taken_air_wizardry_requirement(a):
    return 234 in a



def main():
    scheduling = Problem()

    scheduling.addVariable('air', air)
    scheduling.addVariable('adver', adver)
    scheduling.addVariable('core', core)
    scheduling.addVariable('malic', malic)

    scheduling.addConstraint(unique_courses, ['air', 'adver', 'core', 'malic'])
    scheduling.addConstraint(good_wizard_restriction, ['air', 'adver', 'core', 'malic'])
    scheduling.addConstraint(wizardry_basic_restriction, ['air', 'adver', 'core', 'malic'])
    scheduling.addConstraint(witchcraft_restriction, ['air', 'adver', 'core', 'malic'])

    scheduling.addConstraint(taken_malicious_magic_requirement, ['malic'])
    scheduling.addConstraint(taken_air_wizardry_requirement, ['air'])    

    solutions = scheduling.getSolutions()
    print(len(solutions))

if __name__ == "__main__":
    main()