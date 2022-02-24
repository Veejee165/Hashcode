class Contributor:
    def __init__(self, name, skill_count):
        self.name = name
        self.skill_count = skill_count
        self.skill_dict = {}

    def add_skill(self, skill, L):
        self.skill_dict[skill] = L

    def lvl_up_skill(self, skill):
        if skill in self.skill_dict.keys():
            self.skill_dict[skill] += 1
        else:
            self.skill_dict[skill] = 1

class Project:
    def __init__(self, name, D, S, B, R): #D=DAYS S=SCORE B=BEST BEFORE R=NO OF REQUIRED SKILLS
        self.name = name
        self.D = D
        self.S = S
        self.B = B
        self.R = R
        self.skill_dict = {}
    def add_req_skill(self, req_skill, L):
        self.skill_dict[req_skill] = L 



f = open("a_an_example.in.txt", "r")
inp1 = f.readline()
inp = [int(x) for x in inp1.split()]
C = inp[0]
P = inp[1]

#print(C,P)

contributors = {}
for c in range(C):
    inp1 = f.readline().split()
    cname, N = inp1[0], int(inp1[1])
    #print(name, N)
    contributors[cname] = Contributor(cname, N)
    for n in range(N):
        inp1 = f.readline().split()
        skill, L = inp1[0], int(inp1[1])
        contributors[cname].add_skill(skill, L)


project_skill = {}
for c in range(P):
    inp1 = f.readline().split()
    pname, D, S, B, R = inp1[0], int(inp1[1]), int(inp1[2]), int(inp1[3]), int(inp1[4])
    #print(pname, D, S, B, R)
    project_skill[pname] = Project(pname, D, S, B, R)
    for n in range(R):
        inp1 = f.readline().split()
        skill, L = inp1[0], int(inp1[1])
        project_skill[pname].add_req_skill(skill, L)


"""
contributors[name].lvl_up_skill(skill)
#contributors["Anna"].lvl_up_skill("C++")

for key, value in contributors.items():
    print(key, ' : ', value.skill_dict)

for key, value in contributors.items():
    print(key, ' : ', value.skill_count)

for key, value in project_skill.items():
    print(key, ' : ', value.skill_dict)
"""
