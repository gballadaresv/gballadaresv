Class Component
    def operation
        raise NotImplementedError
    end
end

Class ConcreteComponent < Component
    def operation
        puts "Stock object operation"
    end
end

Class Decorator < Component
    attr_accesor :Component

    def initialize(component)
        @component = component
    end

    def operation
        @component.operation
    end
end

Class ConcreteDecoratorX < Decorator
    def operation
        puts "ConcreteDecoratorX operation over #{component.operation}"
    end
end
