import csv
import math
import copy

class DataSet:
    """
    This class reads the dataset from a csv file, given the file path as a string.
    It exposes the following class members:

        attributes: a list of strings representing the name of each attribute
        domains: a list of lists indicating the possible values each attribute
                 in self.attributes can take in the provided data
        examples: a list of lists, with each element representing a datapoint
    """
    def __init__(self, path_to_csv):
        with open(path_to_csv, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self.attributes = next(csvreader)
            self.examples = [row for row in csvreader]

            # "Clean" dataset by changing any value not in the domain to the plurality vote
            for j in range(len(self.examples[0])):
                num_aye = 0
                num_nay = 0

                for i in range(len(self.examples)):

                    if self.examples[i][j] == 'Aye' or self.examples[i][j] == 'Yea':
                        num_aye += 1
                    elif self.examples[i][j] == 'Nay':
                        num_nay += 1
            
                if num_aye == 0 and num_nay == 0:
            
                    continue

                max = num_aye if num_aye >= num_nay else num_nay

                for i in range(len(self.examples)):
            
                    if self.examples[i][j] != 'Aye' and self.examples[i][j] != 'Nay':
                        if self.examples[i][j] == 'Yea':
                            self.examples[i][j] = 'Aye'
                        elif max == num_aye:
                            self.examples[i][j] = 'Aye'
                        else:  
                            self.examples[i][j] = 'Nay'
    

            self.domains = [list(set(x)) for x in zip(*self.examples)]

            # Debug



    def set_attrs(self, attrs):
        self.attributes = attrs

    def set_examples(self, exs):
        self.examples = exs

    def set_domains(self, doms):
        self.domains = doms


class Node:
    """
    This class represents an internal node of a decision tree.
    `test_attr` is the index of the attribute to test at this node.
    `test_name` is the human-readable name of that attribute.
    The Node stores a dictionary `self.children` that maps values of the test
    attribute to subtrees, where each subtree is either a Node or a Leaf.
    """
    def __init__(self, test_attr, test_name=None):
        self.test_attr = test_attr
        self.test_name = test_name or test_attr
        self.children = {}

    def classify(self, example):
        """Classify an example based on its test attribute value."""

        # TODO: Implement the classify function here and in the Leaf class
        return self.children[example[self.test_attr]].classify(example)
        pass

    def add_child(self, val, subtree):
        """Add a child node, which could be either a Node or a Leaf."""
        self.children[val] = subtree

    def show(self, level=1):
        """Print a human-readable representation of the tree"""
        print('Test:', self.test_name)
        for (val, subtree) in self.children.items():
            print(' ' * 4 * level, "if", self.test_name, '=', val, '==>', end=' ')
            if isinstance(subtree, Leaf):
                subtree.show()
            else:
                subtree.show(level + 1)


class Leaf:
    """A Leaf holds only a predicted class, with no test."""
    def __init__(self, pred_class):
        self.pred_class = pred_class

    def classify(self, example):
        return self.pred_class

    def show(self):
        """This will be called by the Node `show` function"""
        print('Predicted class:', self.pred_class)


def learn_decision_tree(dataset, target_name, feature_names, max_depth):
    """
    Trains a decision tree on the provided dataset.
    The `target_name` parameter is the name of the attribute to be predicted.
    The `feature_names` are the names of input attributes that should be used to split the data.
    Finally, `depth_limit` is a parameter to control overfitting by cutting off the tree after
    a certain depth and predicting the plurality class at that split.

    This function should return a decision tree learned from the data.
    """
    domains = dataset.domains
    target = dataset.attributes.index(target_name)
    features = [dataset.attributes.index(name) for name in feature_names]

    orig_features = features # Don't think we really need it, but oh well

    

    def decision_tree_learning(examples, attrs, parent_examples=(), depth=0):
        """
        This function signature is written to match the pseudocode
        on p. 702 of Russell and Norvig. We recommend following that
        pseudocode to implement your decision tree.
        Note that we are adding an argument for the current depth, so you can
        keep track of the depth limit.

        This function should return the decision tree that has been learned.
        """

        # TODO: Implement the logic for learning the decision tree
        # You must also implement the entropy and information gain functions below.
        # We recommend adding your own helper functions below too, but don't remove
        # any of the provided code.
        tree = None

        print(str(depth) + " - " + str(len(examples)))


        if len(examples) == 0:  # no more examples in this set
            return Leaf(plurality_value(parent_examples, target))

        elif entropy(examples) == 0:   # if homogeneous
            return Leaf(plurality_value(examples, target))  # returns the classification (plurality value is the same as size of examples)
        
        elif entropy(examples) != 0 and depth == max_depth: # if reached max_depth without purity
            return Leaf(plurality_value(examples, target))
        
        elif len(attrs) == 0:
            return Leaf(plurality_value(examples, target))

        #if none of the above are true, we can create a Node

        A = get_max_importance(examples, attrs)

        tree = Node(A)
        
        #print('Splitting on ' + str(dataset.attributes[A]))
        
        children = split_on_attr_dict(examples, A)

        orig_list = copy.deepcopy(attrs)
        orig_list.remove(A)
        attr_name = dataset.attributes[A]

        
        for k, v in children.items():
            
            subtree = decision_tree_learning(v, orig_list, examples, depth + 1)

            tree.add_child(k, subtree)

        return tree

    

    def split_on_attr(examples, attribute):
        children = {}

        for possible_value in domains[attribute]:  # Create a list of each possible child
            children[possible_value] = list()

        
        for example in examples:
            children[example[attribute]].append(example)  # Add the record to suitable bucket
        

        children_list = []

        for key, value in children.items():
            children_list.append(value)

        return children_list
        

    def split_on_attr_dict(examples, attribute):

        children = {}

        for possible_value in domains[attribute]:  # Create a list of each possible child
            children[possible_value] = list()

        
        for example in examples:
            children[example[attribute]].append(example)  # Add the record to suitable bucket

        return children
            
        

    def plurality_value(examples, col):
        values = {}

        for possible_value in domains[col]:
            values[possible_value] = 0

        for example in examples:
            values[example[col]] += 1
        

        max = -1
        pl_value = None

        for k, v in values.items():
            if v > max:
                max = v
                pl_value = k
        
        return pl_value

    




    def get_max_importance(examples, attrs):



        attr = attrs[0]
        importance = -1000 # Some small value

        for attribute in attrs:
            children = split_on_attr(examples, attribute)

            ig = information_gain(examples, children)

            if ig > importance:  # if new information gain is more than current ig

                importance = ig
                attr = attribute
            
            elif ig == importance: # if new information is same as current ig, we break ties lexicographically
                
                if dataset.attributes[attribute].lower() < dataset.attributes[attr].lower():

                    attr = attribute
        

        return attr







    def entropy(examples):
        """Takes a list of examples and returns their entropy w.r.t. the target attribute"""
        possible_values = domains[target]
        bucket = [0 for _ in possible_values]

        for example in examples:
            bucket[possible_values.index(example[target])] += 1

        total_examples = sum(bucket)

        entropy = 0
        for el in bucket:
            p_el = el / total_examples

            entropy += (p_el * math.log2(p_el) if p_el != 0 else 0)
        
        #print(-entropy)
        return -entropy if entropy != 0 else entropy
        # TODO: Implement the entropy function
        

        pass

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
            if len(child) == 0:
                children_entropy.append(0)
            else:
                children_entropy.append(entropy(child))

        avg_entropy = 0
        for i in range(len(children)):
            avg_entropy += len_children[i]/total * children_entropy[i]
        
        
        return parent_entropy - avg_entropy
    
    

    # Finally...
    return decision_tree_learning(dataset.examples, features)


if __name__ == '__main__':
    """
    You can use this area to test your implementation and to generate
    output for the assignment. The autograder will ignore this area.
    """

    ############################
    ###### Example usage: ######
    ############################

    data = DataSet("./congress_small.csv")

    # An example of learning a decision tree to predict party affiliation
    # based on the values of votes 4-7
    t = learn_decision_tree(
        data,
        "class",
        ["vote35", "vote40", "vote18", "vote26", "vote32", "vote21", "vote1", "vote17", "vote11"],
        5
    )
    
    t.show()
