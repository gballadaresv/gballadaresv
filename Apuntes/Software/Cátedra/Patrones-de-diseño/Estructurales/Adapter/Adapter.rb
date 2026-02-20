Class Target
    def request
        # Puede ser abstracto o definir un comportamiento por defecto
        puts "Target: The default target's behavior."
    end
end

Class Adaptee
    def specific_request
        puts "data from Adaptee"
    end
end

Class Adapter < Target
    def initialize(adaptee)
        # Nótese que hereda de Target y posee una dependencia de adaptee
        @adaptee = adaptee
    end

    def request
        puts "Translated: #{@adaptee.specific_request} (translated)"
    end
end


