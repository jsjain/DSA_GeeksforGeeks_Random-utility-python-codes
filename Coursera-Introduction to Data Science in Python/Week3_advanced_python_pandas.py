import pandas as pd
import numpy as np


# Question 1
def energy():
    energy = pd.read_excel('Energy Indicators.xls')
    energy.drop(energy.columns[[0, 1]], axis=1, inplace=True)
    energy.columns = [
        'Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'
    ]
    energy = (energy.dropna().drop(energy.index[7]).reset_index(drop=True))
    energy['Country'] = (energy['Country'].str.replace(
        '\d+|\s+\(.*', '').replace({
            'United States of America':
            'United States',
            "Republic of Korea":
            "South Korea",
            "United Kingdom of Great Britain and Northern Ireland":
            "United Kingdom",
            "China, Hong Kong Special Administrative Region":
            "Hong Kong"
        }))
    energy = energy.replace('...', np.nan)
    energy['Energy Supply'] = energy['Energy Supply'] * 1000000
    return energy


def gdp():
    gdp = pd.read_csv('world_bank.csv', skiprows=[0, 1, 2], header=1)
    gdp = gdp[[
        'Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
        '2013', '2014', '2015'
    ]]
    gdp.columns = [[
        'Country', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
        '2013', '2014', '2015'
    ]]
    gdp['Country'] = gdp['Country'].replace({
        "Korea, Rep.": "South Korea",
        "Iran, Islamic Rep.": "Iran",
        "Hong Kong SAR, China": "Hong Kong"
    })
    return gdp


def scimEn():
    ScimEm = pd.read_excel('scimagojr-3.xlsx')
    return ScimEm


def answer_one():
    e = energy()
    g = gdp()
    s = scimEn()
    merged = pd.merge(e, g, on='Country')
    merged = pd.merge(merged, s, on='Country')
    top15 = merged[merged['Rank'] < 16].set_index('Country')
    return top15


# Question 2
def answer_two():
    g = gdp()
    e = energy()
    s = scimEn()
    union = pd.merge(
        pd.merge(e, g, on='Country', how='outer'),
        s,
        on='Country',
        how='outer')
    intersect = pd.merge(pd.merge(e, g, on='Country'), s, on='Country')
    return len(union) - len(intersect)


# Question 3
def answer_three():
    Top15 = answer_one()
    years = [
        '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
        '2015'
    ]
    return (Top15[years].mean(axis=1)
            ).sort_values(ascending=False).rename('avgGDP')


# Question 4
def answer_four():
    Top15 = answer_one()
    Top15['avgGDP'] = answer_three()
    sortedTop15 = Top15.sort_values('avgGDP', ascending=False)
    return sortedTop15.iloc[5]['2015'] - sortedTop15.iloc[5]['2006']


# Question 5
def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean()


# Question 6
def answer_six():
    Top15 = answer_one()
    name = Top15['% Renewable'].argmax()
    maxRenewable = Top15.loc[name]
    return (name, maxRenewable['% Renewable'])

# Question 7
def answer_seven():
    Top15 = answer_one()
    Top15['selfToTotal'] = Top15['Self-citations'] / Top15['Citations']
    ct = Top15.sort_values(by='selfToTotal', ascending=False).iloc[0]
    return ct.name, ct['selfToTotal']

# Question 8
def answer_eight():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply'] / Top15[
        'Energy Supply per Capita']
    return Top15.sort_values(by='Population', ascending=False).iloc[2].name

# Question 9
def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    return Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'] )

def plot9():
    import matplotlib as plt
    %matplotlib inline
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])

# Question 10
def answer_ten():
    Top15 = answer_one()
    mid = Top15['% Renewable'].median()
    Top15['HighRenew'] = Top15['% Renewable']>=mid
    Top15['HighRenew'] = Top15['HighRenew'].apply(lambda x:1 if x else 0)
    Top15.sort_values(by='Rank', inplace=True)
    return Top15['HighRenew']

# Question 11
def answer_eleven():
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15 = answer_one()
    groups = pd.DataFrame(columns = ['size', 'sum', 'mean', 'std'])
    Top15['Estimate Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    for group, frame in Top15.groupby(by=ContinentDict):
            groups.loc[group] = [len(frame), frame['Estimate Population'].sum(),frame['Estimate Population'].mean(),frame['Estimate Population'].std()]
    return groups

# Question 12
def answer_twelve():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15 = Top15.reset_index()
    Top15['cut'] = pd.cut(Top15['% Renewable'], bins=5)
    Top15['continent'] = [ContinentDict[country] for country in Top15['Country']]
    return Top15.groupby([ 'continent', 'cut']).size()
# Question 13
def answer_thirteen():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita'].astype(float)
    return Top15['PopEst'].apply(lambda x: '{0:,}'.format(x))

# Optional Question
def plot_optional():
    import matplotlib as plt
    %matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")