# - daca litera de inceput sau litera de sfarsit se mai gaseste in interior cuvant, aceasta se va afisa;
# - 7 vieti;

# cuvant = 'p y t h o n'
#         #'p _ _ _ _ n'

word = 'caracteristica'
display_word = ''
start_letter = word[0] # prima litera
end_letter = word[-1] # ultima litera
tried_characters = [start_letter, end_letter]
word_length = len(word)
for letter in word:
    if letter == start_letter or letter == end_letter:
        display_word += letter
    else:
        display_word += '_'

# print(display_word)
attempts = 7
tries = 0
while attempts >= 1:
    tries += 1
    print(f'Cuvantul este: {display_word}. Mai aveti {attempts} vieti!')
    input_letter = input('Introduceti litera urmatoare: ').lower()
    # if len(input_letter) != 1:
    #     print('Va rugam sa introduceti doar o singura litera!')
    #     continue
    # elif not input_letter.isalpha():
    #     print('Va rugam sa introduceti doar litere!')
    #     continue
    if input_letter.lower() == word.lower():
        print(f'Felicitari! Ai castigat! Cuvantul gasit este {word}. Ai ghicit din {tries} incercari! ')
        break
    if len(input_letter) != 1 or not input_letter.isalpha():
        print('Va rugam sa introduceti doar un singur caracter si acesta sa fie litera!')
        continue
    if input_letter in word.lower():
        if input_letter in tried_characters:
            print(f'Ati mai incercat aceasta litera! Pana acum ati incercat {tried_characters}')
            continue
        else:
            tried_characters.append(input_letter)
        for index, character in enumerate(word.lower()):
            if character == input_letter:
                display_word = display_word[:index] + input_letter + display_word[index+1:]
        if display_word == word.lower():
        # if not '_' in display_word:
            print(f'Felicitari! Ai castigat! Cuvantul gasit este {word}. Ai ghicit din {tries} incercari! ')
            break
    else:
        if input_letter in tried_characters:
            print(f'Ati mai incercat aceasta litera! Pana acum ati incercat {tried_characters}')
        else:
            tried_characters.append(input_letter)
            attempts -= 1
            print(f'Pana acum ati incercat {tried_characters}')
            if attempts < 1:
                print(f'Ai pierdut! Cuvantul din joc era "{word}"')