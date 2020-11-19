words = ["poutranca", "dantesco", "sabão", "sabão",
         "pizza", "pizza", "queijo", "queijo", "manteiga", "dantesco"]

find = input("Digite a palavra : ")
count = 0


def find_list(words, find, count):

    for i in range(len(words)):

        if(find == words[i]):

            count += 1

    return count


print(find_list(words, find, count))
