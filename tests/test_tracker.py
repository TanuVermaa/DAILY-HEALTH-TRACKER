import unittest
from src.tracker import FitnessTracker

class TestFitnessTracker(unittest.TestCase):

    def setUp(self):
        # Sample User: 25 y/o male, 80kg, 180cm, moderate activity (option '3')
        self.user = FitnessTracker("Test User", 25, "male", 80.0, 180.0, "3")

    def test_bmr_calculation(self):
        # Male BMR: (10*80) + (6.25*180) - (5*25) + 5 = 800 + 1125 - 125 + 5 = 1805
        self.assertEqual(self.user.calculate_bmr(), 1805)

    def test_tdee_calculation(self):
        # TDEE: 1805 * 1.55 = 2797.75
        self.assertAlmostEqual(self.user.calculate_tdee(), 2797.75, places=2)

    def test_weight_loss_plan(self):
        # Goal: Lose 5 kg over 10 weeks -> -0.5 kg/week -> -3850 kcal/week -> -550 kcal/day
        plan = self.user.generate_plan(target_weight_kg=75.0, weeks_to_goal=10)
        self.assertEqual(plan["goal"], "Weight Loss")
        self.assertEqual(plan["target_calories"], 2248)  # round(2797.75 - 550)

    def test_logging_summary(self):
        self.user.log_meal("Oatmeal", 400)
        self.user.log_workout("Running", 200)
        summary = self.user.get_daily_summary(target_calories=2000)
        
        self.assertEqual(summary["Calories Consumed"], 400)
        self.assertEqual(summary["Calories Burned"], 200)
        self.assertEqual(summary["Net Calories"], 200)
        self.assertEqual(summary["Remaining Target"], 1800)

if __name__ == "__main__":
    unittest.main()
