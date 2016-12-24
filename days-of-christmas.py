import pyttsx

speech_engine = pyttsx.init()


def sayLine(line):
    print(line)

    speech_engine.say(line)
    speech_engine.runAndWait()


def main():
    days = ["first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "tenth",
            "eleventh",
            "twelfth"]

    gifts = ["{} drummers drumming",
             "{} pipers piping",
             "{} lords a leaping",
             "{} ladies dancing",
             "{} maids a milking",
             "{} swans a swimming",
             "{} geese a laying",
             "{} golden rings",
             "{} calling birds",
             "{} french hens",
             "{} turtle doves",
             "a partridge in a pear tree"]

    gifts.reverse()

    for d in range(1, 12 + 1):
        sayLine("On the {} day of Christmas".format(days[d - 1]))
        sayLine("my true love sent to me:")

        for g in range(d - 1, -1, -1):
            gift = gifts[g]

            if d != 1 and g == 0:
                gift = "and " + gift

            sayLine(gift.format(g + 1))

        print("")


if __name__ == '__main__':
    main()
