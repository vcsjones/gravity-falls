#!/usr/bin/env python
import curses
import time

entries = [
    # Journal
    "09/03/2012\n\nI am a researcher that traveled to Gravity Falls to investigate paranormal activity that Top Secret departments in the US government became aware of twenty years ago. " +
        "Originally, plans were made to perform the research remotely for the safety of the researchers. However, the research stalled, millions of dollars were wasted, and the goverment was losing patience. " +
        "As a result, safety of researchers is no longer a top concern, so researchers such as myself are being sent out for investigati╣n.\n\n" +
        "My job is to continue the investigation that the ones before me were unable to complete, and find out what happened to the others. The Agency has not been forthcoming " +
        "about what happe╛ed to the others - however I have heard rumors that two were sent before me. The first one stopped communicating. The second one als╣ stopped responding to messages, however rumors are the second one " +
        "went 'insane'. It is not clear to me what specifically this mea╛s, or if the government is attempting to cover up what happened to the previous researchers.\n\n" +
        "I must be careful with what I say or The Agency may believe that I know too much about Gravity Falls.",

    # Experiments
    "09/17/2012\n\nI am slowly starting to peice back together the research my previous co-workers had started. The research initially proved to be boring. Simply collecting ┴amples of dirt, examining " +
        "animals, and tasting plants. However as the reserach progressed, the results turned... concerning. Eventually, the researchers discovered an area within Gravity Falls around the 'Pines' ┼amily. " +
        "Paranormal activtity greatly increased in the area, with animals exhibiting odd behaviors, unusual intelligence, and abnormal ┴izes. Samples were taken to be sent back to the lab. However, I am " +
        "not sure if those samples were ever sent, as The Agency has no record of receiving those samples. Though, it is entirely possible they destroyed the records to cover up their existience.\n\n" +
        "I will need to continue to research and understand the population o┼ Gravity Falls. It is likely that at least one, or several, of its residents are aware of the the anomilies in the town.\n\n" +
        "It is even possible some understand the paranormal activity better than we do - for better, or for worse.",

    # Cipher File
    "10/04/2012\n\nThrough the previous research, and research of my own, I've determined, what I believe, to be an important bit of information regarding the paranormal activ└ty. Much of it relates to someone " +
        "named 'Bill Cipher'. I do not know who Bill is, and the town has no record of this person living in Gravity Falls. It is also not clear to me if Bill is simply related to the activity, or the cause of it. " +
        "I've asked The Agency if they ha╤e any record of Bill. I have yet to receive an answer as to who, exactly, Bill is. The Agency however seemed more concerned with understanding how I learned of Bill's existence.\n\n"
        "This gives me some hope that I am going in the r└ght direction - The Agency seems to be aware of Bill, howe╤er is not cooperating with me to find Bill. In fact, they seem to suggest that it would be in my " +
        "own best interest to not look too much deeper in to Bill.",

    # Gideon's Plans
    "10/31/2012\n\nI have, I suspect like the researchers before me, l╔arned too much about Gravity Falls to remain ╩omfortable living here for much longer. What I do understan╙ is that the paranormal activity here is " +
    "if anything, just the beginning. I also understand that Gravity Falls has powerful people living here. Gideon Gleeful is such a person. Gideon Gleeful appears to have the body of a child, however is malevolent. " +
    "I am unsure if Gideon is truly a child, or paranormal activity has given a person, or otherwise.\n\n" +
    "Gideon appears to have deep connections to Bill and the Pines, though the specifics of the relationship I am unsure of. He presents himself as being in control of Bill however I do not believe that to be true. In " +
    "fact I believe it to be the opposite - Bill is using Gideon as a puppet without Gideon's knowledge.\n\n" +
    "I am increasingly convinced that Bill is not human, though through possession may appear as human. If this is tru╔, the the paranormal a╩tivity goes much further than I originally anticipated. The Agency would in " +
    "all likelihood steal and cover up such a power and relentlessly work to understand it. This knowledge itself is risky, and I fear having passed it on to whoever rea╙s this may ultimately put them at risk, too.\n\n" +
    "Time is running short.",

    "??/??/????\n\n╣ ╛ ╔\n\n┴ ╔ ╤ ╔ ╛\n\n┼ └ ╤ ╔\n\n" # See notes.
]

def flood_text(port, text):
    # Curses doesn't seem to wrap text intelligently. It just wraps text in the middle of words which looks dumb.
    # This wraps the text at space boundaries like a civilized person.
    port.clear()

    indent = 2
    max_line = curses.COLS - indent
    last_space = -1
    position = 0
    line = 0

    while len(text) > 0:
        while position < max_line:
            if position == len(text) - 1:
                last_space = position + 1 # Add one because we want to preserve the last character.
                break
            c = text[position]
            if c == "\n":
                last_space = position
                break
            elif c.isspace():
                last_space = position
            position = position + 1

        port.addstr(line, indent, text[:last_space])
        line = line + 1
        text = text[last_space + 1:]
        last_space = -1
        position = 0

    port.get_wch()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
    stdscr.clear()

    if curses.COLS < 92 or curses.LINES < 30:
        stdscr.addstr(0, 0, "Terminal must be 92x30 or larger.")
        stdscr.addstr(1, 0, "Resize the terminal and run again.")
        stdscr.getch()
        return

    header = curses.newwin(8, curses.COLS - 20, 0, 0)
    header.bkgd(' ', curses.color_pair(2))
    header.addstr(2, 0, "  ____                 _ _           _____     _ _     \n / ___|_ __ __ ___   _(_) |_ _   _  |  ___|_ _| | |___ \n| |  _| '__/ _` \ \ / / | __| | | | | |_ / _` | | / __|\n| |_| | | | (_| |\ V /| | |_| |_| | |  _| (_| | | \__ \ \n \____|_|  \__,_| \_/ |_|\__|\__, | |_|  \__,_|_|_|___/\n                             |___/")
    bill = curses.newwin(8, 20, 0, curses.COLS - 20)
    bill.bkgd(' ', curses.color_pair(2))
    bill.addstr(1, 0, "       || \n     __||__ \n       /\      | \n      /  \     | \n-----/  0 \----- \n|   /      \ \n   /________\ ")

    work = curses.newwin(curses.LINES - 8, curses.COLS, 8, 0)
    work.bkgd(' ', curses.color_pair(1))

    stdscr.refresh()
    header.refresh()
    bill.refresh()
    curses.mousemask(0)

    while True: # Password reader loop
        work.clear()
        prompt_text = "Enter System Password: "
        work.addstr(0, 0, prompt_text)
        work.refresh()

        offset = 0
        password = ""

        while True: # Character loop
            ch = work.get_wch()

            if (not isinstance(ch, str)) or len(ch) != 1 or ord(ch) > 127:
                continue

            if ord(ch) == 127: # backspace
                if offset > 0:
                    work.addstr(0, len(prompt_text) + offset - 1, " ")
                    work.move(0, len(prompt_text) + offset - 1)
                    offset = offset - 1
                    password = ''.join(password.rsplit(password[-1], 1)) # lol. This is "remove the last character" in python.
            elif ord(ch) == 10: # enter
                break
            elif offset < 16: # No point in allowing more than 16 characters, so swallow it if we are >= 16.
                work.addstr(0, len(prompt_text) + offset, "*")
                password = password + ch
                offset = offset + 1

        if password == "bill": # yeah yeah
            break
        elif password == "quit!":
            exit(0)
        else:
            work.clear()
            work.addstr(0, 0, "Incorrect Password.")
            work.refresh()
            time.sleep(1)

    work.clear()
    work.bkgd(' ', curses.color_pair(4))
    work.addstr(0, 0, "Access Granted!")
    work.refresh()

    time.sleep(1)
    do_clear = True

    while True:
        if do_clear:
            work.clear()

        do_clear = True
        work.addstr(1, 2, "Files")

        work.addstr(3, 5, "1. Journal")
        work.addstr(4, 5, "2. Experiments")
        work.addstr(5, 5, "3. Cipher File")
        work.addstr(6, 5, "4. Gideon's Plans")
        work.addstr(7, 5, "5. ╩ ╣ ╙ ╔ (data is corrupt)")
        work.addstr(8, 5, "6. Log out")
        work.addstr(10, 2, "Enter selection: ")

        menu_selection = work.get_wch()

        if menu_selection == "6":
            main(stdscr) # Eh, I don't really care about stack depth here.
        elif menu_selection == "1":
            flood_text(work, entries[0])
        elif menu_selection == "2":
            flood_text(work, entries[1])
        elif menu_selection == "3":
            flood_text(work, entries[2])
        elif menu_selection == "4":
            flood_text(work, entries[3])
        elif menu_selection == "5":
            flood_text(work, entries[4])
        else:
            do_clear = False
            continue


curses.wrapper(main)