import sys
from src.tracker import FitnessTracker
from src.utils import get_float_input, get_int_input

def main():
    print("=" * 50)
    print("   FITNESS TRACKER & DIET PLANNER CLI")
    print("=" * 50)

    name = input("\nEnter your name: ").strip()
    age = get_int_input("Enter your age: ")
    
    while True:
        gender = input("Enter gender (male/female): ").strip().lower()
        if gender in ["male", "female"]:
            break
        print("Invalid entry. Choose 'male' or 'female'.")

    weight = get_float_input("Enter current weight (kg): ")
    height = get_float_input("Enter height (cm): ")

    print("\nSelect Activity Level:")
    print("  1. Sedentary (little to no exercise)")
    print("  2. Lightly Active (1-3 days/week)")
    print("  3. Moderately Active (3-5 days/week)")
    print("  4. Very Active (6-7 days/week)")
    print("  5. Extra Active (intense workouts / physical job)")
    
    while True:
        activity = input("Choice (1-5): ").strip()
        if activity in ["1", "2", "3", "4", "5"]:
            break
        print("Invalid choice. Select from 1 to 5.")

    user = FitnessTracker(name, age, gender, weight, height, activity)

    print("\n" + "-" * 40)
    print("   SET YOUR GOALS")
    print("-" * 40)
    target_weight = get_float_input("Enter target weight (kg): ")
    weeks = 1 if target_weight == weight else get_int_input("Timeline (weeks to goal): ")

    plan = user.generate_plan(target_weight, weeks)

    if plan["daily_adjustment"] < -1000:
        print("\n[!] WARNING: Target pace requires >1000 kcal/day deficit. Safe pace is 0.5-1 kg/week.")

    print("\n" + "=" * 50)
    print(f"   CUSTOM PLAN FOR {user.name.upper()}")
    print("=" * 50)
    print(f"Goal Type        : {plan['goal']}")
    print(f"Daily Target     : {plan['target_calories']} kcal/day")
    print("Macro Targets    :")
    for macro, value in plan["macros"].items():
        print(f"  • {macro:<8}: {value}")

    print("\nRecommended Diet Plan:")
    for meal, details in plan["diet_plan"].items():
        print(f"  • {meal:<10}: {details}")

    while True:
        print("\n" + "-" * 40)
        print("   MAIN MENU")
        print("-" * 40)
        print("1. Log Meal")
        print("2. Log Workout")
        print("3. View Summary")
        print("4. Exit")

        choice = input("\nChoice (1-4): ").strip()

        if choice == "1":
            m_name = input("Meal description: ").strip()
            m_cals = get_int_input("Calories (kcal): ")
            user.log_meal(m_name, m_cals)
            print(f"[✓] Meal logged successfully.")

        elif choice == "2":
            w_name = input("Workout description: ").strip()
            w_cals = get_int_input("Calories burned (kcal): ")
            user.log_workout(w_name, w_cals)
            print(f"[✓] Workout logged successfully.")

        elif choice == "3":
            summary = user.get_daily_summary(plan['target_calories'])
            print("\n--- Current Progress ---")
            for key, value in summary.items():
                print(f"  • {key:<18}: {value} kcal")

        elif choice == "4":
            print(f"\nGoodbye, {user.name}!")
            sys.exit()

        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
