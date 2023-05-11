
class Validator:
    def __init__(self):
        self.cmrNumbers = []


    # nws = number without space 
    # Validate a cameroon number and return it without spaces
    def cmr_validator(self, number):
        nws = number.replace(" ", "")
        if (len(nws) != 13):
            complete_number = nws[:4] + "6" + nws[4:]
        else:
            complete_number = nws
        return complete_number


    # Checks where the phone number belongs to and who to validate it
    # And returns a list of the validated numbers
    def validate(self, numbers):
        for number in numbers:
            begins_with = number[:4]
            if (begins_with == "+237"):
                cmr = self.cmr_validator(number)
                self.cmrNumbers.append(cmr)
                
            else:
                pass
        
        return self.cmrNumbers
        # print(cmrNumbers)

# val = Validator()
# print(val.validate(numbers))
