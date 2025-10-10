rwp_examples = dict(
    x1=dict(Alt='Y', Bar='N', Fri='N', Hun='Y', Pat='S', Price='$$$', Rain='N', Res='Y', Type='F', Est='0-10', ans='Y'),
    x2=dict(Alt='Y', Bar='N', Fri='N', Hun='Y', Pat='F', Price='$', Rain='N', Res='N', Type='T', Est='30-60', ans='N'),
    x3=dict(Alt='N', Bar='Y', Fri='N', Hun='N', Pat='S', Price='$', Rain='N', Res='N', Type='B', Est='0-10', ans='Y'),
    x4=dict(Alt='Y', Bar='N', Fri='Y', Hun='Y', Pat='F', Price='$', Rain='Y', Res='N', Type='T', Est='10-30', ans='Y'),
    x5=dict(Alt='Y', Bar='N', Fri='Y', Hun='N', Pat='F', Price='$$$', Rain='N', Res='Y', Type='F', Est='>60', ans='N'),
    x6=dict(Alt='N', Bar='Y', Fri='N', Hun='Y', Pat='S', Price='$$', Rain='Y', Res='Y', Type='I', Est='0-10', ans='Y'),
    x7=dict(Alt='N', Bar='Y', Fri='N', Hun='N', Pat='N', Price='$', Rain='Y', Res='N', Type='B', Est='0-10', ans='N'),
    x8=dict(Alt='N', Bar='N', Fri='N', Hun='Y', Pat='S', Price='$$', Rain='Y', Res='Y', Type='T', Est='0-10', ans='Y'),
    x9=dict(Alt='N', Bar='Y', Fri='Y', Hun='N', Pat='F', Price='$', Rain='Y', Res='N', Type='B', Est='>60', ans='N'),
    x10=dict(Alt='Y', Bar='Y', Fri='Y', Hun='Y', Pat='F', Price='$$$', Rain='N', Res='Y', Type='I', Est='10-30', ans='N'),
    x11=dict(Alt='N', Bar='N', Fri='N', Hun='N', Pat='N', Price='$', Rain='N', Res='N', Type='T', Est='0-10', ans='N'),
    x12=dict(Alt='Y', Bar='Y', Fri='Y', Hun='Y', Pat='F', Price='$', Rain='N', Res='N', Type='B', Est='0-10', ans='Y')
)

total_exp = len(rwp_examples)

def tot(attribute, value):
    count = 0
    for val in rwp_examples.values():
        if val[attribute] == value:
            count += 1
    return count

def getProbab(attribute, attribval, ansval):
    count = 0
    for val in rwp_examples.values():
        if val[attribute] == attribval and val['ans'] == ansval:
            count += 1
    return count / tot('ans', ansval)

def main():
    PAnsYes = tot('ans', 'Y') / total_exp
    PAnsNo = tot('ans', 'N') / total_exp
    
    print('Probability for will wait if there is an Alternate Restaurant Nearby:')
    print('Yes: Will Wait', (getProbab('Alt', 'Y', 'Y') * PAnsYes / (tot('Alt','Y')/total_exp)) * 100, '%')
    print('No: Will Wait', (getProbab('Alt', 'Y', 'N') * PAnsNo / (tot('Alt','Y')/total_exp)) * 100, '%')
    
    print('Probability for will wait if Estimated Wait time is 0-10 minutes:')
    print('Yes: Will Wait', (getProbab('Est','0-10','Y') * PAnsYes / (tot('Est','0-10')/total_exp)) * 100, '%')
    print('No: Will Wait', (getProbab('Est','0-10','N') * PAnsNo / (tot('Est','0-10')/total_exp)) * 100, '%')
    
    print('Probability for will wait if Estimated Wait time is 10-30 minutes:')
    print('Yes: Will Wait', (getProbab('Est','10-30','Y') * PAnsYes / (tot('Est','10-30')/total_exp)) * 100, '%')
    print('No: Will Wait', (getProbab('Est','10-30','N') * PAnsNo / (tot('Est','10-30')/total_exp)) * 100, '%')

    print('Probability for Will Wait if the Estimated Wait Time is 30-60 mins:')
    print('Yes:', (getProbab('Est','30-60','Y')*PAnsYes/(tot('Est','30-60')/total_exp))*100, '%')
    print('No:', (getProbab('Est','30-60','N')*PAnsNo/(tot('Est','30-60')/total_exp))*100, '%')

    print('Probability for Will Wait if the Estimated Wait Time is >60 mins:')
    print('Yes:', (getProbab('Est','>60','Y')*PAnsYes/(tot('Est','>60')/total_exp))*100, '%')
    print('No:', (getProbab('Est','>60','N')*PAnsNo/(tot('Est','>60')/total_exp))*100, '%')

main()
