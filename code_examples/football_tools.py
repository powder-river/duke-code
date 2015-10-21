import pandas as pd
import numpy as np
from clean_data import *
import re


#filter info,in future i want a source but for now i must hard code
high_scoring_teams = ['NE','PHI', 'NYG', 'GB']
bad_rush_d = ['TEN','GB','MIN','CLE','SD','CHI']
bad_pass_d = ['NO','MIA','KC','HOU','SF','JAC']
target_thresh = 9
touches_thresh = 15
pass_yd_thresh = 0


# def filter_by_targets(df):
#     df = df[(df.Tgt >= target_thresh)]
#     return df

def filter_by_value(df):
    df = df[(df.value < 425)]
    return df


def filter_by_vegas(df):
    df = df[df['Team'].isin(high_scoring_teams)]
    return df


def bad_rush(df):
    df = df[df['Opponent'].isin(bad_rush_d)]
    return df


def bad_pass(df):
    df = df[df['Opponent'].isin(bad_pass_d)]
    return df

def tgt_per_g(df):
    df = df[(df.Tgt_PG >= target_thresh)]
    return df

def filter_touches(df):
    df = df[((df.Touch_Game.astype(float)) >= touches_thresh)]
    return df


def run_filters(df,value=False,vegas=False,rush_d=False,pass_d=False,touches=False,targets=False):
    if value == True:
        df = filter_by_value(df)
    if vegas == True:
        df = filter_by_vegas(df)
    if rush_d == True:
        df = bad_rush(df)
    if pass_d == True:
        df = bad_pass(df)
    if touches == True:
        df = filter_touches(df)
    if targets == True:
        df = tgt_per_g(df)

    return df
