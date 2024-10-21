import inquirer
import numpy as np


def get_user_input():
    # Define the questions for user input with descriptive units
    questions = [
        inquirer.Text("Clump", message="Clump Thickness"),
        inquirer.Text("UnifSize", message="Uniformity of Cell Size"),
        inquirer.Text("UnifShape", message="Uniformity of Cell Shape"),
        inquirer.Text("MargAdh", message="Marginal Adhesion"),
        inquirer.Text("SingEpiSize", message="Single Epithelial Cell Size"),
        inquirer.Text("BareNuc", message="Bare Nuclei"),
        inquirer.Text("BlandChrom", message="Bland Chromatin"),
        inquirer.Text("NormNucl", message="Normal Nucleoli"),
        inquirer.Text("Mit", message="Mitoses"),
    ]

    # Prompt the user for input
    answers = inquirer.prompt(questions)

    # Convert the answers to a numpy array
    new_data = np.array(
        [
            [
                int(answers["Clump"]),
                int(answers["UnifSize"]),
                int(answers["UnifShape"]),
                int(answers["MargAdh"]),
                int(answers["SingEpiSize"]),
                int(answers["BareNuc"]),
                int(answers["BlandChrom"]),
                int(answers["NormNucl"]),
                int(answers["Mit"]),
            ]
        ]
    )

    return new_data
