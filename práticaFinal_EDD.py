#En el orden inorden se recorre de la siguiente manera: subárbol izquierdo, raíz, subárbol derecho.
class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.root = None
        self.left_S = None
        self.right_S = None

def callback(node)-> int:
    print(node.value)
    
def recorrido_in_order(root, callback)-> None:
    stack = []
    current_node = root
    
    while current_node or stack:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left_S

        current_node = stack.pop()
        callback(current_node)
        current_node = current_node.right_S
        
node_1 = BinaryNode(1)
node_2 = BinaryNode(2)
node_3 = BinaryNode(3)
node_4 = BinaryNode(4)
node_5 = BinaryNode(6)
node_6 = BinaryNode(7)
node_7 = BinaryNode(9)

node_1.left_S = node_2
node_1.right_S = node_3
node_2.root = node_1
node_3.root = node_1

node_2.left_S = node_4
node_2.right_S = node_5
node_4.root = node_2
node_5.root = node_2

node_3.right_S = node_6
node_6.root = node_3

node_4.right_S = node_7
node_7.root = node_4


recorrido_in_order(node_1, callback)
