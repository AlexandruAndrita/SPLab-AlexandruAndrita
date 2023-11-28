from AlignStrategyClass import AlignStrategy


class AlignCenter(AlignStrategy):
    def render(self, textToBeArranged):
        tmp = "## "+ textToBeArranged + " ##"
        return tmp