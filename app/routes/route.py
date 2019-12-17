import abc


class Route:
    @abc.abstractmethod
    def get_name(self):
        return ''

    @abc.abstractmethod
    def register(self):
        pass

    def __eq__(self, other):
        if isinstance(other, Route):
            return self.get_name() == other.get_name()

        return self.get_name() == other
