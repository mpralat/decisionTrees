import math

def read_and_parse(input_file):
    banknotes = []
    with open(input_file) as f:
        for i, line in enumerate(f):
            attributes = [float(x) for x in line.rstrip().split(",")]
            banknotes.append(attributes)
    return banknotes

def gini_index(groups):
    '''
    :param groups: a list of groups of elements we obtained from the dataset after the split. 
    Each element's last position should be its assigned class.
    :return:  value of the Gini index
    '''
    gini_value = 0.0
    # Get all of the possible class values for the items in the groups
    classes = set(item[-1] for sublist in groups for item in sublist)
    for group in groups:
        for class_val in classes:
            # Count how many examples of all classes are in each group
            if (len(group) == 0):
                continue
            how_many_in_class = [item[-1] for item in group].count(class_val)
            proportion = how_many_in_class / float(len(group))
            # 1.0 - proportion is the probability of failure - so, how many examples from the group are not in our class
            gini_value += (proportion * (1.0 - proportion))

    return gini_value

def split_group_by_attribute(attribute_index, threshold_value, data):
    smaller, bigger = [],[]

    for example in data:
        if example[attribute_index] < threshold_value:
            smaller.append(example)
        else:
            bigger.append(example)
    return smaller, bigger

def get_the_best_split(dataset):
    '''
    We check each attribute and each value to get the best split.
    '''
    best_attr_index = math.inf
    best_gini_index = math.inf
    best_split_value = math.inf
    best_groups = None
    for attribute_index in range(len(dataset[0])-1):
        for example in dataset:
            splitted_groups = split_group_by_attribute(attribute_index, example[attribute_index], dataset)
            gini = gini_index(splitted_groups)
            if gini < best_gini_index:
                best_gini_index = gini
                best_attr_index = attribute_index
                best_groups = splitted_groups
                best_split_value = example[attribute_index]
    return {'attribute_index' : best_attr_index, 'value':best_split_value, 'groups' : best_groups }




def main():
    banknotes = read_and_parse("data.txt")
    print(banknotes[0])



if __name__=="__main__":
    # dataset = [[2.771244718, 1.784783929, 0],
    #            [1.728571309, 1.169761413, 0],
    #            [3.678319846, 2.81281357, 0],
    #            [3.961043357, 2.61995032, 0],
    #            [2.999208922, 2.209014212, 0],
    #            [7.497545867, 3.162953546, 1],
    #            [9.00220326, 3.339047188, 1],
    #            [7.444542326, 0.476683375, 1],
    #            [10.12493903, 3.234550982, 1],
    #            [6.642287351, 3.319983761, 1]]
    #
    dataset = read_and_parse("data.txt")
    split = get_the_best_split(dataset)
    print('Split: [X%d < %.3f]' % ((split['attribute_index'] + 1), split['value']))
    print(str(len(split['groups'][0])) + " " +  str(len(split['groups'][1])))
