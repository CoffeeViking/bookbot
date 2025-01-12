def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    letters = []
    dict = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}
    for char in file_contents:
        if char not in dict.keys():
            pass
        else:
            dict[char.lower()] += 1
    print(len(words), "words found in document.")
    for key in dict:
        print("The", key, "character was found", dict[key], "times")

main()