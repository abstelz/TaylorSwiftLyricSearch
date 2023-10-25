import csv  # import library for lyrics

targetLyric = input(
    # input searches lyrics (bold)
    "What word/phrase are you trying to find the song for?\n\033[1m")
found = False
# prev = 0
results = 0
with open('output.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:  # import lyrics
        index = row[2].lower().find(targetLyric.lower())
        # while index != -1:
        if index != -1:  # if lyrics exists
            results += 1
            print("\033[0m")
            print(str(row[0:2]).replace(
                "[", '').replace("]", '').replace('\'', ''))
            # print song and album name
            prev = row[2].rfind(';', 0, index)
            prev = prev if prev != -1 else -2
            if prev > -1:
                prev = row[2].rfind(';', 0, prev)
                prev = prev if prev != -1 else -2  # get index of begginning of previous lyric
            next = row[2].find(';', index)
            next = next if next != -1 else len(row[2])
            next = row[2].find(';', next+1)
            # get index of end of next lyric
            next = next if next != -1 else len(row[2])
            lyricSub = '\t\b\b``' + row[2][prev +
                                           # format everything between those indexes
                                           2:next].replace('; ', '\n\t') + '´´'
            # get index of target word in that new formated string
            newIndex = lyricSub.lower().find(targetLyric.lower())
            newTarget = lyricSub[newIndex:newIndex+len(targetLyric)]

            m = 47
            albumColors = {"Taylor Swift": "38;2;144;238;144", "Fearless": "38;2;255;215;0", "Speak Now": "38;2;128;0;128", "Red": "38;2;255;0;0", "1989": "38;2;173;216;230",
                           "reputation": "48;2;0;0;0m\033[38;2;255;255;255", "Lover": "38;2;255;182;193", "folklore": "48;2;169;169;169", "evermore": "38;2;139;69;19", "Midnights": "38;2;0;0;139", "Holiday": "47"}
            for x in albumColors:
                if row[1].find(x) != -1:
                    m = albumColors[x]
            lyricSub = lyricSub.replace(
                # replace the searched word with the color-fied new word
                newTarget, f"\033[1m\033[{m}m{newTarget}\033[0m")
            print(lyricSub)
            found = True
            # endOfSong = row[2][next+2:]
            # index = endOfSong.lower().find(targetLyric.lower())
            # print(index)
    if found is False:
        print("not found")
    else:
        print(f"Showing result(s) from {results} song(s)")
