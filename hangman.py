"""

@file       :hangman.py
@brief      :Write a program for hangman
@author     :vignesh

"""
import time
import random

def first():
    """
    to display hangman

    """


    print       "    *  *      "
    print       "  *      *   "
    print       "  *      *   "
    print       "   *    *     "
    print       "      *     "
    print       "   *  *  *    "
    print       " *     *   *   "
    print       "    *   *     "
    print       "   *     *   "
    print       " *         *"
    print " WILL YOU SAVE ME "
    time.sleep(2)
first()

def hangman(count):
    """
    hangman game
    """

    if count == 1:
        print       "    *  *      "
        print       "  *      *   "
        print       "  *      *   "
        print       "   *    *     "
        print       "      *     "
        print       "   *  *  *    "
        print       " *   *     *   "
        print       "    *        "
        print       "   *       "
        print       " *          "

    elif count == 2:
        print       "    *  *      "
        print       "  *      *   "
        print       "  *      *   "
        print       "   *    *     "
        print       "      *     "
        print       "   *    *    "
        print       " *        *   "
        print       "            "
        print       "          "
        print       "           "

    elif count == 3:
        print       "    *  *      "
        print       "  *      *   "
        print       "  *      *   "
        print       "   *    *     "
        print       "      *     "
        print       "       *    "
        print       "         *   "
        print       "            "
        print       "          "
        print       "           "


    elif count == 4:
        print       "    *  *      "
        print       "  *      *   "
        print       "  *      *   "
        print       "   *    *     "
        print       "      *     "
        print       "           "
        print       "           "
        print       "            "
        print       "          "
        print       "           "

    elif count == 5:
        print    "YOU LOST "
        print       "    *  *      "
        print       "  *      *   "
        print       "  *      *   "
        print       "   *    *     "
        print       "      *     "
        print       "      * * * * "
        print       "            *  "
        print       "            *  "
        print       "              "
        print       "              "
        print " U  KILLED  ME.."
fp = open("word")
while True:
    #word1 = random.choice(["DHONI","BARCA","CR7","MESSI","INDIA","VVDN"])
    word1 = fp.readline()
    #print word1
    print "IT IS A %d LETTER WORD"%(len(word1)-1)
    k = len(word1) -1
    list1 = []
    for i in word1:
        if i != '\n':
            list1.append(i)
    list2 = ['_' for i in  range(len(word1) - 1)]
    print list2
    count = 0
    while count < 5:
        if '_' in list2:
            j = raw_input("Guess the letter:")
            if j in list1:
                ind = list1.index(j)
                list1[ind] = '_'
                list2[ind] = j
            else:
                count += 1
                hangman(count)
            print list2
        else:
            print "THANK YOU FOR SAVING ME!!!"
            break



    opt = raw_input("DO U WANT TO PLAY AGAIN(YES / NO)")
    if opt == 'YES':
        continue
    else:
        break

