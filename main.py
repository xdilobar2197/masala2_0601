# masala2_0601
def filled_rect(w, h):
    for _ in range(h):
        print("*" * w)

def empty_rect(w, h):
    for i in range(h):
        if i in (0, h-1):
            print("*" * w)
        else:
            print("*" + " "*(w-2) + "*")



def pyramid(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "*"*(2*i-1))

filled_rect(5, 3)
empty_rect(5, 3)
pyramid(4)


nums = {"nol":0,"bir":1,"ikki":2,"uch":3,"to'rt":4}
ops = {"qo'shish":"+","ayirish":"-","ko'paytirish":"*","bo'lish":"/"}

s = "ikki qo'shish uch ko'paytirish to'rt".split()
expr = str(nums[s[0]])

for i in range(1, len(s), 2):
    expr += ops[s[i]] + str(nums[s[i+1]])

print(eval(expr))




import json

FILE = "students.json"

def load():
    try:
        return json.load(open(FILE))
    except:
        return []

def save(data):
    json.dump(data, open(FILE, "w"), indent=2)

def add_student(name):
    data = load()
    data.append({"name": name})
    save(data)

def search(name):
    return [s for s in load() if s["name"] == name]





