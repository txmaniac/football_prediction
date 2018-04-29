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

def main():
	db = pd.read_csv('attack_defence.csv')
	column_alpha_home = db['Alpha_home']
	column_alpha_away = db['Alpha_away']
	column_beta_home = db['Beta_home']
	column_beta_away = db['Beta_away']
	column_avg_goal_away = db['Avg_goals_for_away']
	column_avg_goal_home = db['Avg_goals_for_home']
	column_team = db['Team']
	
	database = pd.read_csv('PremierLeague_Fixtures.csv')
	column_home = database['HomeTeam']
	column_away = database['AwayTeam']
	column_score_home = database['FTHG']
	column_score_away = database['FTAG']
	column_result = database['FTR']
	
	# HOME
	plt.plot(column_alpha_home, column_team, linestyle='None',marker='*', c='r', label = 'alpha value at home')
	plt.plot(column_beta_home, column_team, linestyle='None',marker='*', c='b', label = 'beta value at home')
	plt.title('Alpha and Beta home')
	plt.ylabel('Team')
	plt.xlabel('Values')
	plt.legend()
	plt.show()
	
	# AWAY
	plt.plot(column_alpha_away, column_team, linestyle='None',marker='*', c='r', label = 'alpha value away')
	plt.plot(column_beta_away, column_team, linestyle='None',marker='*', c='b', label = 'beta value away')
	plt.title('Alpha and Beta away')
	plt.ylabel('Team')
	plt.xlabel('Values')
	plt.legend()
	plt.show()
	
	# PLOT OF RESULT COMPARISON
	
	
if __name__ == "__main__":
	main()