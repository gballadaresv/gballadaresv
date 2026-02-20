class Subject
    def add_observer
        raise NotImplementedError
    end

    def remove_observer
        raise NotImplementedError
    end

    def notify
        raise NotImplementedError
    end
end

class ConcreteSubject < Subject
    attr_accesor :state

    def initialize
        @observers = []
    end

    def add_observer(observer)
        @observers << observer
    end

    def remove_observer
        @observer.delete(observer)
    end

    def notify
        puts "notifying observers"
        @observers.each { |observer| observer.update(self)}
    end

    def do_something
        puts "I'm doing something, my state just changed"
        @state = rand(0..10)
        notify
    end
end

class Observer < Subject
    def update(_subject)
        raise NotImplementedError
    end
end

class ConcreteObserverX < Observer
    def update(subject)
        # Revisa alguna condición para reaccionar ante un cambio de estado
        return unless subject.state
    end
end




