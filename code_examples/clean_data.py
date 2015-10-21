import pandas as pd
import numpy as np
import re

#reading in data, dropping unnecessary columns, and creating a value
#column to show a players cost per point
players = pd.read_csv('data_files/fd_data')
players = players.drop('Unnamed: 12',1)
players = players.drop('Unnamed: 13',1)
players = players.drop('Game',1)
players = players.drop('Id',1)
#alt method
players['eff-scr'] = np.round((players['Salary']/players['FPPG'])/266.66,decimals=2)
players['value'] = np.round(players['Salary']/players['FPPG'],decimals=2)


#read in and clean passing data
passing = pd.read_csv('data_files/passing')
passing = passing[['Unnamed: 1','Tm', 'Pos', 'Yds','TD', 'Y/G', 'Int']]
passing.columns = ['Name','Team', 'Position', 'Yds','TD', 'Y/G', 'Int']
passing = passing.replace('qb','QB')
passing = passing.replace({'Team' : { 'SFO' : 'SF', 'NWE' : 'NE', 'JAX' : 'JAC','TAM':'TB', 'NOR':'NO','KAN':'KC','SDG':'SD','GNB':'GB' }})

passing = passing.dropna(subset=['Name'])
clean_names = passing.Name.str.split().tolist()
first_name = []
last_name = []
for n in clean_names:
    first_name.append(n[0])
    last_name.append(n[1])

passing['Last Name'] = last_name
passing['First Name'] = first_name
passing = passing.drop('Name',1)


#read in and clean rushing data
rush_rec = pd.read_csv('data_files/rushing')
rushing = rush_rec.ix[:,:14]
rushing.columns = ['RK','Name','Team' ,'Age','Position','G','GS','Touches',
                   'Yds','TD','Long','Y/A','Y/G','Touch_Game']


rushing = rushing.drop('G',1)
rushing = rushing.drop('GS',1)
rushing = rushing.drop('Y/A',1)
rushing = rushing.drop('RK',1)
rushing = rushing.drop('Age',1)
rushing = rushing.drop('Long',1)
rushing = rushing.replace('wr','WR')
rushing = rushing.replace('rb','RB')
rushing = rushing.replace('qb','QB')
rushing = rushing.replace({'Team' : { 'SFO' : 'SF', 'NWE' : 'NE', 'Jax' : 'Jac','TAM':'TB', 'NOR':'NO','KAN':'KC','SDG':'SD','GNB':'GB' }})
rushing = rushing.dropna(subset=['Name'])

clean_names = rushing.Name.str.split().tolist()
first_name = []
last_name = []
for n in clean_names:
    first_name.append(n[0])
    last_name.append(n[1])
rushing['Last Name'] = last_name
rushing['First Name'] = first_name
rushing = rushing.drop('Name',1)


#read in and clean receiving data
receiving = pd.read_csv('data_files/receiving')
# receiving = receiving.fillna(0)
receiving = receiving[['Unnamed: 1', 'Tm', 'Pos', 'Tgt', 'Rec', 'Yds', 'Y/R',
'TD','R/G','Y/G']]
receiving.columns = ['Name', 'Team', 'Position', 'Tgt', 'Rec', 'Yds', 'Y/R', 'TD',
'R/G','Y/G']
receiving = receiving.replace('wr','WR')
receiving = receiving.replace('rb','RB')
receiving = receiving.replace('qb','QB')
receiving = receiving.replace('te','TE')

receiving = receiving.replace({'Team' : { 'SFO' : 'SF', 'NWE' : 'NE', 'Jax' : 'Jac','TAM':'TB', 'NOR':'NO','KAN':'KC','SDG':'SD','GNB':'GB' }})
receiving = receiving.dropna(subset=['Name'])
receiving['Tgt'] = receiving['Tgt'].astype(float)


clean_names = receiving.Name.str.split().tolist()
first_name = []
last_name = []
for n in clean_names:
    first_name.append(n[0])
    last_name.append(n[1])

receiving['Last Name'] = last_name
receiving['First Name'] = first_name
receiving = receiving.drop('Name',1)


#merge tables
quarterbacks = pd.merge(players,passing)
halfbacks = pd.merge(players,rushing)
halfbacks = halfbacks[halfbacks.Position == 'RB']
receivers = pd.merge(players,receiving)
receivers['Played'].astype(float)
receivers['Tgt_PG'] = receivers['Tgt'] / receivers['Played']
wide_receivers = receivers[receivers.Position == 'WR']
tight_ends = receivers[receivers.Position == 'TE']
