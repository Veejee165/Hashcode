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

contributors = {}
for c in range(C):
    name, N = input().split()
    contributors[name] = Contributor(name, int(N))
    for n in range(N):
        skill, L = input().split()
        contributors[name].add_skill(skill, L)
