# Github: Shantanugupta1118
# DAY 131 of DAY 200
# Mentorship & Teamwork - Hashcode - 2022



class Solution:
    def file_render(self, filename):
        
        with open(filename) as f:
            lines = f.readlines()
            # contents = f.read()
            
        words = lines[0].split()
        contributorCount = int(words[0])
        projectCount = int(words[1])
        c, p = [], []
        n_lines = 1
        while True:
            contributor = self.readContributor(lines[n_lines:])
            c.append(contributor)
            n_lines += contributor["skills_counter"]+1
            if len(c) >= contributorCount: break
        
        while True:
            project = self.readProject(lines[n_lines:])
            p.append(project)
            n_lines += project["role_counter"]+1
            if len(p) >= projectCount: break
        
        return {
            "contributors": c,
            "projects": p
            }
        
    def readContributor(self, contri):
        words = contri[0].split()
        contributor = {
            "name": words[0],
            "skills_counter": int(words[1]),
            "skills": self.readSkills(contri[1:1])
            }
        return contributor
    
    def readSkills(self, contri):
        skills = []
        for l in contri:
            words = l.split()
            skill = {
                "name": words[0],
                "skilllevel": int(words[1])
            }
            skills.append(skill)
    
    def readProject(self, lines):
        words = lines[0].split()
        project = {
            "name": words[0],
            "durationInDays": int(words[1]),
            "score": int(words[2]),
            "bestBeforeInDays": int(words[3]),
            "role_counter": int(words[4]),
            "roles": self.readSkills(lines[1:1 + int(words[4])])
        }

        return project
        
        
        
        

    
a = Solution()
print(a.file_render("Input/a_an_example.in.txt"))













