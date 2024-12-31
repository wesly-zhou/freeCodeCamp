import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # value_counts gets the occurrences of each unique value in the race column and returns a Pandas Series, with the unique
    # value as the index labels and the counts as the value.
    race_count = df['race'].value_counts()

    # Filter the data frame to only males, and then get the mean of the age column
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    average_age_men = round(average_age_men, 1)

    # Filter the data frame to only people with a Bachelor's and use len to get the number of people
    # Divide the number of people with a Bachelor's by the total number of people
    num_bachelors = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = (num_bachelors / len(df)) * 100
    percentage_bachelors = round(percentage_bachelors, 1)

    # Utilize a mask to separate higher education from lower education
    education_mask = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education = df[education_mask]
    lower_education = df[~education_mask]

    # Filter by both education and salary
    higher_education_rich = (len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich = (len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100
    lower_education_rich = round(lower_education_rich, 1)

    # Returns the min of the hours-per-week column
    min_work_hours = df['hours-per-week'].min()

    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])

    # Get the percentage of people who work the minimum number of hours and still make over 50K
    rich_percentage = (len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]) / num_min_workers) * 100

    # Utilize value_counts to get the values for each country
    # Divide the number of rich people from each country by the number of total people in the country
    rich_pop = df[df['salary'] == '>50K']
    country_percentages = (rich_pop['native-country'].value_counts() / df['native-country'].value_counts()) * 100
    highest_earning_country = country_percentages.idxmax()
    highest_earning_country_percentage = round(country_percentages.max(), 1)

    # Filter the people from India and make over 50K
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    # Select the highest index label from value_counts
    india_percentages = india_rich['occupation'].value_counts()
    top_IN_occupation = india_percentages.idxmax()

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
