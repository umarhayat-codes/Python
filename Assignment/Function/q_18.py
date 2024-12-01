def convert_temperature(scale,tem):
    if scale.upper() == "F":
        return ((tem * 9/5) + 32)
    elif scale.upper() == "C":
        return ((tem - 32) * 5/9)
    else:
        return "Enter Correct Scale {F,C}"
print(convert_temperature("F",20))