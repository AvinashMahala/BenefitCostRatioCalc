class Element:
    def __init__(self, nb_element, el_no, element_name, units):
        self.nb_element = nb_element
        self.el_no = el_no
        self.element_name = element_name
        self.units = units


class DeckElementsMData:
    def __init__(self):
        self.headers = ["NB Element", "El. No.", "Element Name", "Units"]
        self.elements = {
            "204": SubstructureElement("Substructures", 204, "204-Prestressed Concrete Column", "EACH"),
            "205": SubstructureElement("Substructures", 205, "205-Reinforced Concrete Column", "EACH"),
            "210": SubstructureElement("Substructures", 210, "210-Reinforced Concrete Pier Wall", "LENGTH ft."),
            "215": SubstructureElement("Substructures", 215, "215-Reinforced Concrete Abutment", "LENGTH ft."),
            "264": SubstructureElement("Substructures", 264, "264-Reinforced Concrete Retaining Wall", "Sq.ft"),
            "270": SubstructureElement("Substructures", 270, "270-Reinforced Concrete Wing Wall", "Each"),
            "233": SubstructureElement("Substructures", 233, "233-Prestressed Concrete Pier Cap", "LENGTH (ft.)"),
            "234": SubstructureElement("Substructures", 234, "234-Reinforced Concrete Pier Cap", "LENGTH (ft.)"),
        }

    def get_element(self, el_no):
        return self.elements.get(el_no, None)

    def get_elementsNumList(self):
        return list(self.elements.keys())

    def get_elementNamesList(self):
        return list(self.elements.values())
    
    def get_all_element_names(self):
        return [element.element_name for element in self.elements.values()]

    def get_headers(self):
        return self.headers
