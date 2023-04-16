"""CONVENTIONS:
When we pass in a row or column number as an argument, it should be the computer's index, not the human one.
We trust anything we pass in as an argument (do the error checking beforehand)
User input inside of a method is filtered as soon as it is received
All object methods occur in-place, meaning they change the properties of the object itself. If you would like to preserve the original object, make a duplicate before doing calculations

"""
import copy

#The matrix object will be defined with all of the properties necessary to behave like the analogous mathematical object
class Matrix(object):
    #when we make the matrix, we take the number of rows and columns, and make an empty 2D list. Doing it like this allows us to access a particular entry as self.__values[row#][col#]
    #By default is a 3x3 matrix of zeroes
    def __init__(self,rows=3,columns=3):
        self.__rows = rows
        self.__columns = columns
        emptyRow = [0]*self.__columns
        self.__values = [emptyRow]*self.__rows



#GETTERS AND SETTERS

    #determines if the matrix is square, returns true if square, false if not
    def getSquare(self):
        if self.__rows == self.__columns:
            squareBool = True
        else:
            squareBool = False
        return squareBool

    #finds the index of that row containing a pivot. Returns the value of the last column if no pivot was found.
    def findPivot(self,row):
        try:
            pivotIndex = row.index(1.0)
        except:
            pivotIndex = self.__columns - 1

        return pivotIndex

    #returns the matrix values as a 2D list. Use this for calculations
    def getMatrix(self):
        return self.__values

    #returns the specified row vector
    def getRowValues(self,row):
        return self.__values[row]


    #use this to change the values in one row of the matrix
    def setRowValues(self,rowNumber):
        invalidRow = True
        #loops while there is no valid set of row entries
        while invalidRow:
            userValues = input("Please give the entries for row {}, separated by commas: ".format(rowNumber+1))
            try:
                #maps the user's entries from strings to floats
                listValues = list(map(float,userValues.split(",")))
            except ValueError:
                #this exception arises whenever the user inputs something that isn't a float, such as a letter
                print("All inputs must be floating-point numbers")
            except:
                #otherwise something bad happened and we're not sure what
                print("Something went wrong, please try again!")
            else:
                #checks to see if the user inputted the correct number of values
                if len(listValues) == self.__columns:
                    self.__values[rowNumber] = listValues
                    invalidRow = False
                #we don't want to mess up the number of columns, so we reject any input that has the wrong number of entries
                else:
                    print("Oops! Row {} must have {} entries!".format(rowNumber+1,self.__columns))


    #Use this to create a completely new matrix from scratch, does this by setting each row individually
    def setNewMatrix(self):
        for row in range(self.__rows):
            self.setRowValues(row)

    #If the matrix is square, we need to make an identity matrix of the same dimensions
    def setSquareIdentity(self):
        identity = []
        for row in range(self.__rows):
            rowList = []
            for column in range(self.__columns):
                if row == column:
                    rowList.append(1.0)
                else:
                    rowList.append(0.0)
            identity.append(rowList)

        return identity


    #Use this to get the value at one particular entry in the matrix.
    def getEntryValue(self,row,column):
        return self.__values[row][column]

    #Use this to change the value at one particular entry in the matrix.
    def setEntryValue(self, row, column):
        invalidInput = True
        #runs until the user has provided a valid new input
        while invalidInput:
            try:
                newValue = float(input("What is the new value at index ({},{})?: ".format(row+1,column+1)))
            except:
                print("Input must be a floating-point number")
            else:
                #changes the value at that index to the new one
                self.__values[row][column] = newValue
                invalidInput = False

    #returns the specified column vector
    def getColumnValues(self, column):
        columnVector = []
        for row in self.__values:
            columnVector.append(row[column])
        return columnVector

    #changes the specified column vector
    def setColumnValues(self,column):
        invalidColumn = True
        #loops while there is no valid set of row entries
        while invalidColumn:
            userValues = input("Please give the entries for column {}, separated by commas: ".format(column+1))
            try:
                #maps the user's entries from strings to floats
                listValues = list(map(float,userValues.split(",")))
            except ValueError:
                #this exception arises whenever the user inputs something that isn't a float, such as a letter
                print("All inputs must be floating-point numbers")
            except:
                #otherwise something bad happened and we're not sure what
                print("Something went wrong, please try again!")
            else:
                #checks to see if the user inputted the correct number of values
                if len(listValues) == self.__rows:
                    for row, value in enumerate(listValues):
                        self.__values[row][column] = value
                    invalidColumn = False
                #we don't want to mess up the number of rows, so we reject any input that has the wrong number of entries
                else:
                    print("Oops! Column {} must have {} entries!".format(column+1,self.__rows))


#ELEMENTARY ROW OPERATIONS
    #swaps the values of the two specified rows
    def swapRows(self,row1,row2):
        #saves the values in the two rows
        row1Values = self.getRowValues(row1)
        row2Values = self.getRowValues(row2)

        #changes the values
        self.__values[row1] = row2Values
        self.__values[row2] = row1Values

    #rescales a row in the matrix
    def rescaleRow(self,row,multiple):
        #saves the values in the given row
        rowValues = self.getRowValues(row)

        #goes through every index,value pair, and multiplies the current value by the specified factor
        for index, value in enumerate(rowValues):
            value *= multiple
            #saves the newly-scaled factor to the same index in the list of values
            rowValues[index] = value
        #changes the specified row to its newly-scaled version
        self.__values[row] = rowValues

    #Adds a specified multiple of row1 onto row2
    def addRowMultiple(self,row1,row2,multiple):
        #gets the values in each row
        row1Values = self.getRowValues(row1)
        row2Values = self.getRowValues(row2)

        #iterates over every index, value pair of row1Vlaues
        for index, currentValue1 in enumerate(row1Values):
            #takes the current value and obtains the desired multiple
            currentValue1 *= multiple
            #adds the current value to the corresponding index in row 2
            row2Values[index] += currentValue1

        #saves the changed values
        self.__values[row2] = row2Values

#DISPLAY
 #prints the matrix in a way that looks familiar. Use this for display
    def printMatrix(self):
        for row in self.__values:
            print(row)

    #Computes the reduced row echelon form of the current matrix. THE BIG GOAL
    def findMatrixRREF(self):
        #iterates over every single row in the matrix looking for a pivot, and clearing the column that pivot is in.
        for rowOuter in range(self.__rows):
            firstValue = True
            currentIndex = 0
            multiple = 0
            rowValues = self.getRowValues(rowOuter)

            #finds the first nonzero entry in each row, and turns it into a one. Fails if there are no nonzero entries in a row.
            for value in rowValues:
                if value != 0 and firstValue:
                    multiple = 1/value
                    currentIndex = rowValues.index(value)
                    firstValue = False
            if multiple != 0:
                self.rescaleRow(rowOuter,multiple)
                colVector = self.getColumnValues(currentIndex)

                #once we have a rowOuter with a pivot, we rescale it  by the negative of the other values in that column, and add to the other rows, clearing the column
                for rowInner in range(self.__rows):
                    if rowInner != rowOuter:
                        self.addRowMultiple(rowOuter,rowInner,-colVector[rowInner])

        #sorts the matrix by where the pivots are located
        self.__values.sort(key=self.findPivot)

        #replaces all of the weird negative zeroes with just regular zeroes
        for row in range(self.__rows):
            for column in range(self.__columns):
                if self.getEntryValue(row,column) == (-0.0):
                    self.__values[row][column] = 0.0

    #Uses the RREF to compute the inverse matrix, if it exists
    def computeInverse(self):
        invertedMatrix = False
        #if the matrix isn't square, it is not invertible
        if self.getSquare() == False:
            print("The matrix is not invertible because it is not square")
        else:
            rrefResult = []
            #builds an identity matrix of the correct size
            identity = self.setSquareIdentity()
            #forms an augmented matrix by extending each row using the corresponding row of the identity matrix
            for index in range(self.__rows):
                self.__values[index].extend(identity[index])

            #the number of columns has doubled
            self.__columns *= 2
            #reduces the matrix to RREF
            self.findMatrixRREF()

            #technically this checks the transpose of the left side of the augmented matrix, but since the identity is its own transpose, this is fine
            for column in range(int(self.__columns/2)):
                rrefResult.append(self.getColumnValues(column))
            #if the left side of the augmented matrix is not the identity after being put in RREF, the matrix is not invertible
            if rrefResult != identity:
                print("The matrix is not invertible because RREF is not the identity")
            #otherwise, the inverse matrix is the right hand side of the augmented matrix
            else:
                invertedMatrix = True
                for index,row in enumerate(self.__values):
                    self.__values[index] = row[int(self.__columns/2):]

        return invertedMatrix


def menu():
    keepGoing = True
    while keepGoing:
        userResponse = input("""\nWhat would you like to do?
        0. Exit Program
        1. Input New Matrix
        2. Change the Values in a Row
        3. Change the Values in a Column
        4. Display Current Matrix
        5. Compute RREF of Current Matrix
        6. Compute Inverse of Current Matrix\n""")

        if userResponse == "0":
            keepGoing = False
        elif userResponse == "1":
            try:
                rowNum = int(input("Number of Rows: "))
                colNum = int(input("Number of Columns: "))
            except:
                print("Oops, something went wrong. Please make sure the row and column numbers are integers.")
            else:
                matrix = Matrix(rowNum, colNum)
                matrix.setNewMatrix()
        elif userResponse == "2":
            try:
                rowNum = int(input("Which row would you like to change?: "))
                #the argument needs to be the computer index, not the human one
                matrix.setRowValues(rowNum-1)
            except:
                print("Oops, something went wrong. Please make sure the row number is an integer and a matrix has been created")
        elif userResponse == "3":
            try:
                colNum = int(input("Which column would you like to change?: "))
                #the argument needs to be the computer index, not the human one
                matrix.setColumnValues(colNum-1)
            except:
                print("Oops, something went wrong. Please make sure the column number is an integer and a matrix has been created")
        elif userResponse == "4":
            try:
                matrix.printMatrix()
            except:
                print("Oops! Something went wrong, or there was no matrix to display")
        elif userResponse == "5":
            try:
                rrefMatrix = copy.deepcopy(matrix)
                rrefMatrix.findMatrixRREF()
                print("The RREF of the current matrix is:\n ")
                rrefMatrix.printMatrix()
            except:
                print("Oops! Something went wrong, or there was no matrix to display")
        elif userResponse == "6":
            try:
                inverseMatrix = copy.deepcopy(matrix)
                result = inverseMatrix.computeInverse()
                if result == True:
                    print("The inverse of the current matrix is:\n ")
                    inverseMatrix.printMatrix()
            except:
                print("Oops! Something went wrong, or there was no matrix to display")


if __name__ == "__main__":
    menu()

