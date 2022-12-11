#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import pickle
from os import path


# TODO: Définissez vos fonction ici
def compare_files(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2, encoding="utf-8") as f2:
        for count, line1 in enumerate(f1):
            line2 = f2.readline()
            if line1 != line2:
                print(f"The files are not identical. Line {count + 1} is different.")
                print(line1)
                print("Is not the same as:")
                print(line2)

                return

    print("The files are identical")

def add_spaces(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2, "w", encoding="utf-8") as f2:
        f2.write(f1.read().replace(" ", "   "))

def convert_to_letter(note_path, result_file_path):
    with open(note_path, encoding="utf-8") as note_file:
        notes_percent = note_file.readlines()  # To get rid of \n: note_file.read().splitlines()

    with open(result_file_path, "w", encoding="utf-8") as result_file:
        for note in notes_percent:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0] <= int(note) < value[1]:
                    result_file.write(note.strip() + " " + key + "\n")
                    break
def delete_recipe(recipes_path):
    with open(recipes_path, "rb") as f:
        recipes = pickle.load(f)

    name = input("Entrez le nom de la recette que vous voulez supprimer.\n")

    if name in recipes:
        del recipes[name]
        print("La recette est supprimée!")
    else:
        print("Cette recette n'existe pas!")

    with open(recipes_path, "wb") as f:
        pickle.dump(recipes, f)

def exercice4(recipes_path):
    with open(recipes_path, "rb") as f:
        recipes = pickle.load(f)

    print("Voici les recettes disponibles:")
    for recipe in recipes:
        print(recipe)

    name = input("Entrez le nom de la recette que vous voulez afficher.\n")

    if name in recipes:
        print_recipe(recipes[name])
    else:
        print("Cette recette n'existe pas!")

def exercice5(recipes_path):
    with open(recipes_path, "rb") as f:
        recipes = pickle.load(f)

    recipes = add_recipes(recipes)

    with open(recipes_path, "wb") as f:
        pickle.dump(recipes, f)


def exercice6(recipes_path):
    with open(recipes_path, "rb") as f:
        recipes = pickle.load(f)

    name = input("Entrez le nom de la recette que vous voulez afficher.\n")

    if name in recipes:
        print_recipe(recipes[name])
    else:
        print("Cette recette n'existe pas!")
        
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compare_files("file1.txt", "file2.txt")
    add_spaces("file1.txt", "file2.txt")
    convert_to_letter("notes.txt", "notes_lettres.txt")
    add_recipe("recettes.p")

    pass
