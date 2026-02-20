Class Component
    def parent
        @parent
    end

    # Setter (opcional), puede implementar la opción de cambiar el nodo padre
    def parent=(parent)
        @parent = parent
    end

    def add(component)
        raise NotImplementedError
    end

    def remove(component)
        rails NotImplementedError
    end

    # (Opcional) Se puede definir un método booleano que determine si un nodo es hoja
    def composite?
        false
    end

    # (Opcional) El componente base puede implementar alguna lógica por defecto
    def operation
        raise NotImplementedError
    end
end

Class Leaf
    def operation
        puts 'Doing something'
    end
end

Class Composite > Component
    def initialize
        @children = []
    end

    def add(component)
        @children << component
        component.parent = self
    end

    def remove(component)
        @children.remove(component)
        component.parent = nil
    end

    def composite?
        true
    end

    # La estructura de la operación depende de lo que se quiera retornar, pero DEBE ser traspasar la operación a los hijos (recursión)
    def operation
        results = []
        @children.each { |child| results << child.operation }
    end
end
