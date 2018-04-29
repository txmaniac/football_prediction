from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import sys
import string
import random 
import math
import csv
import pandas as pd
	
def goal_expectancy(a,b,c):
	return (a*b*c)

def average_total_goals_scored(goals_scored):
	avg_goals = 0
	i=0
	for i in range(len(goals_scored)):
		avg_goals=avg_goals+goals_scored[i]
	
	return avg_goals/len(goals_scored)

def main():
	
	database = pd.read_csv('PremierLeague_Fixtures.csv')
	column_home = database['HomeTeam']
	column_away = database['AwayTeam']
	column_score_home = database['FTHG']
	column_score_away = database['FTAG']
	column_result = database['FTR']
	
	#home_team = input("Enter Home team : ")
	#away_team = input("Enter Away team : ")
	"""
	for i in range(0,len(column_away)):
		if column_home[i] == column_away[i]:
			actual_score = [db[i],db[i]]
	"""
	
	db2 = pd.read_csv('attack_defence.csv')
	column_alpha_home = db2['Alpha_home']
	column_alpha_away = db2['Alpha_away']
	column_beta_home = db2['Beta_home']
	column_beta_away = db2['Beta_away']
	column_avg_goal_away = db2['Avg_goals_for_away']
	column_avg_goal_home = db2['Avg_goals_for_home']
	column_team = db2['Team']
	count = 0
	
	for i in range(len(column_home)):
		home_team = column_home[i]
		away_team = column_away[i]
		actual_res = column_result[i]
		# finding the home team
		index = 0
		for index in range(0,len(column_team)):
			if column_team[index]==home_team:
				break
				
		alpha_home = column_alpha_home[index]
		avg_home = average_total_goals_scored(column_avg_goal_home)
		beta_home = column_beta_home[index]
		
		# finding the away team
		index = 0
		for index in range(0,len(column_team)):
			if column_team[index]==away_team:
				break
		
		alpha_away = column_alpha_away[index]
		avg_away = average_total_goals_scored(column_avg_goal_away)
		beta_away = column_beta_away[index]
		
		value_x = goal_expectancy(alpha_home,beta_away,avg_home)
		value_y = goal_expectancy(beta_home,alpha_away,avg_away)
		
		print (value_x,value_y)
		distribution_list = [[0 for x in range(6)] for y in range(6)]
		
		factor = 0
		for j in range(0,6):
			for i in range(0,6):
				if i==0 and j==0:
					factor = 1-(value_x*value_y*min(avg_home*avg_away/value_x*value_y,1)/avg_away*avg_home)
				elif i==1 and j==0:
					factor = 1+(value_y*min(avg_home*avg_away/value_x*value_y,1)/avg_away)
				elif i==0 and j==1:
					factor = 1+(value_x*min(avg_home*avg_away/value_x*value_y,1)/avg_away)
				elif i==1 and j==1:
					factor = 1-min(avg_home*avg_away/value_x*value_y,1)
				else :
					factor = 1
					
				distribution_list[i][j] = factor*(math.exp(-value_x) * value_x**i / math.factorial(i))*(math.exp(-value_y) * value_y**j / math.factorial(j))
		
		index_home=0
		index_away=0
		max_int=0
		for i in range(0,6):
			for j in range(0,6):
				if max_int < distribution_list[i][j]:
					max_int = distribution_list[i][j]
					index_home=i
					index_away=j
		
		sum_win=0
		sum_draw=0
		sum_loss=0
		for i in range(0,6):
			for j in range(0,6):
				if i>j:
					sum_win=sum_win+distribution_list[i][j]
				if i==j:
					sum_draw=sum_draw+distribution_list[i][j]
				if i<j:
					sum_loss=sum_loss+distribution_list[i][j]
		print ("Match has probable score of ",index_home,"-",index_away)
		
		a=sum_win
		b=sum_draw
		c=sum_loss
		
	
		if a>b and a>c:
			max_prob=a
		elif b>a and b>c:
			max_prob=b
		elif c>a and c>b:
			max_prob=c
		
		if sum_win==max_prob:
			res = 'H'
		if sum_draw==max_prob:
			res = 'D'
		if sum_loss==max_prob:
			res = 'A'
		
		"""
		if index_home>index_away:
			res = "H"
		if index_home==index_away:
			res = "D"
		if index_home<index_away:
			res = "A"
		"""	
		
		print ("Home team : ",home_team,"Away team : ",away_team)
		print ("Win probability for home team : ",sum_win)
		print ("Draw probability : ",sum_draw)
		print ('Loss probability for home team : ',sum_loss)
		
		
		if res==actual_res:
			print (res)
			print (actual_res)
			count=count+1;
			print (count) 
		"""
		sec = [0,distribution_list[0][0],distribution_list[1][0],distribution_list[2][0],distribution_list[3][0],distribution_list[4][0],distribution_list[5][0]]
		fir = [0,distribution_list[0][0],distribution_list[0][1],distribution_list[0][2],distribution_list[0][3],distribution_list[0][4],distribution_list[0][5]]
		goals = [0,1,2,3,4,5,6]
		plt.plot(goals, sec,marker='*', c='r', label = home_team)
		plt.plot(goals, fir,marker='*', c='b', label = away_team)
		#plt.plot(abs_res,column_away,linestyle='None',marker='*', c='y', label = 'Predicted Outcome')
		plt.title('Probabilities of Arsenal and Cardiff City')
		plt.ylabel('Probabilities')
		plt.xlabel('Goals')
		plt.legend()
		plt.show()
		"""
	accuracy = (count*100)/len(column_home)
	print ("Accuracy : ",accuracy)
	
	#for graphs
	"""sec = [0,distribution_list[0][0],distribution_list[1][0],distribution_list[2][0],distribution_list[3][0],distribution_list[4][0],distribution_list[5][0]]
	fir = [0,distribution_list[0][0],distribution_list[0][1],distribution_list[0][2],distribution_list[0][3],distribution_list[0][4],distribution_list[0][5]]
	goals = [0,1,2,3,4,5,6]
	plt.plot(goals, fir,marker='*', c='r', label = 'Arsenal')
	plt.plot(goals, sec,marker='*', c='b', label = 'Aston Villa')
	#plt.plot(abs_res,column_away,linestyle='None',marker='*', c='y', label = 'Predicted Outcome')
	plt.title('Probabilities of Arsenal and Aston Villa')
	plt.ylabel('Probabilities')
	plt.xlabel('Goals')
	plt.legend()
	plt.show()
	"""
	
if __name__ == "__main__":
	main()