import pandas as pd
import time
import os


def clear_screen():
    """Clear the console screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50 + "\n")


def load_data():
    """Load user data from CSV file."""
    try:
        return pd.read_csv('data.csv')
    except FileNotFoundError:
        print("⚠️  Data file not found. Creating a new one...")
        df = pd.DataFrame(columns=['Name', 'Day', 'water', 'sleep', 'exercise', 'study'])
        df.to_csv('data.csv', index=False)
        return df


def find_user(username, dataframe):
    """
    Search for a user in the database.

    Returns:
        int: Index of user if found, -1 otherwise
    """
    users = dataframe['Name'].tolist()
    for index, user in enumerate(users):
        if username == user:
            return index
    return -1


def register_user(username, dataframe):
    """Register a new user in the system."""
    print(f"\n👋 Hello {username.title()}! You're not in our system yet.")
    response = input("Would you like to register? (yes/no): ").strip().lower()

    if response == 'yes':
        new_user = {
            'Name': username,
            'Day': 0,
            'water': 0,
            'sleep': 0,
            'exercise': 0,
            'study': 0
        }
        dataframe = dataframe._append(new_user, ignore_index=True)
        dataframe.to_csv('data.csv', index=False)
        print("\n✅ Registration successful! Welcome aboard!")
        return find_user(username, dataframe)
    else:
        print("\n👋 No problem! Come back when you're ready to start your health journey.")
        return -1


def get_user_row(username, dataframe):
    """Get user row index, offering registration if user doesn't exist."""
    user_index = find_user(username, dataframe)

    if user_index >= 0:
        print(f"\n✅ Welcome back, {username.title()}!")
        return user_index
    else:
        return register_user(username, dataframe)


def calculate_average(old_value, new_value, days_count):
    """
    Calculate running average for health metrics.

    For new users (days_count = 0), returns the new value.
    For existing users, returns the average of old and new values.
    """
    if days_count == 0:
        return new_value
    else:
        return (old_value + new_value) / 2


def validate_goals(water, sleep, exercise, study):
    """Validate that user goals are realistic."""
    total_time = sleep + (exercise / 60) + study

    if total_time > 19:
        print("\n⚠️  Oops! Your daily activities add up to more than 19 hours.")
        print("Remember to leave time for meals, breaks, and other activities!")
        return False

    if water > 10:
        print("\n⚠️  That's quite a lot of water! Typical daily intake is 2-4 liters.")
        print("Please enter a more realistic goal.")
        return False

    return True


def set_daily_routine(username, user_index, dataframe):
    """Guide user through setting their daily health goals."""
    print_header("Daily Routine Planner")
    print("Let's set up your health goals for today! 🎯\n")

    # Get user inputs with helpful prompts
    print("💧 Water Intake Goal")
    water_goal = float(input("   How many liters do you want to drink today? "))

    print("\n😴 Sleep Goal")
    sleep_goal = float(input("   How many hours of sleep are you aiming for? "))

    print("\n🏃 Exercise Goal")
    exercise_goal = float(input("   How many hours of exercise today? "))

    print("\n📚 Study Goal")
    study_goal = float(input("   How many hours of study time today? "))

    # Validate the goals
    if not validate_goals(water_goal, sleep_goal, exercise_goal, study_goal):
        print("\nLet's try again with more realistic goals!\n")
        return set_daily_routine(username, user_index, dataframe)

    # Retrieve current averages
    current_water = dataframe.iloc[user_index, dataframe.columns.get_loc('water')]
    current_sleep = dataframe.iloc[user_index, dataframe.columns.get_loc('sleep')]
    current_exercise = dataframe.iloc[user_index, dataframe.columns.get_loc('exercise')]
    current_study = dataframe.iloc[user_index, dataframe.columns.get_loc('study')]
    days_tracked = dataframe.iloc[user_index, dataframe.columns.get_loc('Day')]

    # Calculate new averages
    dataframe.iloc[user_index, dataframe.columns.get_loc('water')] = \
        calculate_average(current_water, water_goal, days_tracked)
    dataframe.iloc[user_index, dataframe.columns.get_loc('sleep')] = \
        calculate_average(current_sleep, sleep_goal, days_tracked)
    dataframe.iloc[user_index, dataframe.columns.get_loc('exercise')] = \
        calculate_average(current_exercise, exercise_goal, days_tracked)
    dataframe.iloc[user_index, dataframe.columns.get_loc('study')] = \
        calculate_average(current_study, study_goal, days_tracked)
    dataframe.iloc[user_index, dataframe.columns.get_loc('Day')] = days_tracked + 1

    # Save to CSV
    dataframe.to_csv('data.csv', index=False)

    # Display results
    print("\n" + "=" * 50)
    print(f"📊 Your Average Goals After {days_tracked + 1} Day(s)")
    print("=" * 50)
    print(dataframe[dataframe['Name'] == username].to_string(index=False))
    print("\n🎉 Great job tracking your progress!\n")


def focus_timer(minutes):
    """
    Run a countdown timer for focus sessions.

    Args:
        minutes: Duration in minutes
    """
    time.sleep(1)
    seconds = 0

    while True:
        print(f"⏱️  {minutes:02d}:{seconds:02d}", end="\r", flush=True)

        if seconds != 0:
            seconds -= 1
        elif minutes != 0:
            minutes -= 1
            seconds = 59
        else:
            print(f"⏱️  00:00")
            print("\n🎉 TIME'S UP! Great work!\n")
            break

        time.sleep(1)


def run_focus_session():
    """Run a Pomodoro-style focus timer session."""
    print_header("Focus Timer")
    print("Stay focused and productive! ⏰\n")

    focus_minutes = int(input("How many minutes do you want to focus? "))
    break_minutes = int(input("How many minutes for breaks? "))
    rounds = int(input("How many rounds do you want to complete? "))

    print("\n✨ Starting your focus session in 3 seconds...\n")
    time.sleep(3)

    for round_num in range(1, rounds + 1):
        print(f"\n🔥 Round {round_num} of {rounds} - Let's focus!")
        focus_timer(focus_minutes)

        if break_minutes > 0 and round_num < rounds:
            print("☕ Break time! Relax for a bit...")
            time.sleep(3)
            focus_timer(break_minutes)

    print("\n🏆 All rounds complete! You crushed it today!\n")


def main():
    """Main program flow."""
    clear_screen()
    print_header("🌟 Healthy Life Tracker 🌟")

    # Load data
    data = load_data()

    # Get username
    user_name = input("What's your name? ").strip().lower()

    # Check if user exists or register
    user_row_index = get_user_row(user_name, data)

    if user_row_index >= 0:
        # Reload data after potential registration
        data = load_data()

        # Show menu
        print("\nWhat would you like to do today?\n")
        print("  1️⃣  Set Daily Routine")
        print("  2️⃣  Start Focus Timer")

        choice = input("\nEnter your choice (1 or 2): ").strip()

        if choice == '1':
            set_daily_routine(user_name, user_row_index, data)
        elif choice == '2':
            run_focus_session()
        else:
            print("\n⚠️  Invalid choice. Please run the program again and select 1 or 2.")

    print("\n👋 Thanks for using Healthy Life Tracker! Stay healthy!\n")


if __name__ == "__main__":
    main()
