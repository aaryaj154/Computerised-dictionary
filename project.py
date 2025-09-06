import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
Antonym = pd.read_csv("Antonym.csv", index_col = 'Word')
Meanings = pd.read_csv("Meanings.csv", index_col = 'Word')
Synonym = pd.read_csv("Synonym.csv", index_col = 'Word')
print("\tMENU")
while True:
    print("""
    1.Antonym
    2.Meanings
    3.Synonym    
    4.Back to Main Menu
    5.Exit
    """)
    a = int(input("Enter any digit from the above list: "))
    print(a)
    if a == 1:
        print("\tAntonym")
        print("""
        1) Add a new Antonym in dictionary
        2) Modify an existing Antonym in dictionary
        3) Remove an existing Antonym in dictionary
        4) Graphical Representation
        5) Fetch Records of Antonym in dictionary
        """)
        Antonym1 = int(input("Choose Your Desired Option: "))
        if Antonym1 == 1:
            print("\tAdding a New Word in Antonym dictionary")
            sid = input("Enter Word: ")
            while sid in Antonym.index:
                print('Word already exists!')
                sid = input("Enter Word: ")
            a1 = input("Enter Antonym1: ")
            a2 = input("Enter Antonym2: ")
            a3 = input("Enter Antonym3: ")
            a4 = input("Enter Antonym4: ")
            a5 = input("Enter Antonym5: ")
            a6 = int(input("Enter Count of Antonyms: "))
            Antonym.loc[sid] = [a1,a2,a3,a4,a5,a6]
            Antonym.to_csv("Antonym.csv")
            
            print("Word Added")
            print(Antonym)
            input("Press any key to continue: ")
        elif Antonym1 == 2:
            print("\tModifying an Existing Word in Antonym")
            print()
            print("Things you can Modify")
            print("1. Antonym1")
            print("2. Antonym2")
            print("3. Antonym3")
            print("4. Antonym4")
            print("5. Antonym5")
            Antonym2 = int(input("Select the desired option from the above menu: "))
            sid2 = (input("Enter Word: "))
            if sid2 not in Antonym.index:
                print("No Such Word Exist")
                print("Check Your Word")
                input("Press Enter to continue: ")
                sid2 = (input("Enter Word: "))
            if Antonym2 == 1:
                a1 = input("Enter New Antonym1: ")
                Antonym.loc[sid2, "Antonym1"] = a1
                print()
                Antonym.to_csv("Antonym.csv")
                print(Antonym)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Antonym2 == 2:
                a2 = input("Enter New Antonym2: ")
                Antonym.loc[sid2, "Antonym2"] = a2
                print()
                Antonym.to_csv("Antonym.csv")
                print(Antonym)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Antonym2 == 3:
                a3 = input("Enter New Antonym3: ")
                Antonym.loc[sid2, "Antonym3"] = a3
                print()
                Antonym.to_csv("Antonym.csv")
                print(Antonym)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Antonym2 == 4:
                a4 = input("Enter New Antonym4: ")
                Antonym.loc[sid2, "Antonym4"] = a4
                print()
                Antonym.to_csv("Antonym.csv")
                print(Antonym)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Antonym2 == 5:
                a5 = input("Enter New Antonym5: ")
                Antonym.loc[sid2, "Antonym5"] = a5
                print()
                Antonym.to_csv("Antonym.csv")
                print(Antonym)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
        elif Antonym1 == 3:
            ("\t Removing an existing word in Antonym dictionary ")
            sid3 = (input("Enter Word: "))
            
            if sid3 not in Antonym.index:
                print("No Such Word Exist")
                print("Check Your Word")
                input("Press Enter to continue: ")
            else:
                print(Antonym.loc[sid3])
                Antonymdel1 = input("Do you want to delete this account? " 'Y/N')
                if Antonymdel1 == 'y' or Antonymdel1=='Y':
                    Antonym.drop(sid3, axis=0, inplace = True)
                    Antonym.to_csv("Antonym.csv")
                    print("Word Removed Successfully")
                    input("Press Enter to continue: ")
                else:
                    print("Word Not Removed")
                    input("Press Enter to continue: ")
        elif Antonym1 == 4:
            ("\t Graphical Representation of Data")
            print()
            print("Graphical Representation Menu")
            print("""
            1) Count
            """)
            Antonym15 = int(input("Select the desired option from the above menu: "))
            if Antonym15 == 1:
                print()
                print("\tChoose Graph Type")
                print("""
            1. Line Chart
            2. Vertical Bar Chart
            3. Horizontal Bar Chart
            4. Histogram
            """)
                charttype = int(input("Select the desired chart type from the above menu: "))
                if charttype == 1:
                    n = int(input("How many Words from the top you want to plot: "))
                    head1 = Antonym.head(n)
                    count = Antonym.Count.head(n)
                    cindex = head1.index
                    plt.plot(cindex, count, label = "Count of Antonym", linewidth = 4,color = 'k')
                    plt.title("Line Chart Representing the Count of Antonym") 
                    plt.xlabel("Word") 
                    plt.ylabel("Count")  
                    plt.legend()  
                    plt.show()
                elif charttype == 2:
                    n = int(input("How many Word from the top you want to plot: "))
                    head1 = Antonym.head(n)
                    count = Antonym.Count.head(n)
                    cindex = head1.index
                    plt.bar(cindex,count, label = "Count of Antonym")
                    plt.title("Bar Chart Representing the Count of Antonym") 
                    plt.xlabel("Word") 
                    plt.ylabel("Count")  
                    plt.legend()  
                    plt.show()
                elif charttype == 3:
                    n = int(input("How many Word from the top you want to plot: "))
                    head1 = Antonym.head(n)
                    count = Antonym.Count.head(n)
                    cindex = head1.index
                    plt.barh(cindex, count, label = "Count of Antonym", color = 'violet')
                    plt.title("Horizontal Bar Chart Representing the Count of Antonym") 
                    plt.xlabel("Word") 
                    plt.ylabel("Count")  
                    plt.legend()  
                    plt.show()
                elif charttype == 4:
                    n = int(input("How many Word from the top you want to plot: "))
                    head1 = Antonym.head(n)
                    count = Antonym.Count.head(n)
                    cindex = head1.index
                    plt.hist(count, bins = 4,label = "Count of Antonym", color = 'cyan', edgecolor = 'k')
                    plt.title("Histogram Representing the Count of Antonym") 
                    plt.xlabel("Word") 
                    plt.ylabel("Count")  
                    plt.legend()  
                    plt.show()
        elif Antonym1 == 5:
            ("\tFetching Records")
            print("""
            1. All Records
            2. Top Records
            3. Bottom Records
            """)
            fetch1 = int(input("Enter the desired option from the above Menu: "))
            if fetch1 == 1:
                print(Antonym)
            elif fetch1 == 2:
                n = int(input("How Many Records from the Top you want to fetch: "))
                head = Antonym.head(n)
                print(head)
            elif fetch1 == 3:
                n = int(input("How Many Records from the Bottom you want to fetch: "))
                tail = Antonym.tail(n)
                print(tail)
                
    elif a == 2:
        print("\tMeanings")
        print("""
        1) Add a new Meanings in table
        2) Modify an existing Meanings of word in table
        3) Remove an existing Meanings from table
        4) Graphical Representation
        5) Fetch Records of Meanings in table
        """)
        Meanings3 = int(input("Choose Your Desired Option: "))
        if Meanings3 == 1:
            print("\tAdding a New Meanings in table")
            cid = input("Enter Word: ")
            while cid in Meanings.index:
                print('Word already exists!')
                cid = input("Enter Word: ")
            b1 = input("Enter Meanings1: ")
            b2 = input("Enter Meanings2: ")
            b3 = input("Enter Meanings3: ")
            b4 = input("Enter Meanings4: ")
            b5 = input("Enter Meanings5: ")
            b6 = input("Enter the Count of Meanings: ")
            print('test')
            print(cid) 
            Meanings.loc[cid] = [b1,b2,b3,b4,b5,b6]
            Meanings.to_csv("Meanings.csv")
            
            print("New Word Added in table")
            print(Meanings)
            input("Press any key to continue: ")
        elif Meanings3 == 2:
            print("\t Modifing an Existing Data of Word in table")
            print()
            print("Things you can modify")
            print("""
            1. Meanings1
            2. Meanings2
            3. Meanings3
            4. Meanings4
            5. Meanings5
            """)
            Meanings4 = int(input("Select the desired option from the above menu: "))
            cid2 = input("Enter Word: ")
            if cid2 not in Meanings.index:
                print("No Such Word Exist")
                print("Check Your Word")
                input("Press Enter to continue: ")
                cid2 = (input("Enter Word: "))
            if Meanings4 == 1:
                Meanings_a = input("Enter New Meanings1: ")
                Meanings.loc[cid2, "Meaning1"] = Meanings_a
                print()
                Meanings.to_csv("Meanings.csv")
                print(Meanings)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Meanings4 == 2:
                Meanings_b = int(input("Enter New Meanings2: "))
                Meanings.loc[cid2, "Meaning2"] = Meanings_b
                print()
                Meanings.to_csv("Meanings.csv")
                print(Meanings)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Meanings4 == 3:
                Meanings_c = input("Enter New Meanings3: ")
                Meanings.loc[cid2, "Meaning3"] = Meanings_c
                print()
                Meanings.to_csv("Meanings.csv")
                print(Meanings)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Meanings4 == 4:
                Meanings_d = int(input("Enter New Meanings4: "))
                Meanings.loc[cid2, "Meaning4"] = Meanings_d
                print()
                Meanings.to_csv("Meanings.csv")
                print(Meanings)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Meanings4 == 5:
                Meanings_e = input("Enter New Meanings5: ")
                Meanings.loc[cid2, "Meaning5"] = Meanings_e
                print()
                Meanings.to_csv("Meanings.csv")
                print(Meanings)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
        elif Meanings3 == 3:
            ("\t Removing an existing Word from table ")
            cid3 = (input("Enter Word: "))
            
            if cid3 not in Meanings.index:
                print("No Such Word Exist")
                print("Check Your Word")
                input("Press Enter to continue: ")
            else:
                print(Meanings.loc[cid3])
                Meaningsl1 = input("Do you want to delete this account? " 'Y/N')
                if Meaningsl1 == 'y' or Meaningsl1=='Y':
                    Meanings.drop(cid3, axis=0, inplace = True)
                    Meanings.to_csv("Meanings.csv")
                    print("Word Removed Successfully")
                    input("Press Enter to continue: ")
                else:
                    print("Word Not Removed")
                    input("Press Enter to continue: ")
        elif Meanings3 == 4:
            ("\t Graphical Representation of Data")
            print()
            print("Graphical Representation Menu")
            print("""
            1) Count
            """)
            Meanings5 = int(input("Select the desired option from the above menu: "))
            if Meanings5 == 1:
                print()
                print("\tChoose Graph Type")
                print("""
            1. Line Chart
            2. Vertical Bar Chart
            3. Horizontal Bar Chart
            4. Histogram
            """)
                charttype = int(input("Select the desired chart type from the above menu: "))
                if charttype == 1:
                    n = int(input("How many Words from the top you want to plot: "))
                    head1 = Meanings.head(n)
                    count = Meanings.Count.head(n)
                    cindex = head1.index
                    plt.plot(cindex, count, label = "Count of Meanings ", linewidth = 4,color = 'k')
                    plt.title("Line Chart Representing the Count of Meanings") 
                    plt.xlabel("Word") 
                    plt.ylabel("Count")  
                    plt.legend()  
                    plt.show()
                elif charttype == 2:
                    n = int(input("How many Word from the top you want to plot: "))
                    head1 = Meanings.head(n)
                    count = Meanings.Count.head(n)
                    cindex = head1.index
                    plt.bar(cindex, count, label = "Count of Meanings ")
                    plt.title("Bar Chart Representing the Count of Meanings") 
                    plt.xlabel("Word") 
                    plt.ylabel("Count")  
                    plt.legend()  
                    plt.show()
                elif charttype == 3:
                    n = int(input("How many Word from the top you want to plot: "))
                    head1 = Meanings.head(n)
                    count = Meanings.Count.head(n)
                    cindex = head1.index
                    plt.barh(cindex, count, label = "Count of Meanings", color = 'violet')
                    plt.title("Horizontal Bar Chart Representing the Count of Meanings") 
                    plt.xlabel("Word") 
                    plt.ylabel("Count")  
                    plt.legend()  
                    plt.show()
                elif charttype == 4:
                    n = int(input("How many Age from the top you want to plot: "))
                    head1 = Meanings.head(n)
                    count = Meanings.Count.head(n)
                    cindex = head1.index
                    plt.hist(count, bins = 4,label = "Count of Meanings", color = 'cyan', edgecolor = 'k')
                    plt.title("Histogram Representing the Count of Meanings") 
                    plt.xlabel("Word") 
                    plt.ylabel("Age")  
                    plt.legend()  
                    plt.show()
        elif Meanings3 == 5:
                ("\tFetching Records")
                print("""
                1. All Records
                2. Top Records
                3. Bottom Records
                """)
                fetch2 = int(input("Enter the desired option from the above Menu: "))
                if fetch2 == 1:
                    print(Meanings)
                elif fetch2 == 2:
                    n = int(input("How Many Records from the Top you want to fetch: "))
                    head = Meanings.head(n)
                    print(head)
                elif fetch2 == 3:
                    n = int(input("How Many Records from the Bottom you want to fetch: "))
                    tail = Meanings.tail(n)
                    print(tail)
                                                
    elif a == 3:
        print("\tSynonym")
        print("""
        1) Add a new Synonym in table
        2) Modify an existing Synonym in table
        3) Remove an existing Synonym from table
        4) Graphical Representation
        5) Fetch Records of Synonym in table
        """)
        Synonym6 = int(input("Choose Your Desired Option: "))
        if Synonym6 == 1:
            print("\tAdding a New Word in table")
            pid = input("Enter Word: ")
            while pid in Synonym.index:
                print('Word already exists!')
                pid = input("Enter Word: ")
            Synonym1 = input("Enter Synonym1: ")
            Synonym2 = input("Enter Synonym2: ")
            Synonym3 = input("Enter Synonym3: ")
            Synonym4 = input("Enter Synonym4: ")
            Synonym5 = input("Enter Synonym5: ")
            Synonym6 = int(input("Enter the Count of Synonyms: "))

            Synonym.loc[pid] = [Synonym1,Synonym2,Synonym3,Synonym4,Synonym5,Synonym6]
            Synonym.to_csv("Synonym.csv")
            
            print("New Word Added in table")
            print(Synonym)
            input("Press any key to continue: ")
        elif Synonym6 == 2:
            print("\t Modifing an Existing Synonym in table")
            print()
            print("Things you can modify")
            print("""
            1. Synonym1
            2. Synonym2
            3. Synonym3
            4. Synonym4
            5. Synonym5
            """)
            Synonym7 = int(input("Select the desired option from the above menu: "))
            pid2 = input("Enter Word: ")
            if pid2 not in Synonym.index:
                print("No Such Word Exist")
                print("Check Your Word")
                input("Press Enter to continue: ")
                pid2 = (input("Enter Word : "))
            if Synonym7 == 1:
                Synonym_a = input("Enter New Synonym1: ")
                Synonym.loc[pid2, "Synonym1"] = Synonym_a
                print()
                Synonym.to_csv("Synonym.csv")
                print(Synonym)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Synonym7 == 2:
                Synonym_b = input("Enter New Synonym2: ")
                Synonym.loc[pid2, "Synonym2"] = Synonym_b
                print()
                Synonym.to_csv("Synonym.csv")
                print(Synonym)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Synonym7 == 3:
                Synonym_c = int(input("Enter New Synonym3: "))
                Synonym.loc[pid2, "Synonym3"] = Synonym_c
                print()
                Synonym.to_csv("Synonym.csv")
                print(Synonym)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Synonym7 == 4:
                Synonym_d = input("Enter New Synonym4: ")
                Synonym.loc[pid2, "Synonym4"] = Synonym_d
                print()
                Synonym.to_csv("Synonym.csv")
                print(Synonym)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
            elif Synonym7 == 5:
                Synonym_e = input("Enter New Synonym5: ")
                Synonym.loc[pid2, "Synonym5"] = Synonym_e
                print()
                Synonym.to_csv("Synonym.csv")
                print(Synonym)
                print("Data Changed Successfully")
                input("Press Enter to continue: ")
        elif Synonym6 == 3:
            ("\t Removing an existing Word from table ")
            pid3 = (input("Enter Word: "))
            
            if pid3 not in Synonym.index:
                print("No Such Word Exist")
                print("Check Your Word")
                input("Press Enter to continue: ")
            else:
                print(Synonym.loc[pid3])
                Synonyml1 = input("Do you want to delete this player? " 'Y/N')
                if Synonyml1 == 'y' or Synonym=='Y':
                    Synonym.drop(pid3, axis=0, inplace = True)
                    Synonym.to_csv("Synonym.csv")
                    print("Word Removed Successfully")
                    input("Press Enter to continue: ")
                else:
                    print("Word Not Removed")
                    input("Press Enter to continue: ")
        elif Synonym6 == 4:
            ("\t Graphical Representation of Data")
            print()
            print("Graphical Representation Menu")
            print("""
            1) Count
            """)
            Synonym9 = int(input("Select the desired option from the above menu: "))
            if Synonym9 == 1:
                print()
                print("\tChoose Graph Type")
                print("""
            1. Line Chart
            2. Vertical Bar Chart
            3. Horizontal Bar Chart
            4. Histogram
            """)
                charttype = int(input("Select the desired chart type from the above menu: "))
                if charttype == 1:
                    n = int(input("How many Word from the top you want to plot: "))
                    head1 = Synonym.head(n)
                    count = Synonym.Count.head(n)
                    pindex = head1.index
                    plt.plot(pindex, count, label = "Count of Meanings", linewidth = 4,color = 'dodgerblue')
                    plt.title("Line Chart Representing the Count of Synonyms") 
                    plt.xlabel("Word") 
                    plt.ylabel("Count")  
                    plt.legend()  
                    plt.show()
                elif charttype == 2:
                    n = int(input("How many Word from the top you want to plot: "))
                    head1 = Synonym.head(n)
                    count = Synonym.Count.head(n)
                    pindex = head1.index
                    plt.bar(pindex, count, label = "Count of Synonyms", color = 'yellowgreen')
                    plt.title("Bar Chart Representing the Count of Synonyms") 
                    plt.xlabel("Word") 
                    plt.ylabel("Count")  
                    plt.legend()  
                    plt.show()
                elif charttype == 3:
                    n = int(input("How many Word from the top you want to plot: "))
                    head1 = Synonym.head(n)
                    count = Synonym.Count.head(n)
                    pindex = head1.index
                    plt.barh(pindex, count, label = "Count Of Synonyms", color = 'midnightblue')
                    plt.title("Horizontal Bar Chart Representing the Count of Synonyms") 
                    plt.xlabel("Word") 
                    plt.ylabel("Count")  
                    plt.legend()  
                    plt.show()
                elif charttype == 4:
                    n = int(input("How many Word from the top you want to plot: "))
                    head1 = Synonym.head(n)
                    count = Synonym.Count.head(n)
                    pindex = head1.index
                    plt.hist(count, bins = 4,label = "Count of Synonyms", color = 'olive', edgecolor = 'k')
                    plt.title("Histogram Representing the Count Of Synonyms") 
                    plt.xlabel("Word") 
                    plt.ylabel("Count")  
                    plt.legend()  
                    plt.show()
        elif Synonym6 == 5:
                ("\tFetching Records")
                print("""
                1. All Records
                2. Top Records
                3. Bottom Records
                 """)
                fetch3 = int(input("Enter the desired option from the above Menu: "))
                if fetch3 == 1:
                    print(Synonym)
                elif fetch3 == 2:
                    n = int(input("How Many Records from the Top you want to fetch: "))
                    head = Synonym.head(n)
                    print(head)
                elif fetch3 == 3:
                    n = int(input("How Many Records from the Bottom you want to fetch: "))
                    tail = Synonym.tail(n)
                    print(tail)
    else:
        print("\tThank You!")
        break
