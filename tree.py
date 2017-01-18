# Taken from UChicago CS121 Treemap assignment                                                                               
# https://classes.cs.uchicago.edu/archive/2016/fall/12100-1/pa/pa7/index.html.

class TreeNode:

    def  __init__(self, code, label, weight):
        '''
        construct a Tree node

        Inputs:
            code: (string) a code that identifies the type of the node
            label: (string) a label that identifies the node
            weight: (float) an application specific weight
        '''
        self._code = code
        self._label = label
        self._weight = weight
        self._children = {}

    @property
    def code(self):
        return self._code

    @property
    def label(self):
        return self._label

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    def get_children_as_dict(self):
        return self._children

    def get_children_as_list(self):
        return [self._children[x] for x in sorted(self._children)]

    
    def print_tree(self, tabs=""):
        s = "{}{} {} {:d}".format(tabs, self.code, self.label, self.weight)
        print(s)
        for key in sorted(self._children):
            self._children[key].print_tree(tabs+"    ")
