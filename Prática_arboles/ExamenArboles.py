 class Node:
    def __init__(self, value):
        self.value= value
        self.rightS= None
        self.leftS= None
        
def crear_arbol()-> None:
    while True:
        number_nodes= input("Por favor ingrese la cantidad de nodos que desea crear: ")
        number_nodes= number_nodes.lower()
        if number_nodes == "-1":
            nodes= []
            while True:
                value= input("Por favor ingresa el valor del nodo (X para detener): ")
                value= value.lower()
            
                if value.isdigit():
                    nodes.append(int(value))
                
                elif value == "x":
                    print(nodes)
                    print("Chaitooooo")
                    break

                else:
                    print("El valor ingresado no es válido")
                        
            return build_tree(nodes)
        
        elif number_nodes =="0":
            return None
        elif number_nodes== ("x"or "X"):
            print("Cansón mor, haga alguito con el programa ome")
            break
        else: 
            if number_nodes.isdigit() and int(number_nodes) >0:
                number_nodes = int(number_nodes)
                nodes= []
                for _ in range(number_nodes):
                    value= input(f"Por favor ingresa el valor para el nodo {len(nodes)+1}, (X para detener):  ")
                    value= value.lower()
                    if value.isdigit():
                        nodes.append(int(value))
                     
                    elif value == "x":
                        if nodes== 0:
                            return None
                        else:
                            print(f"Los nodos que creaste son: {nodes}")
                            print("Chao chao")
                        break
                    else:
                        print("El valor ingresado no es válido.")  
                return build_tree(nodes)    
                       
            
def build_tree(nodes) -> Node:
    tree= None
    for value in nodes:
        tree= insert_nodes(tree, value)
    return tree

def insert_nodes(root, value) -> Node:
    if root is None:
        return Node(value)
    elif value <root.value:
        root.leftS= insert_nodes (root.leftS, value)
    elif value > root.value:
        root.rightS= insert_nodes(root.rightS, value)
    return root 


def menu_arbol(nodo) -> None:
    while True:
        print("\n")
        print("\nMenú del Árbol:")
        print("Estos son los recorridos disponibles:")
        print("1. PostOrder")
        print("2. PreOrder")
        print("3. InOrder")
        print("4. Número de Hojas")
        print("5. Altura del Árbol")
        print("6. Es completo?")
        print("7. Número de Nodos")
        print("8. Salir")
        print("9. Balancear")
        opcion = input("Seleccione una opción: ")
        print("\n")
        
        if opcion == "1":
            print("Recorrido PostOrder:")
            recorrido_postorder(nodo)
        elif opcion == "2":
            print("Recorrido PreOrder:")
            recorrido_preorder(nodo)
        elif opcion == "3":
            print("Recorrido InOrder:")
            recorrido_inorder(nodo)
        elif opcion == "4":
            print("Número de Hojas:", contar_hojas(nodo))
        elif opcion == "5":
            print("Altura del Árbol:", altura_arbol(nodo))
        elif opcion == "6":
            if es_completo(nodo):
                print("El árbol es completo.")
            else:
                print("El árbol no es completo.")
        elif opcion == "7":
            print("Número de Nodos:", contar_nodos(nodo))  
            
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
def recorrido_preorder(nodo) -> None:
    if nodo is not None:
        print(nodo.value, end=" ")
        recorrido_preorder(nodo.leftS)
        recorrido_preorder(nodo.rightS)
        
def recorrido_inorder(nodo) -> None:
    if nodo is not None:
        recorrido_inorder(nodo.leftS)
        print(nodo.value, end=" ")
        recorrido_inorder(nodo.rightS)

def recorrido_postorder(nodo) -> None:
    if nodo is not None:
        recorrido_postorder(nodo.leftS)
        recorrido_postorder(nodo.rightS)
        print(nodo.value, end=" ")
        
def contar_hojas(nodo) -> None:
    if nodo is None:
        return 0
    if nodo.leftS is None and nodo.rightS is None:
        return 1
    return contar_hojas(nodo.leftS) + contar_hojas(nodo.rightS)

def altura_arbol(nodo) -> None:
    if nodo is None:
        return 0
    left_height = altura_arbol(nodo.leftS)
    right_height = altura_arbol(nodo.rightS)
    return max(left_height, right_height) + 1

def contar_nodos(nodo) -> None:
    if nodo is None:
        return 0
    return contar_nodos(nodo.leftS) + contar_nodos(nodo.rightS) + 1

def es_completo(nodo) -> None:
    if nodo is None:
        return True
    elif nodo.leftS is None and nodo.rightS is None:
        return True
    elif nodo.leftS is not None and nodo.rightS is not None:
        return es_completo(nodo.leftS ) and es_completo(nodo.rightS)
    return False
                
def imprimir(nodo, prefix="", is_left=True) -> None:
    if not nodo:
      print("Empty Tree")
      return
    if nodo.rightS:
      imprimir(nodo.rightS, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(nodo.value))
    if nodo.leftS:
      imprimir(nodo.leftS, prefix + ("    " if is_left else "│   "), True)      

if __name__ == "__main__":    
    p= crear_arbol()
    imprimir(p)
    menu_arbol(p)
