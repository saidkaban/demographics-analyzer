import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_list = df["race"].unique()
    race_len = [len(df[df["race"] == race]) for race in race_list]
    race_count = pd.Series(race_len, race_list)

    # What is the average age of men?
    age_of_males = df[df["sex"] == "Male"]["age"]
    average_age_men = round(sum(age_of_males) / len(age_of_males), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df["education"] == "Bachelors"]) / len(df) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced_education = ["Bachelors", "Masters", "Doctorate"]

    higher_education = df[df["education"].isin(advanced_education)]
    lower_education = df[~df["education"].isin(advanced_education)]

    # percentage with salary >50K
    higher_education_rich = round(len(higher_education[higher_education["salary"] == ">50K"]) / len(higher_education) * 100, 1)
    lower_education_rich = round(len(lower_education[lower_education["salary"] == ">50K"]) / len(lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df["hours-per-week"])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df["hours-per-week"] == min(df["hours-per-week"])]
    
    num_min_workers = len(min_workers)

    rich_percentage = len(min_workers[min_workers["salary"] == ">50K"]) / num_min_workers * 100

    # What country has the highest percentage of people that earn >50K?
    country_list = df["native-country"].unique()
    perc_list = []
    for country in country_list:
        country_df = df[df["native-country"] == country]
        country_perc = len(country_df[country_df["salary"] == ">50K"]) / len(country_df)
        perc_list.append(country_perc * 100)

    countries_percentage = pd.Series(perc_list, index=country_list)

    highest_earning_country = countries_percentage.idxmax()
    highest_earning_country_percentage = round(max(countries_percentage), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df[df["native-country"] == "India"]
    top_IN_occupation = india_df[india_df["salary"] == ">50K"]["occupation"].value_counts().idxmax()

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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()
