import csv
import random

print("\n Welcome to music collector!")
while True:
    music = []
    albums_list = []


    with open('music.csv', 'r') as f:
        read_csv = csv.reader(f, delimiter="|")

        def no_space(n):
            n = n.strip(" ").upper()
            return n

        for row in read_csv:
            row = list(map(no_space, row))
            artist = row[0]
            album = row[1]
            year = row[2]
            genre = row[3]
            time = row[4]

            name_tuple = (artist, album)
            info_tuple = (year, genre, time)
            global_tuple = (name_tuple, info_tuple)
            alb_genre = [genre, album]


            music.append(global_tuple)

    #print(music)

    artists = global_tuple[0][0]
    albums = global_tuple[0][1]
    years = global_tuple[1][0]
    genres = global_tuple[1][1]
    timess = global_tuple[1][2]



    print(        "\n1) Add new album\n"
                  "2) Find albums by artist\n"
                  "3) Find albums by year\n"
                  "4) Find musician by album\n"
                  "5) Find album by letter(s)\n"
                  "6) Find albums by genre\n"
                  "7) Calculate the age of all albums\n"
                  "8) Choose a random album by genre\n"
                  "0) Exit")
    answer = input()

    if answer == "2":
        a = input("Name of artist: ")
        for global_tuple in music:
            if a.upper() == global_tuple[0][0]:
                artist = global_tuple[0][0]
                album = global_tuple[0][1]
                year = global_tuple[1][0]
                genre = global_tuple[1][1]
                times = global_tuple[1][2]
                print("\n", artist, "-", album, ",", "was released in", year,"." "\n Genre:", genre, ", Length:",
                      times)




    if answer == "1":
        ans1 = input("What album? ")
        ans2 = input("Who is the artist? ")
        while True:
            try:
                ans3 = int(input("The year of album: "))
                break
            except ValueError:
                print("Please provide only numbers")
        while ans3 not in range(1900,2017):
            ans3 = int(input("Please provide correctly. The year of album: "))
        ans4 = input("Genre? ")
        ans5 = input("Time? ")

        print("\nNew album is added\n")

        with open('music.csv', 'a') as k:
            k.writer = csv.writer(k, delimiter="|")
            k.writer.writerow([ans2, ans1, ans3, ans4.lower(), ans5])
            k.close()

    if answer == "8":
        answer = input('Choose genre: ')

        for album in music:
            for info in album[1]:
                if info == answer.upper():
                    albums_list.append(album)

        try:
            x = random.randint(0, len(albums_list) - 1)
            print("\n", albums_list[x][0][0],"-", albums_list[x][0][1],",", "was released in", albums_list[x][1][0],
                  "\n Genre:",albums_list[x][1][1],", Length:", albums_list[x][1][2])

            albums_list.clear()
        except ValueError:
            print("There is no such genre in list")




    if answer == "3":
        a = input("Year: ")
        for global_tuple in music:
            if a == global_tuple[1][0]:
                artist = global_tuple[0][0]
                album = global_tuple[0][1]
                year = global_tuple[1][0]
                genre = global_tuple[1][1]
                times = global_tuple[1][2]
                print("\n", artist, "-", album, ",", "was released in", year, "." "\n Genre:", genre, ", Length:",
                      times)


    if answer == "4":
        a = input("Album: ")
        for global_tuple in music:
            if a.upper() == global_tuple[0][1]:
                artist = global_tuple[0][0]
                album = global_tuple[0][1]
                year = global_tuple[1][0]
                genre = global_tuple[1][1]
                times = global_tuple[1][2]
                print("\n", artist, "-", album, ",", "was released in", year, "." "\n Genre:", genre, ", Length:",
                      times)

    if answer == "5":
        a = input("Type letter or letters: ")
        b = len(a)
        for global_tuple in music:
            if global_tuple[0][1].startswith(a.upper()) or a in global_tuple[0][1] and b > 1:
                print("\n",global_tuple[0][1],"\n")
                artist = global_tuple[0][0]
                album = global_tuple[0][1]
                year = global_tuple[1][0]
                genre = global_tuple[1][1]
                times = global_tuple[1][2]
                print("\n", artist, "-", album, ",", "was released in", year,"." "\n Genre:", genre, ", Length:", times)


    if answer == "6":
        a = input("The name of genre: ")
        for global_tuple in music:
            if a.upper() == global_tuple[1][1]:
                artist = global_tuple[0][0]
                album = global_tuple[0][1]
                year = global_tuple[1][0]
                genre = global_tuple[1][1]
                times = global_tuple[1][2]
                print("\n", artist, "-", album,"," ,"was released in" ,year,"." "\n Genre:",genre,", Length:",times)




    if answer == "7":
        years = 0
        for album in music:
            years += int(album[1][0])

        print(years ,"years","- summary time of all years")


    if answer == "0":
        break
