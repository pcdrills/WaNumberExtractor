class Cleaner:
    def __init__(self):
        self.cleaned_numbers = []

    # Cleanup each phone number and remove character encodings
    # Cleanup the Encoding from the numbers
    def cleanup(self, inp):
        new_char = ""
        for char in inp:
            if char not in ["\u202a", "\u202c"]:
                new_char += char
        new_char = new_char.replace(u'\xa0', u' ')
        return new_char   

    # Get hold of just the cleaned phone numbers and return a list of cleaned_numbers
    def clean(self, number_list):
        for phone_number in number_list:
            cleaned = self.cleanup(phone_number)
            self.cleaned_numbers.append(cleaned)
        return self.cleaned_numbers