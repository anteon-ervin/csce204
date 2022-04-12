def replace_stars(word):
    answer = ""
    
    for letter in word:
        if letter == "*":
            answer += "."
        else:
            answer += letter
    return answer

word = "a*b*c*d"
print(replace_stars("a*b*c*d"))


def replace_stars():
    answer = ""
    global word
    for letter in word:
        if letter == "*":
            answer += "."
        else:
            answer += letter
    word = answer

word = "a*b*c*d"
replace_stars()
print(word)