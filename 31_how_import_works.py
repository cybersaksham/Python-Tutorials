import sklearn as sk
import sys
from sklearn.ensemble import RandomForestClassifier
import T31_how_import_works_2  # Importing a custom file
from T31_how_import_works_2 import b

print(f"Version of sklearn is {sk.__version__}")  # Printing version of a module
print(f"path of sys is {sys.path}")  # Printing path of a module
print(RandomForestClassifier())

print(f"Value of a from source file is {T31_how_import_works_2.a}")  # Recommended
print(f"Value of b from source file is {b}")
T31_how_import_works_2.joke("Saksham")
