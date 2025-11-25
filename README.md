# 🌟 Healthy Life Tracker

A simple, user-friendly Python application to help you track your daily health goals and boost productivity with a built-in focus timer.

## 📋 Table of Contents

- #features
- #requirements
- #installation
- #usage
- #how-it-works
- #file-structure
- #contributing
- #contact

## ✨ Features

### 📊 Daily Routine Tracking
- Track multiple health metrics:
  - 💧 Water intake (liters)
  - 😴 Sleep duration (hours)
  - 🏃 Exercise time (hours)
  - 📚 Study time (hours)
- Automatic calculation of running averages
- Goal validation to ensure realistic targets
- Progress tracking over multiple days

### ⏱️ Focus Timer (Pomodoro-Style)
- Customizable focus sessions
- Configurable break times
- Multiple rounds support
- Visual countdown timer
- Perfect for studying or deep work

### 👤 User Management
- Easy user registration
- Persistent data storage
- Multiple user support
- Automatic data backup in CSV format

## 🔧 Requirements

- Python 3.6 or higher
- pandas library

## 📥 Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd healthy-life-tracker
   ```

2. **Install required dependencies**
   ```bash
   pip install pandas
   ```

3. **Run the application**
   ```bash
   python health_tracker.py
   ```

## 🚀 Usage

### First Time Setup

1. Run the program:
   ```bash
   python health_tracker.py
   ```

2. Enter your name when prompted

3. If you're a new user, choose to register when asked

4. Select your desired feature:
   - **Option 1**: Set your daily health goals
   - **Option 2**: Start a focus timer session

### Setting Daily Goals

When you select the routine option, you'll be prompted to enter:

- **Water intake goal**: How many liters you want to drink (realistic range: 2-4L)
- **Sleep goal**: Target hours of sleep (realistic range: 6-9 hours)
- **Exercise goal**: Minutes of physical activity (e.g., 30-60 minutes)
- **Study goal**: Hours of focused study time

The app will validate your goals and calculate running averages based on your history.

### Using the Focus Timer

1. Select option 2 from the main menu
2. Enter the following:
   - Focus duration (in minutes)
   - Break duration (in minutes)
   - Number of rounds to complete

The timer will guide you through focus sessions with breaks in between, perfect for the Pomodoro Technique!

## 🔍 How It Works

### Data Storage

The application stores user data in `data.csv` with the following structure:

| Name | Day | water | sleep | exercise | study |
|------|-----|-------|-------|----------|-------|
| john | 5   | 2.5   | 7.5   | 45       | 3     |

- **Name**: Username (lowercase)
- **Day**: Number of days tracked
- **water**: Average water intake in liters
- **sleep**: Average sleep duration in hours
- **exercise**: Average exercise time in minutes
- **study**: Average study time in hours

### Average Calculation

The app uses a running average formula:
- For new users (Day 0): Average = Today's goal
- For existing users: Average = (Previous Average + Today's Goal) / 2

This helps smooth out variations and shows your overall trends.

### Goal Validation

The app ensures your goals are realistic:
- Total daily time activities (sleep + exercise + study) must not exceed 19 hours
- Water intake should not exceed 10 liters
- This leaves time for meals, breaks, and other daily activities

## 📁 File Structure

```
healthy-life-tracker/
│
├── health_tracker.py    # Main application file
├── data.csv             # User data storage (auto-generated)
└── README.md            # This file
```

## 🎯 Example Session

```
==================================================
  🌟 Healthy Life Tracker 🌟
==================================================

What's your name? john

✅ Welcome back, John!

What would you like to do today?

  1️⃣  Set Daily Routine
  2️⃣  Start Focus Timer

Enter your choice (1 or 2): 1

==================================================
  Daily Routine Planner
==================================================
Let's set up your health goals for today! 🎯

💧 Water Intake Goal
   How many liters do you want to drink today? 3

😴 Sleep Goal
   How many hours of sleep are you aiming for? 8

🏃 Exercise Goal
   How many minutes of exercise today? 30

📚 Study Goal
   How many hours of study time today? 4

==================================================
📊 Your Average Goals After 6 Day(s)
==================================================
  Name  Day  water  sleep  exercise  study
  john    6   2.75    7.5      37.5    3.5

🎉 Great job tracking your progress!
```

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- Report bugs
- Suggest new features
- Improve documentation
- Submit pull requests

## 📝 Tips for Best Results

1. **Be Consistent**: Track your goals daily for accurate averages
2. **Be Realistic**: Set achievable goals that fit your lifestyle
3. **Review Progress**: Check your averages regularly to see improvements
4. **Use Focus Timer**: Combine with routine tracking for maximum productivity
5. **Stay Hydrated**: Aim for 2-3 liters of water daily

## ⚠️ Troubleshooting

**Issue**: `data.csv not found`
- **Solution**: The app will automatically create this file on first run

**Issue**: Goals rejected as unrealistic
- **Solution**: Ensure your sleep + exercise/60 + study ≤ 19 hours and water ≤ 10 liters

**Issue**: User not found after registration
- **Solution**: Check that `data.csv` has write permissions

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

**Stay healthy, stay focused! 🌟**
