# Github: Shantanugupta1118
# DAY 131 of DAY 200
# Mentorship & Teamwork - Hashcode

import sys
file2 = "Output/f1.txt"
sys.stdout = open(file2,"w")




class Skill:
    name = ""
    level = 0
    
    def __init__(self, name, level):
        self.name = name
        self.level = level
        
    def __repr__(self):
        return f"skill: {self.name} {self.level}"
    
    
class Contributor:
    name = ""
    skills = None

    def __init__(self, name):
        self.name = name
        self.skills = []

    def addSkill(self, role):
        self.skills.append(role)

    def __repr__(self):
        ret = f"Contributor: {self.name}\n"
        for skill in self.skills:
            ret += skill.__repr__() + "\n"
        return ret

    def canFulfillRole(self, role):
        for skill in self.skills:
            if skill.name == role.name and skill.level >= role.level:
                return True
        return False

    def doneJob(self, role):
        for skill in self.skills:
            if skill.name == role.name:
                if skill.level <= role.level:
                    skill.level += 1
                return
    
class Project:
    name = ""
    duration = 0
    score = 0
    last_day = 0
    roles = None

    def __init__(self, name, duration, score, last_day):
        self.name = name
        self.duration = duration
        self.score = score
        self.last_day = last_day
        self.roles = []

    def addRole(self, skill):
        self.roles.append(skill)

    def __repr__(self):
        ret = f"Project: {self.name}\nDuration: {self.duration}\nScore: {self.score}\nBest before: {self.last_day}\n"
        for role in self.roles:
            ret += role.__repr__() + "\n"
        return ret


class Work:
    name = ""
    workers = None

    def __init__(self, name, workers):
        self.name = name
        self.workers = workers


def readFile(file, contributors, projets):
    firstLine = file.readline().split(' ')
    nbContributors = int(firstLine[0])
    nbProjets = int(firstLine[1])

    for _ in range(0, nbContributors):
        contributorLine = file.readline().split(' ')
        contributor = Contributor(contributorLine[0])
        nbSkills = int(contributorLine[1])

        for _ in range(0, nbSkills):
            skillLine = file.readline().split(' ')
            contributor.addSkill(Skill(skillLine[0], int(skillLine[1])))
        contributors.append(contributor)

    for _ in range(0, nbProjets):
        projectLine = file.readline().split(' ')
        project = Project(projectLine[0], int(projectLine[1]), int(projectLine[2]), int(projectLine[3]))
        nbRoles = int(projectLine[4])

        for _ in range(0, nbRoles):
            skillLine = file.readline().split(' ')
            project.addRole(Skill(skillLine[0], int(skillLine[1])))
        projets.append(project)



def enrollWork(works, project, asg):
    workers = []

    for role in project.roles:
        asg[role].doneJob(role)
        workers.append(asg[role])
    works.append(Work(project.name, workers))


def prototype(contributors, projects, works):
    asg, remainRole = None, None

    for project in projects:
        asg = {}
        remainRole = list(project.roles)
        # total_RRoles = len(remainRole)
        # print(total_RRoles)
        for contributor in contributors:
            for role in remainRole:
                if contributor.canFulfillRole(role):
                    remainRole.remove(role)
                    asg[role] = contributor
                    break
        if len(remainRole) == 0:
            enrollWork(works, project, asg)
            
           


def process(file_path):
    contributors, projects, works = [], [],[]
    file = open(file_path)
    readFile(file, contributors, projects)
    projects.sort(key = lambda p:p.last_day)
    prototype(contributors, projects, works)
    print(len(works))
    for work in works:
        workers = work.workers

        print(work.name)
        for i in range(0, len(workers)):
            if i > 0:
                print(f" {workers[i].name}", end='')
            else:
                print(workers[i].name, end='')
        print()
        
    
        
inputFilesDirectory = "Practice/input/"  
# outputFilesDirectory = "Output/" 
# fileNames = ["a_an_example.in", 
#             "b_better_start_small.in", 
#             "c_collaboration.in",
#             "d_dense_schedule.in", 
#             "e_exceptional_skills.in",
#             "f_find_great_mentors.in"] 
# for fileName in fileNames: 
#     process(inputFilesDirectory+fileName+".txt")
    

process(inputFilesDirectory+"f_find_great_mentors.in"+".txt")