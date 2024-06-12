def main():
    with open("./books/frankenstein.txt") as f:
        print(f"--- Begin report of {f.name[2::]} ---")
        d = dict()
        file_contents = f.read()
        words = file_contents.split()
        print(f"{len(words)} words found in the document\n")
        for word in words:
            for letter in word:
                if letter.isalpha():
                    if letter.lower() in d.keys():
                        d[letter.lower()] += 1
                    else:
                        d[letter.lower()] = 1
        sorted_keys = sorted(d, key=d.get)
        sorted_keys.reverse()
        for letter in sorted_keys:
            print(f"The '{letter}' character was found {d[letter]} times")
        print("--- End report ---")
                
        


main()

