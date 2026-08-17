class Valuechecker:

    

    @staticmethod
    def name_check(value):
        
        if not value.isalpha():
            return False
        return True

    @staticmethod
    def number_check(value):
        if not value or not value.strip():
            return False
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def email_check(value):
        if not value or not value.strip():
            return False
        if "@" not in value or "." not in value:
            return False
        return True