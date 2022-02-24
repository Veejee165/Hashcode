class Contributor:
    def __init__(self, name, skill_count):
        self.name = name
        self.skill_count = skill_count
C = int(input())
P = int(input())
contributors = {}
for c in range(C):
    name, skill_count = input().split()
    contributors[name] = Contributor(name, int(skill_count))
    