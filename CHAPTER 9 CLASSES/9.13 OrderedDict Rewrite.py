from collections   import OrderedDict

glossary = OrderedDict

glossary = {
    "Variable": "A variable is a reserved memory location to store values.",
    "Function": "A function is a block of organized, reusable code that is used to perform a single, related action.",
    "Script": "A script is a collection of commands in a file designed to be executed like a program.",
    "Class": "A class is a code template for creating objects.",
    "Dictionary": "A dictionary is a collection which is unordered, changeable and indexed.",
    "Docstring": "A docstring is a string literal that we use to explain the functionality of a class, function, or module.",
    "Decorator": "A decorator is a function that returns another function, or wraps it.",
    "F-string": "An f-string is a formatted string literal.",
    "Importer": "The importer is an object that finds and loads a module.",
    "Iterator": "An iterator is an object that represents a stream of data.",
    }

for word,definition in glossary.items():
    print(f"{word}:{definition}")