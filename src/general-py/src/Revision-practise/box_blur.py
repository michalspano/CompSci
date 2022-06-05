# Define main function
def main(*argv):

    # Using Pillow (PIL)
    from PIL import Image
    from PIL import ImageFilter

    # Proceed to the effect (box blur)
    input_file = Image.open(argv[0], "r")
    output_file = input_file.filter(ImageFilter.BoxBlur(argv[2]))
    output_file.save(argv[1])


# Define maine executable pathway
if __name__ == "__main__":

    # Define variables to be passed to the main function
    inputPath: str = input("Input PATH: ")
    outputPath: str = input("Output PATH: ")
    ratio: int = int(input("Filter ratio: "))

    #  Call the main function
    main(inputPath, outputPath, ratio)
