Class Factory
    def create
        rails NotImplementedError
    end
end

Class FactoryA < Factory
    def create
        Product1.new
    end
end

Class FacotryB < Facotry
    def create
        Product2.new
    end
end

Class Product
    def do_something
        rails NotImplementedError
    end
end

Class Product1 < Product
    def do_something(product1)
        puts "Product1 = #{product1}"
    end
end

Class Product2 < Product
    def do_something(product2)
        puts "Product2 = #{product2}"
    end
end