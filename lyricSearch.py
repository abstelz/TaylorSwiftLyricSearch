import csv
targetLyric = input("What word/phrase are you trying to find the song for?\n\033[1m")
found = False
results = 0
count = 0
with open('output.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:
        lyric = row[2]
        count += lyric.lower().count(targetLyric.lower())
        if lyric.lower().find(targetLyric.lower()) != -1:
            results += 1

        while True:
            index = lyric.lower().find(targetLyric.lower())
            if index == -1:
                break

            print("\033[0m")
            print(f"{row[0]}: {row[1]}")

            prev = lyric.rfind(';', 0, index)
            prev = prev if prev != -1 else -2
            if prev > -1:
                prev = lyric.rfind(';', 0, prev)
                prev = prev if prev != -1 else -2

            next = lyric.find(';', index)
            next = next if next != -1 else len(lyric)
            next = lyric.find(';', next + 1)
            next = next if next != -1 else len(lyric)

            lyricSub = '\t\b\b``' + lyric[prev + 2:next].replace('; ', '\n\t') + '´´'
            newIndex = lyricSub.lower().find(targetLyric.lower())
            newTarget = lyricSub[newIndex:newIndex + len(targetLyric)]

            m = 47
            albumColors = {
                "Taylor Swift": "38;2;144;238;144",
                "Fearless": "38;2;255;215;0",
                "Speak Now": "38;2;128;0;128",
                "Red": "38;2;255;0;0",
                "1989": "38;2;173;216;230",
                "reputation": "48;2;0;0;0m\033[38;2;255;255;255",
                "Lover": "38;2;255;182;193",
                "folklore": "48;2;169;169;169",
                "evermore": "38;2;139;69;19",
                "Midnights": "38;2;0;0;139",
                "Holiday": "47",
            }
            for x in albumColors:
                if row[1].find(x) != -1:
                    m = albumColors[x]

            lyricSub = lyricSub.replace(newTarget, f"\033[1m\033[{m}m{newTarget}\033[0m")
            print(lyricSub)
            found = True
            lyric = lyric[next+2:] #hi

    if found is False:
        print("not found")
    else:
        print(f"Showing {count} result{"s" if count != 1 else ""} from {results} song{"s" if results != 1 else ""}")
