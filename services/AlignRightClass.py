from services.AlignStrategyClass import AlignStrategy


class AlignRight(AlignStrategy):
    def render(self, textToBeArranged):
        tmp = textToBeArranged + " ##"
        return tmp