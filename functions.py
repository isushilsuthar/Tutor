def mcq(subject):
    m = {
        "Maths": """
            [
                {{
                    "question": "Solve the following equation for \\(x\\): \\(3x^2 - 5x + 2 = 0\\)",
                    "options": {{
                        "A": "\\(x = \\frac{1}{3}, \\frac{2}{3}\\)",
                        "B": "\\(x = 1, 2\\)",
                        "C": "\\(x = -1, -2\\)",
                        "D": "\\(x = -\\frac{1}{3}, -\\frac{2}{3}\\)"
                    }},
                    "answer": "A"
                }},
                {{
                    "question": "Simplify the expression: \\(4a^2b^3 \\div (ab)^2\\)",
                    "options": {{
                        "A": "\\(4b\\)",
                        "B": "\\(4ab\\)",
                        "C": "\\(4a^2b\\)",
                        "D": "\\(4b^3/a\\)"
                    }},
                    "answer": "A"
                }}
            ]
""",
        "Physics": """
            [
                {{
                    "question": "What is the SI unit of force?",
                    "options": {{
                        "A": "Newton",
                        "B": "Joule",
                        "C": "Pascal",
                        "D": "Watt"
                    }},
                    "answer": "A"
                }},
                {{
                    "question": "State the law of conservation of momentum.",
                    "options": {{
                        "A": "Momentum is always conserved.",
                        "B": "In an isolated system, the total momentum before collision is equal to the total momentum after collision.",
                        "C": "Momentum can neither be created nor destroyed.",
                        "D": "Momentum is the product of mass and velocity."
                    }},
                    "answer": "B"
                }}
            ]
""",
        "Chemistry": """
            [
                {{
                    "question": "What is the chemical formula for water?",
                    "options": {{
                        "A": "H2O",
                        "B": "CO2",
                        "C": "O2",
                        "D": "NaCl"
                    }},
                    "answer": "A"
                }},
                {{
                    "question": "State the law of conservation of mass.",
                    "options": {{
                        "A": "Mass can neither be created nor destroyed.",
                        "B": "Energy can neither be created nor destroyed.",
                        "C": "The mass of reactants is always equal to the mass of products in a chemical reaction.",
                        "D": "Mass and energy are interchangeable."
                    }},
                    "answer": "C"
                }}
            ]
""",
        "Biology":"""
            [
                {{
                    "question": "What is the powerhouse of the cell?",
                    "options": {{
                        "A": "Nucleus",
                        "B": "Mitochondria",
                        "C": "Ribosome",
                        "D": "Endoplasmic Reticulum"
                    }},
                    "answer": "B"
                }},
                {{
                    "question": "Describe the process of photosynthesis.",
                    "options": {{
                        "A": "Conversion of light energy into chemical energy by plants.",
                        "B": "Absorption of nutrients from soil by roots.",
                        "C": "Respiration in plants.",
                        "D": "Transpiration in leaves."
                    }},
                    "answer": "A"
                }}
            ]
"""
    }
    return m[subject]


#####################################################################

def tf(subject):
    m = {
        "Maths": """
            [
                {{
                    "question": "The square root of 16 is 4.",
                    "answer": "True"
                }},
                {{
                    "question": "The sum of angles in a triangle is 180 degrees.",
                    "answer": "True"
                }}
            ]
""",
        "Physics": """
            [
                {{
                    "question": "Acceleration due to gravity on Earth is approximately 9.8 m/s².",
                    "answer": "True"
                }},
                {{
                    "question": "Sound travels faster in air than in water.",
                    "answer": "False"
                }}
            ]
""",
        "Chemistry": """
            [
                {{
                    "question": "Water is composed of two hydrogen atoms and one oxygen atom.",
                    "answer": "True"
                }},
                {{
                    "question": "An acid has a pH greater than 7.",
                    "answer": "False"
                }}
            ]
""",
        "Biology": """
            [
                {{
                    "question": "DNA is found in the nucleus of a cell.",
                    "answer": "True"
                }},
                {{
                    "question": "Photosynthesis occurs in the mitochondria of plant cells.",
                    "answer": "False"
                }}
            ]
"""
    }
    return m[subject]

#####################################################################

def SA(subject):
    m = {
        "Maths": """
            [
                {{
                    "question": "Solve for x: \\(2x + 3 = 11\\)",
                    "answer": "Subtract 3 from both sides to get \\(2x = 8\\), then divide by 2 to find \\(x = 4\\)."
                }},
                {{
                    "question": "Find the derivative of \\(f(x) = x^2 + 3x + 2\\)",
                    "answer": "Use the power rule: \\(f'(x) = 2x + 3\\)."
                }}
            ]
""",
        "Physics": """
            [
                {{
                    "question": "Calculate the force acting on an object of mass 5 kg accelerating at 2 m/s².",
                    "answer": "Use Newton's second law: \\(F = ma\\). Here, \\(F = 5 \\times 2 = 10\\, \\text{N}\\)."
                }},
                {{
                    "question": "Explain the concept of inertia.",
                    "answer": "Inertia is the property of an object to resist changes in its state of motion. It depends on the mass of the object."
                }}
            ]
""",
        "Chemistry": """
            [
                {{
                    "question": "Calculate the number of moles in 22 grams of CO2. (Molar mass of CO2 = 44 g/mol)",
                    "answer": "Use the formula: \\(\\text{moles} = \\frac{\\text{mass}}{\\text{molar mass}}\\). Here, \\(\\text{moles} = \\frac{22}{44} = 0.5\\, \\text{moles}\\)."
                }},
                {{
                    "question": "Describe the process of electrolysis.",
                    "answer": "Electrolysis is a chemical process that uses electrical energy to cause a non-spontaneous chemical reaction. Commonly used for the extraction of metals and electroplating."
                }}
            ]
""",
        "Biology": """
            [
                {{
                    "question": "Calculate the magnification of a microscope if the objective lens is 40x and the eyepiece lens is 10x.",
                    "answer": "Multiply the magnifications: Total magnification = 40 \\times 10 = 400x."
                }},
                {{
                    "question": "Explain the role of chlorophyll in photosynthesis.",
                    "answer": "Chlorophyll is a pigment in plants that absorbs light energy, which is then used to convert carbon dioxide and water into glucose and oxygen during photosynthesis."
                }}
            ]
"""
    }
    return m[subject]

###############################################################

def LA(subject):
    m = {
        "Maths": """
            [
                {{
                    "question": "Explain the process of solving a system of linear equations using the Gaussian elimination method.",
                    "answer": "1. Write the system of equations in augmented matrix form.\n2. Perform row operations to transform the matrix into row echelon form.\n3. Continue row operations to obtain reduced row echelon form.\n4. Back-substitute to find the solutions for the variables.\nExample: Solve the system:\n\\[\\begin{cases} 2x + 3y - z = 1 \\\\ 4x + y + 2z = 2 \\\\ -x + y + 2z = -1 \\end{cases}\\]"
                }},
                {{
                    "question": "Discuss the applications of calculus in real life.",
                    "answer": "1. Physics: Calculus is used to find the rate of change of quantities, such as velocity and acceleration.\n2. Engineering: Calculus is used in designing curves and calculating areas and volumes.\n3. Medicine: Calculus helps in modeling the growth of tumors and the spread of diseases.\n4. Economics: Calculus is used to find the maximum profit and minimum cost in optimization problems."
                }}
            ]
""",
        "Physics": """
            [
                {{
                    "question": "Derive the equations of motion for an object under uniform acceleration.",
                    "answer": "1. Start with the definitions of velocity and acceleration: \\(v = u + at\\), \\(s = ut + \\frac{1}{2}at^2\\), and \\(v^2 = u^2 + 2as\\).\n2. Derive each equation step by step using calculus or algebraic methods.\n3. Provide examples of their applications in real-world scenarios, such as projectile motion and free fall."
                }},
                {{
                    "question": "Explain the theory of relativity and its implications.",
                    "answer": "1. Special Relativity: Discuss Einstein's postulates, time dilation, length contraction, and mass-energy equivalence (\\(E = mc^2\\)).\n2. General Relativity: Explain the concept of spacetime curvature and its impact on gravity.\n3. Applications: GPS systems, black holes, and cosmology."
                }}
            ]
""",
        "Chemistry": """
            [
                {{
                    "question": "Describe the process of fractional distillation and its applications.",
                    "answer": "1. Define fractional distillation and its principle based on differences in boiling points.\n2. Describe the setup: distillation column, heat source, condenser, and collection of fractions.\n3. Steps: Heating, vaporization, condensation, and collection.\n4. Applications: Separation of crude oil into fractions, production of high-purity chemicals, and alcohol distillation."
                }},
                {{
                    "question": "Explain the chemical bonding theories: VSEPR, Valence Bond Theory, and Molecular Orbital Theory.",
                    "answer": "1. VSEPR Theory: Predicts molecular shapes based on electron pair repulsion.\n2. Valence Bond Theory: Describes bonding through the overlap of atomic orbitals.\n3. Molecular Orbital Theory: Explains bonding by combining atomic orbitals to form molecular orbitals, including bonding and antibonding orbitals.\n4. Compare and contrast these theories with examples."
                }}
            ]
""",
        "Biology": """
            [
                {{
                    "question": "Describe the process of DNA replication and its significance.",
                    "answer": "1. Explain the structure of DNA and the role of enzymes like helicase, DNA polymerase, and ligase.\n2. Steps: Initiation, elongation, and termination.\n3. Importance: Ensures genetic continuity, allows for cell division, and supports growth and repair.\n4. Errors in replication and their consequences: Mutations, cancer, and genetic disorders."
                }},
                {{
                    "question": "Discuss the process of evolution by natural selection.",
                    "answer": "1. Define evolution and natural selection.\n2. Mechanisms: Variation, competition, adaptation, and survival of the fittest.\n3. Evidence: Fossil records, comparative anatomy, genetic similarities, and observed instances of natural selection.\n4. Examples: Darwin's finches, antibiotic resistance in bacteria, and peppered moths."
                }}
            ]
"""
    }
    return m[subject]



def generate_example(question_type, subject):
    if question_type == "Multiple Choice": return mcq(subject)
    if question_type == "True/False": return tf(subject)
    if question_type == "Short Answers": return SA(subject)
    if question_type == "Long Answers": return LA(subject)



############################ PARSER FUNCTIONS HERE ##########################################

import json

def parse_mcq(json_str):
    parsed_data = json.loads(json_str)

    questions = []
    options_A = []
    options_B = []
    options_C = []
    options_D = []
    answers = []

    for question_data in parsed_data['questions']:
        questions.append(question_data['question'])
        options_A.append(question_data['options'][0])
        options_B.append(question_data['options'][1])
        options_C.append(question_data['options'][2])
        options_D.append(question_data['options'][3])
        answers.append(question_data['answer'])

    return questions, options_A, options_B, options_C, options_D, answers

def parse_questions_answers(json_string):
    questions = []
    answers = []
    data = json.loads(json_string)
    for item in data:
        questions.append(item["question"])
        answers.append(item["answer"])
    return questions, answers

#################################################################################################################

