# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 01:38:54 2017

@author: NeeliGowri
"""

import os
import pandas as pd
import numpy as np
import mysql.connector as mariadb
#import plotly.plotly as py
#import plotly.graph_objs as go

#merging to common csv file
def merging():
     path = "E:/FALL/DAT900_DataArchitecture/Scott_DataArch_900/HW5_Baby/names/"

     listoffiles  = os.listdir(path)

     fout=open("E:/FALL/DAT900_DataArchitecture/Scott_DataArch_900/HW5_Baby/merged_babynames.csv","a")

     for i,j in enumerate(listoffiles):
        df3=[]
        listoffiles[i]= listoffiles[i].strip(".txt")
    #rows=listofifles[i].shape
        year=(listoffiles[i][-4:])

        df3 = pd.read_table(path+listoffiles[i]+".txt", sep = ",",header=None)
   
        new = np.repeat(year, df3.shape[0])
   
        df3['year']=new
      
        df3.to_csv(fout) 
        df3.rename(columns={0: 'Name', 1: 'Gender',2:'Frequency'}, inplace=True)

     fout.close()
     
#creating schemas and metadata and their relationships of the babynames data     
def toMariaDb():
      df4 = pd.read_csv("E:/FALL/DAT900_DataArchitecture/Scott_DataArch_900/HW5_Baby/merged_babynames.csv", sep = ",")
      
      ## to MariaDb
     
      con=mariadb.connect(user='Gowri',password='1234', database='babynames')

      cur = con.cursor(buffered=True)
      
      #Creating a table to MariaDb
      cur.execute('create table babynames_trial1(name varchar(25), gender char(1),frequency char(9), year char(4))')
      
      #Inserting vales to the created table and these values get reflected to MariaDb
      for x in range(0,df4.shape[0]):
   
           cur.execute("INSERT INTO babynames_trial1(name, gender, frequency, year) values (%s, %s,%s,%s)", 
                (df4['0'][x],df4['1'][x],str(df4['2'][x]),str(df4['year'][x])))


           con.commit()
           
def execQuery1(year_value):
      print(year_value)
      con=mariadb.connect(user='Gowri',password='1234', database='babynames')
      cur = con.cursor(buffered=True)
      #cur.execute('select * from  babynames_trial1 where year = '%s' group by gender'%(year_value)
      
      select_table = ("""select * from  babynames_trial1 where year = '%s' group by gender""")
      cur.execute(select_table%(year_value))
      
      rows = cur.fetchall()
      for row in rows:
          print(row)
          
          
def execQuery2(name_value,year_index,gender_value):
      lname=[]
      lgender=[]
      lyear=[]
      lfreq=[]
      if(year_index==0):
         year_value=['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
      elif(year_index==1): #1980 & later
         year_value=['1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999']
      elif(year_index==2): #1960 & later
         year_value=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979']
      elif(year_index==3): #1940 & later
         year_value=['1940','1941','1942','1943','1944','1945','1946','1947','1948','1949','1950','1951','1952','1953','1954','1955','1956','1957','1958','1959']
      elif(year_index==4): #1920 & later
         year_value=['1920','1921','1922','1923','1924','1925','1926','1927','1928','1929','1930','1931','1932','1933','1934','1935','1936','1937','1938','1939']
      elif(year_index==5): #1900 & later
         year_value=['1900','1901','1902','1903','1904','1905','1906','1907','1908','1909','1910','1911','1912','1913','1914','1915','1916','1917','1918','1919']
      
      year_len=len(year_value)
         
      con=mariadb.connect(user='Gowri',password='1234', database='babynames')
      cur = con.cursor(buffered=True) #buffered=True
     # if(gender_value=='M'):
          #cur.execute('select name, max(freq), dyear from babynames_trial1 where name = name_value group by year_value')
      select_table = ("""select name, max(frequency), year from  babynames_trial1 where name= '%s'and gender='%s' group by year='%s'""")
     
      for index in range(0,year_len):
          
          cur.execute(select_table%(name_value,gender_value,year_value[index]))
          
      #elif(gender_value=='F'):
          #cur.execute('select name, max(freq), dyear from babynames_trial1 where name = name_value group by year_value')
         # select_table = ("""selectname, max(freq), year from  babynames_trial1 where name= '%s' and gender='%s' group by year='%s'""")
         # cur.execute(select_table%(name_value,gender_value,year_value))
        
          rows = cur.fetchall()
      
          #for row in rows:
         # print('in printing')
          lname.append(rows[1][0])
          lfreq.append(rows[1][1])
          lyear.append(rows[1][2])
          print(rows[1])
      print('end')
      
      #query2=pd.DataFrame('name'=lname,'freq'=lfreq,'year'=lyear)
      
     
     #df = web.DataReader("frequency", 'year',
                   # datetime(2015, 1, 1),
                   # datetime(2016, 7, 1))

    #
    #py.iplot(data)