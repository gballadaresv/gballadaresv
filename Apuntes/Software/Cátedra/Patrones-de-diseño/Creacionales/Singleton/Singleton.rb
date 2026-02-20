Class Singleton
    @@instance = nil

    def self.instance
        @@instance ||= new
    end

    def do_something
        puts 'Doing something...'
    end

    private_class_method :new
end
