from models.ElementClass import Element


class Section(Element):
    def __init__(self, section_name):
        self.section_name = section_name
        self.elements = []

    def get_section_name(self):
        return self.section_name

    def add(self,element_to_be_added):
        self.elements.append(element_to_be_added)

    def remove(self,element_to_be_removed):
        self.elements.remove(element_to_be_removed)

    def get(self,index):
        if index<0 or index>len(self.elements)-1:
            raise IndexError(f"Index given {index} is not correct")
        return self.elements[index]

    def print_method(self,print_section_name=True):
        if print_section_name:
            print(self.section_name)
        """
        commented this loop because otherwise while going through the list of elements in accept
        the inherited ones (the children) will be printed twice
        """
        # for i in range(len(self.elements)):
            # self.elements[i].print_method()

    def accept(self,visitor):
        """
        should be omitted for statistics
        """
        visitor.visit_section(self)

        for element in self.elements:
            element.accept(visitor)

