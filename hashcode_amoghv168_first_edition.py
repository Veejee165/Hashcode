class Contributor:
    def __init__(self, name, skill_count):
        self.name = name
        self.skill_count = skill_count

f = open("C:\\Users\\RAHUL\\Desktop\\HashCode\\data\\a_an_example.in.txt", "r")
inp1 = f.readline()
inp = [int(x) for x in inp1.split()]
C = inp[0]
P = inp[1]

contributors = {}
for c in range(C):
    name, skill_count = input().split()
    contributors[name] = Contributor(name, int(skill_count))
    
