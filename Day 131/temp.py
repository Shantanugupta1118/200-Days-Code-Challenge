
import sys

class Skill:
    name = ""
    level = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Skill: {self.name} {self.level}"

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
    bestBefore = 0
    roles = None

    def __init__(self, name, duration, score, bestBefore):
        self.name = name
        self.duration = duration
        self.score = score
        self.bestBefore = bestBefore
        self.roles = []

    def addRole(self, skill):
        self.roles.append(skill)

    def __repr__(self):
        ret = f"Project: {self.name}\nDuration: {self.duration}\nScore: {self.score}\nBest before: {self.bestBefore}\n"
        for role in self.roles:
            ret += role.__repr__() + "\n"
        return ret

class Work:
    name = ""
    workers = None

    def __init__(self, name, workers):
        self.name = name
        self.workers = workers

# Fill contributors and projets
def read_file(file, contributors, projets):
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

def dummyAssignments(contributors, projets, works):
    assignments = None
    remainingRoles = None

    for project in projets:
        assignments = {}
        remainingRoles = list(project.roles)
        nbRoles = len(remainingRoles)

        for contributor in contributors:
            for role in remainingRoles:
                if contributor.canFulfillRole(role):
                    remainingRoles.remove(role)
                    assignments[role] = contributor
                    break

        if len(remainingRoles) == 0:
            addWork(works, project, assignments)

def addWork(works, project, assignments):
    workers = []

    for role in project.roles:
        assignments[role].doneJob(role)
        workers.append(assignments[role])
    works.append(Work(project.name, workers))

# Open file, fill lists, run simulation
def main(path):
    contributors = []
    projets = []
    works = []

    file = open(path)
    read_file(file, contributors, projets)

    projets.sort(key=lambda project: project.bestBefore)

    dummyAssignments(contributors, projets, works)

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

if __name__ == "__main__":
    main("a_an_example.in.txt")