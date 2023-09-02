import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.


    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("enter the name of city you want to know about it\n")
    city = city.lower()
    while city != "chicago" and city != "new york city" and city != "washington":
        print('there is no this city in our list please try again')
        city = input("enter the name of city you want to know about it\n")

    month = input(
        "would you like filter data by month ? \n if yes please write which month and if no please write ""all""\n")
    month = month.lower()

    day = input("would you like filter data by day ? \nif yes please write which day and if no please write ""all""\n")
    day = day.lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.strftime("%A")
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Augst', 'September', 'October',
                  'November', 'December']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('common_month:',common_month,"\n")


    # TO DO: display the most common day of week
    common_day=df['day'].mode()[0]
    print('common_day:',common_day,'\n')


    # TO DO: display the most common start hour
    common_hour=df['hour'].mode()[0]
    print('common_hour',common_hour,'\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    if 'Start Station' in df:
        common_start_station = df['Start Station'].mode()[0]
        print('common_start_station:', common_start_station, "\n")
    else:
        print('start station stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: display most commonly used end station
    if 'End Station' in df:
        common_end_station = df['End Station'].mode()[0]
        print('common_end_station: ', common_end_station, "\n")
    else:
        print('end station stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = (df['Start Station'] + ' ' + df['End Station']).mode()[0]
    print('common_start_end_station: ', common_start_end_station, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    if 'Trip Duration' in df:
        total_travel_time = df['Trip Duration'].sum()
        print('total_travel_time: ', total_travel_time, "\n")
        # TO DO: display mean travel time
        total_mean_time = df['Trip Duration'].mean()
        print('total_mean_time:', total_mean_time, "\n")
    else:
        print('time duration stats cannot be calculated because Gender does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df:
        user_types = df['User Type'].value_counts()
        print('user_types_counts:', user_types, '\n')
    else:
        print('User Type stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('gender_counts:', gender, '\n')
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        mini_year = df['Birth Year'].min()
        print("mini_year:", mini_year, "\n")
        maxi_year = df['Birth Year'].max()
        print("maxi_year:", maxi_year, '\n')
        common_year = df['Birth Year'].mode()[0]
        print('common_year:', common_year, '\n')
    else:
        print('Birth Year stats cannot be calculated because Gender does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    view_data = view_data.lower()
    start_loc = 0
    while view_data != 'no':
        print(df.iloc[start_loc:start_loc + 5, :])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        view_data = view_display
        if view_data == 'no':
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
