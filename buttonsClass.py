class buttons:
    def __init__(self, w, s, b):
        bord_top_botm = 1 + s + len(w) + s + 1
        print(f"{w} Button Specifications:\nButton name: {w}")
        print("Number of the border characters for the top and the bottom: ", b)
        print('Number of spaces between the left side border and the first character of the button')
        print("name: ", s)
        print("Number of spaces between the right side border and the last character of the button")
        print("name: ", s)
        print("Characters representing the borders: ", b)
        print(b * bord_top_botm)
        print(b + ' '*s + w + ' '*s + b)
        print(b * bord_top_botm)

word = "CANCEL"
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')
