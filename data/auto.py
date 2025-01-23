import pandas as pd
import numpy as np
import os

body = open('README.md', 'w', encoding='utf-8')

AI = ['IJCAI', 'KDD', 'CIKM', 'AAAI', 'WWW']
ML = ['ICML', 'NeurIPS', 'ICLR']
Ro = ['IROS', 'ICRA']

confs = {}

for conf in AI:
    confs[conf] = pd.read_csv('./conference/{:s}.csv'.format(conf)).set_index('Year')
for conf in ML:
    confs[conf] = pd.read_csv('./conference/{:s}.csv'.format(conf)).set_index('Year')
for conf in Ro:
    confs[conf] = pd.read_csv('./conference/{:s}.csv'.format(conf)).set_index('Year')

all_conf = pd.read_csv('conference.csv')

def newLine(com = ''):
    body.write('{:s}\n'.format(str(com)))

# Conferences' accepted paper lists

newLine('# Conferences\' accepted paper lists\n')
newLine('❗ 建议使用 [dblp](https://dblp.uni-trier.de/) 和 [Aminer](https://www.aminer.cn/conf)查询。\n')
newLine('❗ It is highly recommended to utilize the [dblp](https://dblp.uni-trier.de/) and [Aminer](https://www.aminer.cn/conf)(in Chinese) to search.\n')

newLine('# Quick Links')
years = np.arange(2025, 2019, -1)

qc_hedaer1 = '| Conference | Submission | Notification | {:d} | {:d} | {:d} | {:d} | {:d} |'.format(years[0], years[1], years[2], years[3], years[4])
qc_hedaer2 = '| ---------- | ---------- | ------------ | ---- | ---- | ---- | ---- | ---- |'
newLine(qc_hedaer1)
newLine(qc_hedaer2)


for conf in AI:
    row = all_conf[all_conf['Conference'] == conf]
    body.write('| ')
    body.write('[{:s}](#{:s})'.format(conf, conf))
    body.write(' | ')
    body.write('~{:s}'.format(row['Submission'].values[0]))
    body.write(' | ')
    body.write('~{:s}'.format(row['Notification'].values[0]))
    body.write(' | ')
    print(conf)
    for year in years:
        if year in confs[conf].index:
            if confs[conf]['Link'].isnull()[year]:
                body.write(' ')
            else:
                body.write('[🔗]({:s})'.format(str(confs[conf].loc[year]['Link'])))
        else:
            body.write(' ')
        body.write(' | ')
    body.write('\n')

for i in range(9):
    body.write('| ')
body.write('\n')

for conf in ML:
    row = all_conf[all_conf['Conference'] == conf]
    body.write('| ')
    body.write('[{:s}](#{:s})'.format(conf, conf))
    body.write(' | ')
    body.write('~{:s}'.format(row['Submission'].values[0]))
    body.write(' | ')
    body.write('~{:s}'.format(row['Notification'].values[0]))
    body.write(' | ')
    print(conf)
    for year in years:
        if year in confs[conf].index:
            if confs[conf]['Link'].isnull()[year]:
                body.write(' ')
            else:
                body.write('[🔗]({:s})'.format(str(confs[conf].loc[year]['Link'])))
        else:
            body.write(' ')
        body.write(' | ')
    body.write('\n')

for i in range(9):
    body.write('| ')
body.write('\n')

for conf in Ro:
    row = all_conf[all_conf['Conference'] == conf]
    body.write('| ')
    body.write('[{:s}](#{:s})'.format(conf, conf))
    body.write(' | ')
    body.write('~{:s}'.format(row['Submission'].values[0]))
    body.write(' | ')
    body.write('~{:s}'.format(row['Notification'].values[0]))
    body.write(' | ')
    print(conf)
    for year in years:
        if year in confs[conf].index:
            if confs[conf]['Link'].isnull()[year]:
                body.write(' ')
            else:
                body.write('[🔗]({:s})'.format(str(confs[conf].loc[year]['Link'])))
        else:
            body.write(' ')
        body.write(' | ')
    body.write('\n')

newLine()
newLine()
newLine()


def check_website(web):
    if web == '':
        return ' '
    return '[🏠 website]({:s})'.format(web)

def check_link(link):
    if link == '':
        return ' '
    return '[🔗 link]({:s})'.format(link)


def make_conf_header():
    conf_header1 = '| Year | Official Website |  Paper List | Deadline | Notification |'
    newLine(conf_header1)
    conf_header2 = '| ---------- | ---------- | ----------- | ---------- | ---------- |'
    newLine(conf_header2)

def make_conf_table(conf):
    test = conf.iloc[::-1]
    test.fillna('', inplace=True)
    Year = test.index.values
    Submission = test['Submission'].values
    Notification = test['Notification'].values
    Link = [check_link(sub) for sub in test['Link'].values]
    Web = [check_website(sub) for sub in test['Web'].values]
    for i in range(len(Year)):
        body.write('| ')
        body.write(str(Year[i]))
        body.write('| ')
        body.write(Web[i])
        body.write('| ')
        body.write(Link[i])
        body.write('| ')
        body.write(Submission[i])
        body.write('| ')
        body.write(Notification[i])
        body.write('|')
        body.write('\n')
    newLine()
    newLine()
    newLine()

for conf in AI:
    newLine('## {:s}'.format(conf))
    extra = all_conf['Other'].isnull()
    if ~extra[ all_conf[all_conf['Conference'] == conf].index[0] ]:
        newLine(all_conf['Other'].values[ all_conf[all_conf['Conference'] == conf].index[0]])
    make_conf_header()
    make_conf_table(confs[conf])
    
for conf in ML:
    newLine('## {:s}'.format(conf))
    extra = all_conf['Other'].isnull()
    if ~extra[ all_conf[all_conf['Conference'] == conf].index[0] ]:
        newLine(all_conf['Other'].values[ all_conf[all_conf['Conference'] == conf].index[0]])
    make_conf_header()
    make_conf_table(confs[conf])

    
for conf in Ro:
    newLine('## {:s}'.format(conf))
    extra = all_conf['Other'].isnull()
    if ~extra[ all_conf[all_conf['Conference'] == conf].index[0] ]:
        newLine(all_conf['Other'].values[ all_conf[all_conf['Conference'] == conf].index[0]])
    make_conf_header()
    make_conf_table(confs[conf])



body.close()
