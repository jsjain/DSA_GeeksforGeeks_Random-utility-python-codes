import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

states = {
    'OH': 'Ohio',
    'KY': 'Kentucky',
    'AS': 'American Samoa',
    'NV': 'Nevada',
    'WY': 'Wyoming',
    'NA': 'National',
    'AL': 'Alabama',
    'MD': 'Maryland',
    'AK': 'Alaska',
    'UT': 'Utah',
    'OR': 'Oregon',
    'MT': 'Montana',
    'IL': 'Illinois',
    'TN': 'Tennessee',
    'DC': 'District of Columbia',
    'VT': 'Vermont',
    'ID': 'Idaho',
    'AR': 'Arkansas',
    'ME': 'Maine',
    'WA': 'Washington',
    'HI': 'Hawaii',
    'WI': 'Wisconsin',
    'MI': 'Michigan',
    'IN': 'Indiana',
    'NJ': 'New Jersey',
    'AZ': 'Arizona',
    'GU': 'Guam',
    'MS': 'Mississippi',
    'PR': 'Puerto Rico',
    'NC': 'North Carolina',
    'TX': 'Texas',
    'SD': 'South Dakota',
    'MP': 'Northern Mariana Islands',
    'IA': 'Iowa',
    'MO': 'Missouri',
    'CT': 'Connecticut',
    'WV': 'West Virginia',
    'SC': 'South Carolina',
    'LA': 'Louisiana',
    'KS': 'Kansas',
    'NY': 'New York',
    'NE': 'Nebraska',
    'OK': 'Oklahoma',
    'FL': 'Florida',
    'CA': 'California',
    'CO': 'Colorado',
    'PA': 'Pennsylvania',
    'DE': 'Delaware',
    'NM': 'New Mexico',
    'RI': 'Rhode Island',
    'MN': 'Minnesota',
    'VI': 'Virgin Islands',
    'NH': 'New Hampshire',
    'MA': 'Massachusetts',
    'GA': 'Georgia',
    'ND': 'North Dakota',
    'VA': 'Virginia'
}


def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    state_town = []
    state = None
    with open('university_towns.txt', 'r') as file:
        for line in file:
            thisLine = line[:-1]
            if thisLine[-6:] == '[edit]':
                state = thisLine[:-6]
                continue
            if '(' in line:
                town = thisLine[:thisLine.index('(') - 1]
                state_town.append([state, town])
            else:
                town = thisLine
            state_town.append([state, town])
    df = pd.DataFrame(state_town, columns=['State', 'RegionName'])
    return df


def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    gdplev = pd.ExcelFile('gdplev.xls')
    gdplev = gdplev.parse("Sheet1", skiprows=219)
    gdplev = gdplev[['1999q4', 9926.1]]
    gdplev.columns = ['Quarter', 'GDP']
    for i in range(2, len(gdplev)):
        if (gdplev.iloc[i - 2][1] > gdplev.iloc[i - 1][1]) and (
                gdplev.iloc[i - 1][1] > gdplev.iloc[i][1]):
            return gdplev.iloc[i - 2][0]


def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    gdplev = pd.ExcelFile('gdplev.xls')
    gdplev = gdplev.parse("Sheet1", skiprows=219)
    gdplev = gdplev[['1999q4', 9926.1]]
    gdplev.columns = ['Quarter', 'GDP']
    start = get_recession_start()
    start_index = gdplev[gdplev['Quarter'] == start].index.tolist()[0]
    gdplev = gdplev.iloc[start_index:]
    for i in range(2, len(gdplev)):
        if (gdplev.iloc[i - 2][1] < gdplev.iloc[i - 1][1]) and (
                gdplev.iloc[i - 1][1] < gdplev.iloc[i][1]):
            return gdplev.iloc[i][0]


def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    gdplev = pd.ExcelFile('gdplev.xls')
    gdplev = gdplev.parse("Sheet1", skiprows=219)
    gdplev = gdplev[['1999q4', 9926.1]]
    gdplev.columns = ['Quarter', 'GDP']
    start = get_recession_start()
    start_index = gdplev[gdplev['Quarter'] == start].index.tolist()[0]
    end = get_recession_end()
    end_index = gdplev[gdplev['Quarter'] == end].index.tolist()[0]
    gdplev = gdplev.iloc[start_index:end_index + 1]
    bottom = gdplev['GDP'].min()
    bottom_index = gdplev[gdplev['GDP'] ==
                          bottom].index.tolist()[0] - start_index
    return gdplev.iloc[bottom_index]['Quarter']


def quarterdColumns():
    years = list(range(2000, 2017))
    quarters = ['q1', 'q2', 'q3', 'q4']
    colomns = []
    for year in years:
        for quarter in quarters:
            colomns.append(str(year) + quarter)
    return colomns[:67]


def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    data = pd.read_csv('City_Zhvi_AllHomes.csv')
    data.drop(
        ['Metro', 'CountyName', 'RegionID', 'SizeRank'], axis=1, inplace=1)
    data['State'] = data['State'].map(states)
    data.set_index(['State', 'RegionName'], inplace=True)
    col = list(data.columns)
    col = col[0:45]
    data.drop(col, axis=1, inplace=1)
    qs = [
        list(data.columns)[x:x + 3]
        for x in range(0, len(list(data.columns)), 3)
    ]
    quarteredColoumns = quarterdColumns()
    for col, q in zip(quarteredColoumns, qs):
        data[col] = data[q].mean(axis=1)
    data = data[quarteredColoumns]
    return data


def price_ratio(row):
    return (row['2008q3'] - row['2009q2'] / row['2008q3'])


def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    data = convert_housing_data_to_quarters().copy()
    data = data.loc[:, '2008q3':'2009q2']
    data = data.reset_index()
    data['ratio'] = data.apply(price_ratio, axis=1)

    university_town = get_list_of_university_towns()['RegionName']
    university_town = set(university_town)

    def is_university_town(row):
        if (row['RegionName'] in university_town):
            return 1
        else:
            return 0

    data['isUni'] = data.apply(is_university_town, axis=1)

    uni_towns = data[data['isUni'] == 1].loc[:, 'ratio'].dropna()
    non_uni_towns = data[data['isUni'] == 0].loc[:, 'ratio'].dropna()

    def better():
        if (uni_towns.mean() < non_uni_towns.mean()):
            return 'university town'
        else:
            return "non-university town"

    better = better()

    p_value = list(ttest_ind(uni_towns, non_uni_towns))[1]

    if p_value < 0.01:
        differnet = True
    else:
        differnet = False
    return (differnet, p_value, better)