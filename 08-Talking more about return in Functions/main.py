def my_sum(num1, num2, num3):
    return num1 + num2 + num3

def standardize_text(text):
    text = text.casefold()
    text = text.replace("  ", " ")
    text = text.strip()
    return text

def met_goal(sales, target):
    if sales >= target:
        return True
    else:
        return False