import math


def entropy(examples, target):
        """Takes a list of examples and returns their entropy w.r.t. the target attribute"""
        possible_values = ['S', 'C']
        bucket = [0 for _ in possible_values]

        for example in examples:
            bucket[possible_values.index(example[target])] += 1

        
        #print(len(examples))
        total_examples = sum(bucket)
        entropy = 0
        for el in bucket:
            p_el = el / total_examples

            entropy += (p_el * math.log2(p_el) if p_el != 0 else 0)
        
        #print(-entropy)
        return -entropy if entropy != 0 else entropy


def information_gain(parent, children):
        """
        Takes a `parent` set and a subset `children` of the parent.
        Returns the information gain due to splitting `children` from `parent`.
        """
        total = len(parent)
        len_children = [len(child) for child in children]
        
        parent_entropy = entropy(parent)
        children_entropy = []
        for child in children:
            children_entropy.append(entropy(child))

        avg_entropy = 0
        for i in range(len(children)):
            avg_entropy = len_children[i]/total * children_entropy[i]
        # TODO: Implement the information gain
        
        return parent_entropy - avg_entropy
    

parent =  [
    [1, 'S'],
    [2, 'S'],
    [3, 'S'],
    [4, 'S'],
    [5, 'S'],
    [6, 'S'],
    [7, 'S'],
    [8, 'S'],
    [9, 'S'],
    [10, 'S'],
    [11, 'S'],
    [12, 'S'],
    [13, 'S'],
    [14, 'S'],
    [15, 'C'],
    [16, 'C'],
    [17, 'C'],
    [18, 'C'],
    [19, 'C'],
    [20, 'C'],
    [21, 'C'],
    [22, 'C'],
    [23, 'C'],
    [24, 'C'],
    [25, 'C'],
    [26, 'C'],
    [27, 'C'],
    [28, 'C'],
    [29, 'C'],
    [30, 'C'],
]

child1 = [
    [1, 'S'],
    [2, 'C'],
    [3, 'C'],
    [4, 'C'],
    [5, 'C'],
    [6, 'C'],
    [7, 'C'],
    [8, 'C'],
    [9, 'C'],
    [10, 'C'],
    [11, 'C'],
    [12, 'C'],
    [13, 'C'],
]

child2 = [
    [1, 'S'],
    [2, 'S'],
    [3, 'S'],
    [4, 'S'],
    [5, 'S'],
    [6, 'S'],
    [7, 'S'],
    [8, 'S'],
    [9, 'S'],
    [10, 'S'],
    [11, 'S'],
    [12, 'S'],
    [13, 'S'],
    [14, 'C'],
    [15, 'C'],
    [16, 'C'],
    [17, 'C']
]

print(entropy(parent, 1))
print(information_gain(parent, [child1, child2]))