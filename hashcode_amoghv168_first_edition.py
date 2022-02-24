class Contributor:
    def __init__(self, name, skill_count):
        self.name = name
        self.skill_count = skill_count
        self.skill_dict = {}
    def add_skill(self, skill, L):
        self.skill_dict[skill] = L

f = open("a_an_example.in.txt", "r")
inp1 = f.readline()
inp = [int(x) for x in inp1.split()]
C = inp[0]
P = inp[1]

print(C,P)

contributors = {}
for c in range(C):
    inp1 = f.readline().split()
    name, N = inp1[0], int(inp1[1])
    #print(name, N)
    contributors[name] = Contributor(name, int(N))
    for n in range(N):
        inp1 = f.readline().split()
        skill, L = inp1[0], int(inp1[1])
        contributors[name].add_skill(skill, L)
        
"""
for key, value in contributors.items():
    print(key, ' : ', value.skill_dict)

for key, value in contributors.items():
    print(key, ' : ', value.skill_count)
"""
