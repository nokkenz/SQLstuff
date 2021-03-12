import sqlite3 as conector
from models import Person, Car
import random

conection = conector.connect("./base.db")
cursor = conection.cursor()

idNumber = random.randint(0,100)

def db():

    whatToDo = input('What you want to do ? ').strip()

    if whatToDo in 'updateUPDATEUpdateuPDATE':

        try:

            what = input('In which table you want to update? ')

            newValue, condition = input('The new value :'),input('Whats the condition : ')
            
            comand = '''UPDATE ''' + what + ''' SET ''' + newValue + ''' WHERE ''' + condition

            cursor.execute(comand)

            conection.commit()
            cursor.close()
            conection.close()

        except conection.OperationalError as err:
            print(err)
            db()

    elif whatToDo in ('INSERTinsertInsertiNSERT'):
        try:
                          
            cursor.execute('''SELECT name from sqlite_master where type= "table"''')

            data = cursor.fetchall()

            print(data)

            insertInto = input('In wich table would you like to insert ? ')

            if insertInto in 'Person':
                try:
                    name,birth = input("Enter the name : ").title(),input("Enther the date of birth (use '/' to separate): ")

                    person = Person(idNumber, name , birth)
            
                    comando = '''INSERT INTO Person VALUES (:id, :name, :birth)'''

                    print('success')

                    cursor.execute(comando, vars(person))

                except conection.Error as err:

                    print(err)

            elif insertInto in 'carCARCarcAR':

                try:    
                    model, year, motor = input('Whats the model? ').title(),input('The year? '), input('Whats the motor? ')

                    car = Car(idNumber,model, year, motor)

                    comando = '''INSERT INTO Car VALUES(:id, :model, :year, :motor)'''

                    cursor.execute(comando, vars(car))
               
                except conection.Error as err:
                    
                    print(err)
            
            conection.commit()
            cursor.close()
            conection.close()



        except conector.OperationalError as err:
            print(repr(err))
            print('Table created, please redo the operation')

            createTable = '''CREATE TABLE Person(id PRIMARY KEY, name CHAR(25), birth CHAR)'''

            cursor.execute(createTable)

            conection.commit()

            print('Table created')

            cursor.close()
            conection.close()

    elif whatToDo in 'CREATEcreateCreatecREATE':
            try:
                tableName = input('Whats the table name and the parameters :')

                createTable = '''CREATE TABLE ''' + tableName

                cursor.execute(createTable)

                conection.commit()

                print('Successfully created')
                
                cursor.close()
                conection.close()

            except conector.OperationalError as err:
                print(err)
                db()

    elif whatToDo in 'DROPDropdropdROP':
        try:
            
            table = input('Table : ')

            comand = ''' DROP TABLE IF EXISTS '''+ table

            cursor.execute(comand)

            conection.commit()
            print('Table deleted successfully')

            cursor.close()
            conection.close()
        
        except conection.Error as err:
            print(err)
            db()
            
            
    elif whatToDo in 'DELETEdeleteDeletedELETE':
        try:        
            
            table, parameters = input('From with table ? '), input('Parameters to the deletion : ')

            comand = '''DELETE FROM ''' + table + ''' WHERE ''' + parameters 
                
            cursor.execute(comand)

            conection.commit()
            print('Successfully deleted')

            cursor.close()
            conection.close()
            
        except conection.DatabaseError as err:
            print(err)
            db()

    elif whatToDo in 'FETCHALLfetchallFetchallfETCHALLgetGETgETGetSELECTSelectsELECTselect':
        try:
            
            data = input('What to fetch ? ')

            if data in '*':
                
                table = input('From whith table ? ')

                comand = '''SELECT ''' + data + ''' FROM ''' +  table 

                cursor.execute(comand)

                data = cursor.fetchall()

                print('The data recovered was : ' + repr(data))

                conection.commit()

                cursor.close()
                conection.close()

            else:

                table, parameters = input('From whith table ? '), input('Where...')

                comand = '''SELECT ''' + data + ''' FROM ''' +  table + ''' WHERE ''' + parameters 

                cursor.execute(comand)

                data = cursor.fetchall()

                print('The data recovered was : ' + repr(data))

                conection.commit()

                cursor.close()
                conection.close()
        
        except conection.Error as error:
            print(error)
            db()

    else:
        print('Invalid parameters')
        db()

if __name__ == '__main__':
    db()