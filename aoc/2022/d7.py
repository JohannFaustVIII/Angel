from abc import ABC, abstractmethod


class Element(ABC):

    @abstractmethod
    def get_size(self):
        pass

class Directory(Element):

    def __init__(self, name : str, parent) -> None:
        super().__init__()
        self.name = name
        self.parent = parent
        self.elements = []

    def add_element(self, element : Element) -> None:
        self.elements.append(element)

    def contains_element(self, name : str) -> bool:
        for element in self.elements:
            if element.name == name:
                return True
        return False

    def get_size(self):
        return sum([element.get_size() for element in self.elements])

    def get_directory(self, name : str):
        for element in self.elements:
            if element.name == name:
                return element

    def get_part_1(self) -> int:
        size = 0
        if self.get_size() < 100000:
            size += self.get_size()
        
        for element in self.elements:
            if isinstance(element, Directory):
                size += element.get_part_1()
        
        return size

    def get_part_2(self, size_required_to_delete : int = None) -> int:
        if self.name == "/":
            size_required_to_delete = self.get_size() - 40_000_000

        min_size = 70_000_000
        my_size = self.get_size()

        if my_size >= size_required_to_delete and my_size < min_size:
            min_size = my_size

        for element in self.elements:
            if isinstance(element, Directory):
                dir_size = element.get_part_2(size_required_to_delete)
                if dir_size < min_size:
                    min_size = dir_size

        return min_size
        

class File(Element):
    
    def __init__(self, size : int, name : str, parent : Directory) -> None:
        super().__init__()
        self.size = size
        self.name = name
        self.parent = parent

    def get_size(self):
        return self.size


current_directory = None
main_directory = None

with open("aoc/2022/d7.input") as file:
    lines = file.readlines()

    for line in lines:
        parts = line.strip().split()

        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    current_directory = current_directory.parent
                else:
                    if parts[2] == "/":
                        if not main_directory:
                            main_directory = Directory(parts[2], None)
                        current_directory = main_directory
                    else:
                        current_directory = current_directory.get_directory(parts[2])
        else:
            if parts[0] == "dir":
                if not current_directory.contains_element(parts[1]):
                    element = Directory(parts[1], current_directory)
                    current_directory.add_element(element)
            else:
                if not current_directory.contains_element(parts[1]):
                    size = int(parts[0])
                    element = File(size, parts[1], current_directory)
                    current_directory.add_element(element)
                

print(main_directory.get_part_1())
print(main_directory.get_size())
print(main_directory.get_part_2())