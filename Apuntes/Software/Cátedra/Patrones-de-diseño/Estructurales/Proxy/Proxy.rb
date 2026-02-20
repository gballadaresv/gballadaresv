Class Subject
    def operation
        raise NotImplementedError
    end
end

Class Service < Subject
    def operation
        puts "Service operation"
    end
end

Class Proxy < Subject
    def initialize(service)
        @service = service
    end

    # No retorna nada a menos que pase las verificaciones
    def operation
        return unless check_access

        # Si pasa las verificaciones permite la ejecución del servicio
        @real_service.operation

        # Luego de ejecutar el servicio, se puede ejecutar lógica adicional del proxy
        proxy_operation
    end

    def check_access
        puts "Checking access"
        true
    end

    def proxy_operation
        puts "Proxy operation"
    end
end