filename = input("Введіть ім'я файлу: ")
try:
    with open (filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())
except:
    print("Такого файлу не існує!")
    print("Повторіть спробу пізніше")
    exit()

author = input("\nХто написав ті рядки? ")
with open(filename, 'a', encoding='utf-8') as f:
    f.write(f"\n({author})")

ans = input("Хочете додати цитату? (Y/n)")
while ans.lower() != 'n':
    quote = input("Введіть цитату: ")
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\n{quote}")
    author_of_quote = input("Введіть автора: ")
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\n({author_of_quote})")
    ans = input("Хочете добавити цитату? ")
with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
    f.close()
