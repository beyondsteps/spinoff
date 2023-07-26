from input import create_character
from layer import layer1, layer2, layer3

def main():
    player = create_character()
    layer1(player)
    # continue with the rest of the game layers

if __name__ == "__main__":
    main()