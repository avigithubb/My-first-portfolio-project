mores = {"properties": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U", "V", "X", "Y", "Z"],
         "mores": ["*-", "-***", "-*-*", "-**", "*", "**-*", "--*", "****", "**", "*---", "-*-", "*-**", "*-**", "--",
                   "-*", "---", "*--*", "--*-", "*-*", "***", "-", "**-", "***-", "*--", "-**-", "-*--", "--**"]}
summed_mores = ""


def get_mores_code(sent):
    global summed_mores
    for char in sent:
        if char.upper() in mores['properties']:
            code_ind = mores['properties'].index(char.upper())
            summed_mores = summed_mores + mores['mores'][code_ind]
        else:
            return f"No property named {char.upper()}"
    return summed_mores


is_true = True

while is_true:
    sentence = input("Enter your string:\n")
    codify = get_mores_code(sentence)
    print(f"The mores code for {sentence} is {codify}")
    get_out = input("Want to get out of the loop press y, n if No.")
    if get_out == "y":
        is_true = False
    else:
        summed_mores = ""
        continue

