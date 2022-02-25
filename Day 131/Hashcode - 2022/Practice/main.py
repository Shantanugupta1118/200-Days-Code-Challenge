in_files=["a_an_example.in.txt","b_better_start_small.in.txt","c_collaboration.in.txt","d_dense_schedule.in.txt","e_exceptional_skills.in.txt","f_find_great_mentors.in.txt"]

out_files=["a_an_example.txt","b_better_start_small.txt","c_collaboration.txt","d_dense_schedule.txt","e_exceptional_skills.txt","f_find_great_mentors.txt"]

for i in range(6):
    in_file=r"input/"+in_files[i]
    out_file=r"output/"+out_files[i]
    
    in_file = open(in_file,'r')
    out_file = open(out_file,'w')
    
    cons={}
                
    skills={}    
    
    contributors,project_count=map(int,in_file.readline().split())
    
    for contributor in range(contributors):
        cname,skill_num = in_file.readline().split()
        skill_num = int(skill_num)
        for i in range(skill_num):
            sname,slevel=in_file.readline().split()
            slevel = int(slevel)
            if cname not in cons.keys():
                cons[cname]=[(sname,slevel)]
            else:
                cons[cname].append((sname,slevel))
                
            if sname not in skills.keys():
                skills[sname]=[(cname,slevel)]
            else:
                skills[sname].append((cname,slevel))
                
    # print(cons)

                
    projects={}
    for project in range(project_count):
        project_data=in_file.readline().split()
        project_name=project_data.pop(0)
        schedule=list(map(int,project_data))
        if project_name not in projects.keys():
            projects[project_name]={"schedule":schedule}
        req_skills=[]
        for j in range(schedule[-1]):
            req_skills.append(in_file.readline().split())
            
        projects[project_name]["req_skills"]=req_skills
            
    
    
    print(projects)
    
    
    for i in projects:
        for s in projects[i][req_skills]:
            skill_name,req_skills_level=s[0],s[1]
            person_available=skills[skill_name]