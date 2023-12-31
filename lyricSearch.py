import csv  #import library
targetLyric = input("What word/phrase are you trying to find the song for?\n\033[1m")   #get phrase being searched for
found = False
songCount = 0
lyricCount = 0   #set tracking varibles to defualt
with open('output.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:  #go through each row in the output.csv file
        lyric = row[2]  #'lyric' is the lyrics column of the current row
        lyricCount += lyric.lower().count(targetLyric.lower())   #add to the count however many times targetLyric is in this song
        if lyric.lower().find(targetLyric.lower()) != -1:
            songCount += 1    #if the targetLyric is in this song, add to the count of how many songs this targetLyric was found in

        while True:
            index = lyric.lower().find(targetLyric.lower()) #start from the first time the targetLyric is found
            if index == -1:
                break   #if it's not found, exit

            print("\033[0m")
            print(f"{row[0]}: {row[1]}")    #print the song title and album

            prevLyric = lyric.rfind(';', 0, index)
            prevLyric = prevLyric if prevLyric != -1 else -2
            if prevLyric > -1:
                prevLyric = lyric.rfind(';', 0, prevLyric)
                prevLyric = prevLyric if prevLyric != -1 else -2   #the previous lyric is the semicolon found before the line with the targetLyric

            nextLyric = lyric.find(';', index)
            nextLyric = nextLyric if nextLyric != -1 else len(lyric)
            nextLyric = lyric.find(';', nextLyric + 1)
            nextLyric = nextLyric if nextLyric != -1 else len(lyric)   #the next lyric is the semicolon found after the line with the targetLyric

            lyricSub = '\t\b\b``' + lyric[prevLyric + 2:nextLyric].replace('; ', '\n\t') + '´´'   #format from previous to next lyric
            newIndex = lyricSub.lower().find(targetLyric.lower())
            newTarget = lyricSub[newIndex:newIndex + len(targetLyric)]  #target corrects for capitalization

            m = 47
            albumColors = { #dictionary of albums to rgb codes
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
                    m = albumColors[x]  #depending on what album it is, change the color of the target

            lyricSub = lyricSub.replace(newTarget, f"\033[1m\033[{m}m{newTarget}\033[0m")   #colorize and bold the target lyric in new formatted lyrics
            print(lyricSub) #print it
            found = True    #the target exists in any song
            lyric = lyric[nextLyric+2:]  #start checking again from after the next lyric

    if found is False:
        print("not found")  #print if it wasn't found
    else:
        print(f"Showing {lyricCount} result{"s" if lyricCount != 1 else ""} from {songCount} song{"s" if songCount != 1 else ""}")    #if it was, print how many times and in how many songs
