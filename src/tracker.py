class FitnessTracker:
    """Manages profile calculations, energy expenditure, and nutrition logging."""
    
    def __init__(self, name: str, age: int, gender: str, weight_kg: float, height_cm: float, activity_level: str):
        self.name = name
        self.age = age
        self.gender = gender.lower()
        self.weight = weight_kg
        self.height = height_cm
        self.activity_level = str(activity_level).lower()
        self.logged_meals = []
        self.logged_workouts = []

    def calculate_bmr(self) -> float:
        """Calculates Basal Metabolic Rate using the Mifflin-St Jeor equation."""
        if self.gender == "male":
            return (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        return (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161

    def calculate_tdee(self) -> float:
        """Calculates Total Daily Energy Expenditure based on activity multiplier."""
        multipliers = {
            "1": 1.2,      # Sedentary
            "2": 1.375,    # Light activity
            "3": 1.55,     # Moderate activity
            "4": 1.725,    # Active
            "5": 1.9       # Very active
        }
        return self.calculate_bmr() * multipliers.get(self.activity_level, 1.2)

    def generate_plan(self, target_weight_kg: float, weeks_to_goal: int) -> dict:
        """Computes calorie targets, macronutrient split, and sample diet plan."""
        weight_diff = target_weight_kg - self.weight
        
        if weight_diff == 0:
            goal_type = "Maintenance"
            daily_adjustment = 0
        else:
            total_calorie_change = weight_diff * 7700  # ~7700 kcal / kg body mass
            daily_adjustment = total_calorie_change / (weeks_to_goal * 7)

        target_calories = max(1200, round(self.calculate_tdee() + daily_adjustment))
        
        # Macros: 40% Carbs, 30% Protein, 30% Fat
        protein_g = round((target_calories * 0.30) / 4)
        carbs_g = round((target_calories * 0.40) / 4)
        fats_g = round((target_calories * 0.30) / 9)

        return {
            "goal": goal_type if weight_diff == 0 else ("Weight Loss" if weight_diff < 0 else "Weight Gain"),
            "target_calories": target_calories,
            "daily_adjustment": daily_adjustment,
            "macros": {"Protein": f"{protein_g}g", "Carbs": f"{carbs_g}g", "Fats": f"{fats_g}g"},
            "diet_plan": self._sample_meals(target_calories)
        }

    def _sample_meals(self, calories: int) -> dict:
        """Generates caloric diet plans."""
        if calories < 1800:
            return {
                "Breakfast": "Oatmeal with berries & 1 scoop whey protein (350 kcal)",
                "Lunch": "Grilled chicken breast salad with olive oil dressing (450 kcal)",
                "Snack": "Greek yogurt with almonds (200 kcal)",
                "Dinner": "Baked salmon with steamed broccoli & quinoa (450 kcal)"
            }
        elif calories <= 2500:
            return {
                "Breakfast": "3 scrambled eggs, whole-wheat toast & avocado (500 kcal)",
                "Lunch": "Turkey wrap with brown rice and mixed greens (650 kcal)",
                "Snack": "Apple with peanut butter & protein shake (350 kcal)",
                "Dinner": "Lean beef stir-fry with mixed veggies and Jasmine rice (650 kcal)"
            }
        return {
            "Breakfast": "4 eggs, 2 toast slices, avocado & fruit smoothie (750 kcal)",
            "Lunch": "Chicken breast with double sweet potato & asparagus (800 kcal)",
            "Snack": "Trail mix, banana & whey protein shake (500 kcal)",
            "Dinner": "Salmon fillet with double quinoa & roasted greens (750 kcal)"
        }

    def log_meal(self, meal_name: str, calories: int):
        self.logged_meals.append({"meal": meal_name, "calories": calories})

    def log_workout(self, exercise: str, calories_burned: int):
        self.logged_workouts.append({"exercise": exercise, "calories_burned": calories_burned})

    def get_daily_summary(self, target_calories: int) -> dict:
        consumed = sum(item["calories"] for item in self.logged_meals)
        burned = sum(item["calories_burned"] for item in self.logged_workouts)
        net = consumed - burned
        return {
            "Calories Consumed": consumed,
            "Calories Burned": burned,
            "Net Calories": net,
            "Remaining Target": target_calories - net
        }
