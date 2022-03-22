import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df =pd.read_csv('adult_data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts().rename_axis('Race').reset_index(name ='Population')

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male'].age.mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = len(df[df['education'] == 'Bachelors'])/len(df)*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = ['Bachelors','Masters','Doctorate']
    all_edu = list(df['education'].unique())
    lower_education = all_edu
    for item in higher_education:
      lower_education.remove(item)
    
    lower_education

    # percentage with salary >50K
    adv_ed =  df.loc[df['education'].isin(higher_education)]
  
    adv50k = adv_ed[adv_ed['salary'] == '>50K']
    higher_education_rich = 100*(len(adv50k)/len(adv_ed))

    edu = df.loc[df['education'].isin(lower_education)]
    edu50k = edu[edu['salary'] == '>50K']
    lower_education_rich = 100*(len(edu50k)/len(edu))

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    wrks1 = df[df['hours-per-week'] == df['hours-per-week'].min()]
    
    num_min_workers = len(wrks1)

    rich_percentage = (len(wrks1[wrks1['salary'] == '>50K'])/len(wrks1))*100

    # What country has the highest percentage of people that earn >50K?
    high_earn = df[df['salary'] == '>50K']['native-country'].value_counts().rename_axis('Country').reset_index(name ='Population')
    high_earn['Percentage'] = (high_earn['Population']/high_earn['Population'].sum())*100
    highest_earning  =  high_earn[high_earn['Percentage'] == high_earn['Percentage'].max()]
    
    
    highest_earning_country = highest_earning.iloc[0]['Country']
    highest_earning_country_percentage = highest_earning.iloc[0]['Percentage']

    # Identify the most popular occupation for those who earn >50K in India.
    cond1=(adult['native-country'] == 'India')
    cond2=  (adult['salary'] == '>50K')

    india50k =adult[cond1 & cond2 ]['occupation'].value_counts().to_frame(name='Population')
 
    top_IN_occupation = india50k[india50k['Population'] == india50k['Population'].max()].reset_index().iloc[0]['index']

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
