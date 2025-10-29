from models.Database import Database
from models.Result import Result

class Person(Database):
    '''
        PERSON MODEL CLASS
            inherits from Database Class
            includes an aggregation of Results (one-to-many relationship)
    
    '''

    ''' Person Table Attributes '''
    __userName=None
    __firstName=None
    __lastName=None

    '''
    AGGREGATION of Results from Database
    '''
    __results=[]

    '''
    Local Static Variables
    '''
    __tableName="persons"
    __primaryKey="userName"
    __attributes=["userName","firstName","lastName"]


    def __init__(self,userName=None,firstName=None,lastName=None):
        '''
        Constructor
        '''
        super().__init__()  # Initialize the Database connection
        self.__userName=userName
        self.__firstName=firstName
        self.__lastName=lastName

        # if the person exists in database (based on Primary Key) then get Person from Database
        if self.__exists():
            self.__getPersonFromDB()

    '''
    GETTERS AND SETTERS
    '''
    def getUserName(self):
        return self.__userName

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getPrimaryKey(self):
        return self.getUserName()

    def setUserName(self,userName):
        self.__userName=userName

    def setFirstName(self,firstName):
        self.__firstName=firstName

    def setLastName(self,lastName):
        self.__lastName=lastName

    '''
        OBJECT-RELATIONAL METHODS
    '''
    def __exists(self):
        retCode = False

        if self.getPrimaryKey():
            sql = f"SELECT EXISTS(SELECT 1 FROM {__class__.__tableName} WHERE {__class__.__primaryKey} = ?) AS row_exists"
            params = (self.getPrimaryKey(),)
            result = self.query(sql,params)
            for row in result:
                if row['row_exists'] == 1:
                    retCode = True

        return retCode

    def __getPersonFromDB(self):
        '''
        Get a single Person from Database if UserName has been provided
        '''
        sql = f"SELECT {', '.join(__class__.__attributes)} FROM {__class__.__tableName} WHERE {__class__.__primaryKey} = ?"
        params = (self.getPrimaryKey(),)
        result = self.query(sql,params)
        for row in result:
            self.setUserName(row['userName'])
            self.setFirstName(row['firstName'])
            self.setLastName(row['lastName'])


    def getResultsForPerson(self):
        self.__results = []
        self.__results = Result.loadResultsForPerson(self)
        return self.__results

    def save(self):
        if self.__exists():
            self.__update()
        else:
            self.__insert()

    def __insert(self):
        sql = "INSERT INTO persons (userName, firstName, lastName) VALUES (?, ?, ?)"
        params = (self.__userName, self.__firstName, self.__lastName)
        self.__personId = self.query(sql, params)

    def __update(self):
        sql = "UPDATE persons SET firstName = ?, lastName = ? WHERE userName = ?"
        params = (self.__firstName, self.__lastName, self.__userName)
        self.query(sql, params)


    '''
    Business Methods

    '''
    def login(self,userName):

        self.setUserName(userName)
        if self.__exists():
            self.__getPersonFromDB()
            return True
        else:
            return False

    def addResult(self, word, attempts):
        result = Result(person=self, word=word, attempts=attempts)
        result.save()
        self.__results.append(result)


    def showResults(self):
        self.getResultsForPerson()
        for result in self.__results:
            print(result)


    '''
    Utility Methods

    '''
    def __str__(self):
        return f"{self.getUserName()} {self.getFirstName()} {self.getLastName()}"


'''
TEST HARNESS IS OUTSIDE OF THE CLASS DEFINITION
'''
def test():
    person = Person(userName="jbloggs")
    print(person)

    person.showResults()


if __name__ == "__main__":
    test()