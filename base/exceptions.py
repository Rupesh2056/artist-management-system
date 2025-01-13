class InvalidAttributeError(Exception):
    pass


class InvalidAttributeError(Exception):
    """Exception for invalid attribute while filtering Model """
    def __init__(self, attribute,model):
        super().__init__(f"invalid Attribute '{attribute}' for the Model '{model}'.")