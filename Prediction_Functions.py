from __future__ import division
import numpy as np
import matplotlib as mpl
import datetime as dt
import sys
import string
import random 
import math
import csv
import pandas as pd

#TOTAL GOALS SCORED/20
def average_total_goals_scored(goals_scored):
	avg_goals = 0
	i=0
	for i in range(len(goals_scored)):
		avg_goals=avg_goals+goals_scored[i]
	
	return avg_goals/len(goals_scored)

#AVG GOALS SCORED FOR EACH TEAM RESPECTIVELY
def average_goals_scored_for(goals_scored,total):
	avg_goals_for = []
	for i in range(0,len(goals_scored)):
		avg_goals_for.append(goals_scored[i]/total[i])
	
	return avg_goals_for

#AVERAGE GOALS SCORED FOR BY ALL TEAMS
def sum_average_goals_scored_for(avg_goals_for):
	sum_avg_goals_scored_for=0
	for i in range(0,len(avg_goals_for)):
		sum_avg_goals_scored_for=sum_avg_goals_scored_for+avg_goals_for[i]

	return sum_avg_goals_scored_for/20

#AVERAGE GOAL SCORED FOR EACH TEAM
def average_goals_scored_against(goals_scored,total):
	avg_goals_against = []
	for i in range(0,len(goals_scored)):
		avg_goals_against.append(goals_scored[i]/total[i])
	
	return avg_goals_against

def sum_average_goals_scored_against(avg_goals_against):
	sum_avg_goals_scored_against=0
	for i in range(0,len(avg_goals_against)):
		sum_avg_goals_scored_against=sum_avg_goals_scored_against+avg_goals_against[i]

	return sum_avg_goals_scored_against/20

def alpha(avg_goals_for):
	num = sum_average_goals_scored_for(avg_goals_for)
	alpha_value=[]
	for i in range(0,len(avg_goals_for)):
		alpha_value.append(avg_goals_for[i]/num)
	
	return alpha_value

def beta(avg_goals_against):
	num = sum_average_goals_scored_against(avg_goals_against)
	beta_value=[]
	for i in range(0,len(avg_goals_against)):
		beta_value.append(avg_goals_against[i]/num)
	
	return beta_value

def main():	
	db = pd.read_csv('2013-2014.csv')
	column_name = db['Team']
	column_FTHG_home = db['FH']
	column_FTHA_home = db['AH']
	column_FTHG_away = db['FA']
	column_FTHA_away = db['AA']
	total_home = db['TMH']
	total_away = db['TMA']
	#print (column_FTHG)
	#avg_total = average_total_goals_scored(column_FTHG)
	#print ('Average Total Goals : '),avg_goals
	home_avg_goal_per_game = average_goals_scored_for(column_FTHG_home,total_home)
	home_league_avg_goal_per_game = sum_average_goals_scored_for(home_avg_goal_per_game)
	alpha_list_home = alpha(home_avg_goal_per_game)
	home_avg_goalmiss_per_game = average_goals_scored_against(column_FTHA_home,total_home)
	home_league_avg_goalmiss_per_game = sum_average_goals_scored_against(home_avg_goalmiss_per_game)
	beta_list_home = beta(home_avg_goalmiss_per_game)
	
	away_avg_goal_per_game = average_goals_scored_for(column_FTHG_away,total_away)
	away_league_avg_goal_per_game = sum_average_goals_scored_for(away_avg_goal_per_game)
	alpha_list_away = alpha(away_avg_goal_per_game)
	away_avg_goalmiss_per_game = average_goals_scored_against(column_FTHA_away,total_home)
	away_league_avg_goalmiss_per_game = sum_average_goals_scored_against(away_avg_goalmiss_per_game)
	beta_list_away = beta(away_avg_goalmiss_per_game)
	
	data = {'Team':column_name,'Alpha_home':alpha_list_home,'Avg_goals_for_home':home_avg_goal_per_game,
	'Beta_home':beta_list_home,'Avg_goalmiss_for_home':home_avg_goalmiss_per_game,'Alpha_away':alpha_list_away,'Avg_goals_for_away':away_avg_goal_per_game,
	'Beta_away':beta_list_away,'Avg_goalmiss_for_away':away_avg_goalmiss_per_game}
	list = pd.DataFrame(data)
	list['Avg_goals_for_home'] = list['Avg_goals_for_home'].map('{:,.2f}'.format)
	list['Alpha_home'] = list['Alpha_home'].map('{:,.2f}'.format)
	list['Avg_goalmiss_for_home'] = list['Avg_goalmiss_for_home'].map('{:,.2f}'.format)
	list['Beta_home'] = list['Beta_home'].map('{:,.2f}'.format)
	list['Avg_goals_for_away'] = list['Avg_goals_for_away'].map('{:,.2f}'.format)
	list['Alpha_away'] = list['Alpha_away'].map('{:,.2f}'.format)
	list['Avg_goalmiss_for_away'] = list['Avg_goalmiss_for_away'].map('{:,.2f}'.format)
	list['Beta_away'] = list['Beta_away'].map('{:,.2f}'.format)
	list.to_csv('attack_defence.csv',index=False)
	
		
if __name__ == "__main__":
	main()
