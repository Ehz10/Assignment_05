#------------------------------------------#
# Title: CDInventory.py
# Desc: Script CDINventory to store CD Inventory data
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Tiago, 2022-Nov-05, Updated File
# Tiago, 2022-Nov-12, Modefied to use dictionaries instead of Lists
#------------------------------------------#
# 1. Display menu allowing the user to choose: 'Add CD', 'Display Current Inventory', 'Save Inventory to file' and 'exit'
strChoice = ''
dicRow = []
lstTblData = []
lstRow = []
strFileName = 'MyData.txt'
objFile = None
while True:
    print('[a] Add CD \n[v] Display Current Inventury \n[s] Save Inventory to file \n[r] Read the Data in File \n[d] Delete data \n[x] Exit')
    Choice = input('Your choice:')

# 2. Exit the program if the user chooses so.
    if Choice.lower() == 'x':
        break
    
# 3. Add data to the table (2d-list) each time the user wants to add data
    if Choice.lower() == 'a':
        iid = int(input('Enter the Id '))
        name = input('What is the CDTitle? ')
        Aname = input('What is the artist name? ')
        dicRow = {'id' : iid, 'cdtitle' : name, 'artistname' : Aname}
        lstTblData.append(dicRow)

# 4. Display the current data to the user each time the user wants to display the data
    elif Choice.lower() == 'v':
        for item in lstTblData:
            print(item)

# 5. Save the data to a text file MyData.txt if the user chooses so
    elif Choice.lower() == 's':
        objF = open(strFileName, 'a')
        for row in lstTblData:
            objF.write(str(row['id']) + ',' + row['cdtitle'] + ',' + row['artistname'] + '\n')
        print('Added to MyData.txt file!')
        objF.close()
        
# 6. Read the Data from MyData.txt file
    elif Choice.lower() == 'r':
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id' : int(lstRow[0]), 'cdtitle' : lstRow[1], 'artistname' : lstRow[2]}
            print(dicRow)
        objFile.close()
# 7. Delete an entry
#open the file
#request an id to user
#insert all data inside a list
#itherate that list
#if the id requested is equal to the row['id'] then remove
#open the file
#update the data file
    elif Choice.lower() == 'd':
        delChoice = input('Select an Id to delete:')
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            if lstRow[0] == delChoice:
                lstRow.remove(lstRow[0])
            else:
                dicRow = {'id' : int(lstRow[0]), 'cdtitle' : lstRow[1], 'artistname' : lstRow[2]}
                lstTblData.append(dicRow)
        objFile.close()
        # this override the .txt file information
        objFile = open(strFileName, 'w')
        for row in lstTblData:
            objFile.write(str(row['id']) + ',' + row['cdtitle'] + ',' + row['artistname'] + '\n')
        objFile.close()
        lstTblData = []
        delChoice = None
# 8. Check if the User have choose something from the List
    else:
        print('Wrong choice')
        print('-------------------------')
    




