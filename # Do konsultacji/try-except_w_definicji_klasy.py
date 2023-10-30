class Type:
    def __init__(self):
        try:
            self.input_file = argv[1]
            self.output_file = argv[2]
            self.changes_list = argv[3:]
        except IndentationError:
            print("Błąd - Niewłaściwa ilość podanych argumentów.")
            exit()

"""
Czy pisze się Try-Except w definicji klasy, czy definitywnie już potem w kodzie dla obiektu?
"""
