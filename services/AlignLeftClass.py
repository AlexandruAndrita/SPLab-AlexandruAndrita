from services.AlignStrategyClass import AlignStrategy


class AlignLeft(AlignStrategy):
    def render(self, textToBeArranged):
        tmp = "## " + textToBeArranged
        return tmp
