mode = input("What class would you like to take notes for ('ethics' / 'datastruct' / 'principle'): ")
chapter = input("Enter chapter name: ")
filename = 'notes_output.txt'

while True:
    match mode:
        case "ethics":
            information = 'Act as though you were a PhD holding Engineer professor teaching a Sustainable Development and Environmental Stewardship course. Teach me the following information of the SECTION section of the CHAPTER chapter of my textbook: '
        case "datastruct":
            information = 'Act as though you were a PhD holding Computer Science professor teaching a Java Data Structures and Algorithms course. Teach me the following information of the SECTION section of the CHAPTER chapter of my textbook. If your explanations can be supplemented by code, provide me amazing code examples:'
        case "principle":
            information = 'Act as though you were a PhD holding Computer Science professor teaching a Principles of Programming Languages course. Teach me the following information of the SECTION section of the CHAPTER chapter of my textbook. If your explanations can be supplemented by code, provide me amazing code examples:'
        case _:
            exit()
    section = input("Enter section name (or enter 'q' to quit): ")
    if section == "q":
        break
    content = input("Enter content : ")
    information = information.replace("SECTION", section)
    information = information.replace("CHAPTER", chapter)
    
    with open(filename, "a") as file:
        file.write(information + '"' + content + '"\n\n')