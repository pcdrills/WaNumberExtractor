class Saver:
    def __init__(self):
        pass

    #Creates a text file and stores the output to it
    def save(self, numbers):
        output_file = "output.txt"
        with open(output_file, mode="w") as output:
            output.writelines((str(nums)+'\n' for nums in numbers))
            