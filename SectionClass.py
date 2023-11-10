from ElementClass import Element


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
        for i in range(len(self.elements)):
            self.elements[i].print_method()



