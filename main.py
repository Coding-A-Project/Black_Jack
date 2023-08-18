import sqlite3
import random
from pathlib import Path
K=Path('./U.db')
if K.is_file()==False:
    N=sqlite3.connect('U.db')
    Q=N.cursor()
    Q.execute("CREATE TABLE U(\
    pn TEXT,\
    password TEXT,\
    P INT NOT NULL,\
    PRIMARY KEY(pn))")
    N.commit()
h=0
while h==0:
    SL=input('Sign Up Or Login: ').upper()
    if SL=='LOGIN':
        i=0
        while i==0:
            N=sqlite3.connect('U.db')
            Q=N.cursor()
            U=input('Enter Username: ')
            Q.execute('SELECT*from U where pn="'+U+'"')
            R=Q.fetchall()
            if bool(R)==False:
                print('Wrong Username Or You Did Not Create Your Account')
            else:
                i+=1
        P=R[0][2]
        if len(R)>0:
            T=R[0][1]
            E=input('Enter Password: ')
            while E!=T:
                E=input('Password Is Wrong Please Try Again: ')
            print('Points: ',P)
            h+=1
    elif SL=='SIGN UP':
        N=sqlite3.connect('U.db')
        Q=N.cursor()
        i=0
        while i==0:
            U=input('Enter Username: ')
            Q.execute('SELECT*from U where pn="'+U+'"')
            R=Q.fetchall()
            if bool(R)==True:
                print('Username Taken')
            else:
                i+=1
        E=input('Welcome, Please Create Your Password: ')
        Q.execute('INSERT INTO U VALUES(?,?,?)',(U,E,1000))
        N.commit()
        R=Q.fetchall()
        h+=1
    else:
        print('Enter A Proper Command')
def G():
    Q.execute('SELECT pn,P FROM U ORDER BY P')
    R2=Q.fetchall()
    a=len(R2)
    a-=1
    while a<=len(R2) and a>=0:
        R3=R2[a]
        print(R3[0],'-',R3[1])
        a-=1
    Q.execute('SELECT*from U where pn="'+U+'"')
    R=Q.fetchall()
    P=R[0][2]
    k=0
    while k==0:
        try:
            B=eval((input('Enter Bet: ')))
        except NameError:
            print('Enter A Proper Number')
        else:
            if B>P:
                print('Bet Too High')
            elif B<=0:
                print("Hey,You Can't Bet Less Than 0 Points")
            elif B<=P:
                P-=B
                Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
                k+=1
    D=('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    C=''.join(random.sample(D,1))
    C2=''.join(random.sample(D,1))
    Y=''.join(random.sample(D,1))
    Y2=''.join(random.sample(D,1))
    O=Y
    O2=Y2
    R=C
    R2=C2
    l=0
    if O=='A':
        while l==0:
            O=eval(input('Enter Value For Ace Card (1 or 11) (This Is Your First Card): '))
            if O==1 or O==11:
                l+=1
            else:
                print('Invalid Number')
    elif O=='J' or O=='Q' or O=='K':
        O=10
    else:
        O=int(O)
    if O2=='A':
        l=0
        while l==0:
            print('Your First Card Is '+ Y)
            O2=eval(input('Enter Value For Ace Card (1 or 11): '))
            if O2==1 or O2==11:
                l+=1
            else:
                print('Invalid Number')
    elif O2=='J' or O2=='Q' or O2=='K':
        O2=10
    else:
        O2=int(O2)
    X=O+O2
    print('You: ',Y,Y2,'Sum =',X)
    if X==21:
        P+=B*2
        Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
        N.commit()
        print('Points: ',P)
        print('You Won As You Got To 21 First.')
        G()
    if R=='A':
        R=11
    elif R=='J' or R=='Q' or R=='K':
        R=10
    else:
        R=int(R)
    W=R
    print('Computer: ',C,'Sum =',W)
    if R2=='A':
        if W+11<=21:
            R2=11
        else:
            R2=1
    elif R2=='J' or R2=='Q' or R2=='K':
        R2=10
    else:
        R2=int(R2)
    W+=R2
    if W==21:
        print('Computer: ',C,C2,'Sum =',W)
        print('The Computer Won On Its First Hand')
        if P==0:
            P+=1
        Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();G()
    if X<21:
        UC0=input('Hit, Stand Or Double: ').upper()
        j=0
        while j==0:
            if UC0!='HIT' and UC0!='STAND' and UC0!='DOUBLE':
                print('Enter A Proper Command: ')
                UC0=input('Hit, Stand or Double: ').upper()
            elif UC0=='DOUBLE':
                if B>P:
                    print('You Do Not Have Enough Points To Double')
                    UC0=input('Hit or Stand: ').upper()
                else:
                    P-=B
                    B*=2
                    Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
                    j+=1
                    UC0='HIT'
            else:
                j+=1
    if UC0=='HIT':
        Y3=''.join(random.sample(D,1))
        O=Y3
        l=0
        if O=='A':
            while l==0:
                O=eval(input('Enter Value For Ace Card (1 or 11): '))
                if O==1 or O==11:
                    l+=1
                else:
                    print('Invalid Number')
        elif O=='J' or O=='Q' or O=='K':
            O=10
        else:
            O=int(O)
        X+=O
        I1='i'
        print('You: ',Y,Y2,Y3,'Sum =',X)
        if X==21:
            P+=B*2
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('You Won As You Got To 21 First.')
            G()
        if X>21:
            if P==0:
                P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('You Lost As You Got Over 21 And Busted.')
            G()
            if X==21:
                P+=B*2
                Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
                N.commit()
                print('Points: ',P)
                print('You Won As You Got To 21 First.')
                G()
    else:
        print('You: ',Y,Y2,'Sum =',X)
    if W<=15:
        Z2='Hit'
    if X>W and UC0=='STAND':
        Z2='Hit'
    else:
        Z2='Stand'
    if Z2=='Hit':
        C3=''.join(random.sample(D,1));R=C3
        if R=='A':
            if W+11<=21:
                R=11
            else:
                R=1
        elif R=='J' or R=='Q' or R=='K':
            R=10
        else:
            R=int(R)
        W+=R
        J1='i'
        print('Computer: ',C,C2,C3,'Sum =',W)
        if W==21:
            if P==0:
                P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('You Lost As The Computer Got To 21 First.')
            G()
        if W>21:
            P+=B*2
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('You Won As The Computer Got Over 21 And Busted.')
            G()
    elif Z2=='Stand':
        print('Computer: ',C,C2,'Sum =',W)
    UC=input('Hit, Stand or Double: ').upper()
    j=0
    while j==0:
        if UC!='HIT' and UC!='STAND' and UC!='DOUBLE':
            print('Enter A Proper Command: ')
            UC=input('Hit, Stand or Double: ').upper()
        elif UC=='DOUBLE':
            if B>P:
                print('You Do Not Have Enough Points To Double')
                UC=input('Hit or Stand: ').upper()
            else:
                P-=B
                B*=2
                Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
                j+=1
                UC='HIT'
        else:
            j+=1
    if UC=='HIT':
        Y4=''.join(random.sample(D,1))
        O=Y4
        if O=='A':
            l=0
            while l==0:
                O=eval(input('Enter Value For Ace Card (1 or 11): '))
                if O==1 or O==11:
                    l+=1
                else:
                    print('Invalid Input')
        elif O=='J' or O=='Q' or O=='K':
            O=10
        else:
            O=int(O)
        X+=O
        try:
            I1
        except NameError:
            I2='i'
            print('You: ',Y,Y2,Y4,'Sum =',X)
        else:
            I2='i'
            print('You: ',Y,Y2,Y3,Y4,'Sum =',X)
        if X==21:
            P+=B*2
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('You Won As You Got To 21 First.')
            G()
        if X>21:
            if P==0:
                P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('You Lost As You Got Over 21 And Busted.')
            G()
    if UC=='STAND':
        try:
            I1
        except NameError:
            print('You: ',Y,Y2,'Sum =',X)
        else:
            print('You: ',Y,Y2,Y3,'Sum =',X)
    if W<=15:
        Z4='Hit'
    if X>W and UC=='STAND':
        Z4='Hit'
    else:
        Z4='Stand'
    if Z4=='Hit':
        C4=''.join(random.sample(D,1));R=C4
        if R=='A':
            if W+11<=21:
                R=11
            else:
                R=1
        elif R=='J' or R=='Q' or R=='K':
            R=10
        else:
            R=int(R)
        W+=R
        try:
            J1
        except NameError:
            J2='i'
            print('Computer: ',C,C2,C4,'Sum =',W)
        else:
            J2='i'
            print('Computer: ',C,C2,C3,C4,'Sum =',W)
        if W==21:
            if P==0:
                P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('You Lost As The Computer Got To 21 First.')
            G()
        if W>21:
            P+=B*2
        Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
        N.commit()
        print('Points: ',P)
        print('You Won As The Computer Got Over 21 And Busted.')
        G()
    else:
        try:
            J1
        except NameError:
            print('Computer: ',C,C2,'Sum =',W)
        else:
            print('Computer: ',C,C2,C3,'Sum =',W)
    UC2=input('Hit, Stand or Double: ').upper()
    j=0
    while j==0:
        if UC2!='HIT' and UC2!='STAND' and UC2!='DOUBLE':
            print('Enter A Proper Command: ')
            UC2=input('Hit, Stand or Double: ').upper()
        elif UC2=='DOUBLE':
            if B>P:
                print('You Do Not Have Enough Points To Double')
                UC2=input('Hit or Stand: ').upper()
            else:
                P-=B
                B*=2
                Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
                j+=1
                UC2='HIT'
        else:
            j+=1
    if UC2=='HIT':
        Y5=''.join(random.sample(D,1))
        O=Y5
        if O=='A':
            l=0
            while l==0:
                O=eval(input('Enter Value For Ace Card (1 or 11): '))
                if O==1 or O==11:
                    l+=1
                else:
                    print('Invalid Number')
        elif O=='J' or O=='Q' or O=='K':
            O=10
        else:
            O=int(O)
        X+=O
        try:
            I1
        except NameError:
            try:
                I2
            except NameError:
                print('You: ',Y,Y2,Y5,'Sum =',X)
            else:
                print('You: ',Y,Y2,Y4,Y5,'Sum =',X)
        else:
            try:
                I2
            except NameError:
                print('You: ',Y,Y2,Y3,Y5,'Sum =',X)
            else:
                print('You: ',Y,Y2,Y3,Y4,Y5,'Sum =',X)
        if X==21:
            P+=B*2
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('You Won As You Got To 21 First.')
            G()
        if X>21:
            if P==0:
                P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('You Lost As You Got Over 21 And Busted.')
            G()
    else:
        try:
            I1
        except NameError:
            try:
                I2
            except NameError:
                print('You: ',Y,Y2,'Sum =',X)
            else:
                print('You: ',Y,Y2,Y4,'Sum =',X)
        else:
            try:
                I2
            except NameError:
                print('You: ',Y,Y2,Y3,'Sum =',X)
            else:
                print('You: ',Y,Y2,Y3,Y4,'Sum =',X)
    if W<=15:
        Z6='Hit'
    elif X>W and UC2=='STAND':
        Z6='Hit'
    else:
        Z6='Stand'
    if Z6=='Hit':
        C5=''.join(random.sample(D,1))
        R=C5
        if R=='A':
            if W+11<=21:
                R=11
            else:
                R=1
        elif R=='J' or R=='Q' or R=='K':
            R=10
        else:
            R=int(R)
        W+=R
        try:
            J1
        except NameError:
            try:
                J2
            except NameError:
                print('Computer: ',C,C2,C5,'Sum =',W)
            else:
                print('Computer: ',C,C2,C4,C5,'Sum =',W)
        else:
            try:
                J2
            except NameError:
                print('Computer: ',C,C2,C3,C5,'Sum =',W)
            else:
                print('Computer: ',C,C2,C3,C4,C5,'Sum =',W)
    else:
        try:
            J1
        except NameError:
            try:
                J2
            except NameError:
                print('Computer: ',C,C2,'Sum =',W)
            else:
                print('Computer: ',C,C2,C4,'Sum =',W)
        else:
            try:
                J2
            except NameError:
                print('Computer: ',C,C2,C3,'Sum =',W)
            else:
                print('Computer: ',C,C2,C3,C4,'Sum =',W)
    if W>21:
        P+=B*2
        Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
        N.commit()
        print('Points: ',P)
        print('You Won As The Computer Got Over 21 And Busted.')
        G()
    if X>21:
        if P==0:
            P+=1
        Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
        N.commit()
        print('Points: ',P)
        print('You Lost As You Got Over 21 And Busted.')
        G()
    else:
        if X>W:
            P+=B*2
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('You Won As You Stood With A Higher Score Than The Computer.')
            G()
        if W>X:
            if P==0:
                P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('You Lost As You Stood With A Lower Score Than The Computer.')
            G()
        if W==X:
            P+=B
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P))
            N.commit()
            print('Points: ',P)
            print('It was a draw!')
            G()
G()