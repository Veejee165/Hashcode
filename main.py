days_passsed=0
assigned=[]
projects_done=0
max_days=0
def assign(project_days,to_assign):
    for e in to_assign:
        if e in assigned:
            j=0
    if j!=0:
        if max_days<project_days:
            global max_days
            max_days=project_days
            global days_passsed
            days_passsed = days_passsed + (project_days-max_days)
        global assigned
        assigned = to_assign
        global  projects_done
        projects_done=projects_done+1







