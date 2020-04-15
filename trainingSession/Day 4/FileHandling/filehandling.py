'''
More code is present in the jupyter notebook
'''
with open("test.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
    print("Is Writable: ", f.writable())
    print("Is Seekable: ", f.seekable())
    print("Is Atty: ", f.isatty())
