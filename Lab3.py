import json
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict


#######
## 1 ##
#######

def matrix_Multiplication(mat_1: list, mat_2: list):
    if len(mat_1[1]) != len(mat_2):
        return False

    result = [[0 for _ in range(len(mat_2[0]))] for _ in range(len(mat_1))]


    for i in range(len(mat_1)):
        for j in range(len(mat_2[0])):
            for k in range(len(mat_2)):
                result[i][j] += mat_1[i][k] * mat_2[k][j]

    return result

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[7, 4], [8, 5], [9, 6]]
res = matrix_Multiplication(matrix_1, matrix_2)
#print(res)


#######
## 2 ##
#######

class dane_Osobowe():
    def __init__(self, name = None, surname = None, address = None):
        self.name = name
        self.surname = surname
        self.address = address

    def save(self):
        json_object = json.dumps(vars(self), indent=4)
        with open(__class__.__name__ + ".json", "w") as outfile:
            outfile.write(json_object)

    def load(self):
        with open(__class__.__name__ + ".json", "r") as infile:
            json_obj = json.load(infile)
        self.name = json_obj['name']
        self.surname = json_obj['surname']
        self.address = json_obj['address']

    def __str__(self):
        return f'{self.name} {self.surname} {self.address}'

dane_1 = dane_Osobowe('Grzegorz', 'Płonka', 'Kraków')
dane_1.save()
dane_2 = dane_Osobowe()
dane_2.load()
#print(dane_2)

#######
## 7 ##
#######

@dataclass
class dane_Osobowe_Dataclass:
    name: str
    surname: str
    address: str

    def save(self):
        json_object = json.dumps(vars(self), indent=4)
        with open(__class__.__name__ + ".json", "w") as outfile:
            outfile.write(json_object)

    def load(self):
        with open(__class__.__name__ + ".json", "r") as infile:
            json_obj = json.load(infile)
        self.name = json_obj['name']
        self.surname = json_obj['surname']
        self.address = json_obj['address']


dane_3 = dane_Osobowe_Dataclass('Grzegorz', 'Plonka', 123456)
dane_3.save()
dane_4 = dane_Osobowe_Dataclass(None,None,None)
dane_4.load()
#print(dane_4)


#######
## 3 ##
#######
class dijkstry:
   def __init__(self, graph: dict = {}):
       self.graph = graph

   def shortest_distances(self, source: str):
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0
        pq = [(0, source)] #priority queue
        heapify(pq)
        visited = set()

        while pq:
            current_distance, current_node = heappop(pq)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))

        return distances

Graph = {
   "A": {"B": 3, "C": 3},
   "B": {"A": 3, "D": 3.5, "E": 1},
   "C": {"A": 3, "E": 4, "F": 2},
   "D": {"B": 3.5, "E": 5, "G": 3},
   "E": {"B": 3.5, "C": 6, "D": 4, "G": 5},
   "F": {"G": 3.5, "C": 7},
   "G": {"F": 4, "E": 8, "D": 10},
}

g = dijkstry(Graph)
distances = g.shortest_distances("D")
to = distances["G"]
#print(distances, "\n")
#print(to)


#######
## 4 ##
#######

class aho_Corasick:
    def __init__(self):
        self.trie = {}
        self.fail = {}
        self.output = defaultdict(list)
        self.state_count = 0

    def add_Pattern(self, input_pattern):
        state = 0
        for char in input_pattern:
            if char not in self.trie.get(state, {}):
                self.trie.setdefault(state, {})[char] = self.state_count + 1
                self.state_count += 1
            state = self.trie[state][char]
        self.output[state].append(input_pattern)

    def create(self):
        queue = deque()
        for char, next_state in self.trie.get(0, {}).items():
            self.fail[next_state] = 0
            queue.append(next_state)
        while queue:
            state = queue.popleft()
            for char, next_state in self.trie.get(state, {}).items():
                queue.append(next_state)
                fail_state = self.fail.get(state, 0)
                while fail_state and char not in self.trie.get(fail_state, {}):
                    fail_state = self.fail.get(fail_state, 0)
                self.fail[next_state] = self.trie.get(fail_state, {}).get(char, 0)
                self.output[next_state].extend(self.output[self.fail[next_state]])

    def search(self, input_text):
        state = 0
        results = []
        for i, char in enumerate(input_text):
            while state and char not in self.trie.get(state, {}):
                state = self.fail[state]
            state = self.trie.get(state, {}).get(char, 0)
            if self.output[state]:
                for pattern in self.output[state]:
                    results.append((i - len(pattern) + 1, pattern))
        return results

aaa = aho_Corasick()

words = ["nut", "coconut", "you", "you'll",]

for word in words:
    aaa.add_Pattern(word)

aaa.create()

text = "The coconut nut is a giant nut, if you eat too much you'll get very fat"

matches = aaa.search(text)

#print(matches)

#######
## 5 ##
#######

class state:
    def __init__(self, states: dict = {}, value = 0):
        self.state_Name = value[0]
        self.value = value[1]
        self.states = states

    def return_Next_State(self, input):
        return self.states[input]

    def give_Info(self):
        print("The current state is state {0} with value of {1}".format(self.state_Name,self.value))

class moore_State_Machine:
    def __init__(self, states_dict: dict = {}):
        self.states=[]
        self.current_state = 0
        for key, value in states_dict.items():
            self.states.append(state(value, key))
        self.states[self.current_state].give_Info()


    def next_State(self, input):
        self.current_state = self.states[self.current_state].return_Next_State(input)
        self.states[self.current_state].give_Info()



States = {  # (state name, state value) : {value to change to state : next state}
    (0, 1) : {0 : 0, 1 : 1},
    (1, 1) : {0 : 1, 1 : 2},
    (2, 0) : {0 : 1, 1 : 3},
    (3, 0) : {0 : 4, 1 : 5},
    (4, 0) : {0 : 0, 1 : 5},
    (5, 1) : {0 : 5, 1 : 0},
}

Moore_State_Machine = moore_State_Machine(States)
Inputs = [0, 0, 1, 1, 0, 1, 1, 0, 0 ]

#for value in Inputs:
#    Moore_State_Machine.next_State(value)

#######
## 6 ##
#######

def upper(func):
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    if isinstance(result, str):
      return result.upper()
    return result
  return wrapper

def make_Text():
    return "Mankind knew that they cannot change society. So instead of reflecting on themselves, they blamed the beasts"

make_Text = upper(make_Text)
#print(make_Text())
