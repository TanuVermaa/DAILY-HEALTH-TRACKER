# Problem Statement & System Design

## 1. Problem Description
Achieving personal fitness goals requires tracking energy intake versus output. Standard calorie counting tools lack adaptive meal plans based on target timelines or fail to provide transparent mathematical models. 

This project delivers a command-line application that calculates caloric balance, designs macro-targeted meal schedules, and monitors live workouts/meals.

## 2. Theoretical Framework
* **Basal Metabolic Rate (BMR):** Calculated using the Mifflin-St Jeor equation:
  
  $$\text{BMR}_{\text{male}} = 10W + 6.25H - 5A + 5$$
  
  $$\text{BMR}_{\text{female}} = 10W + 6.25H - 5A - 161$$

  *(where $W$ is weight in kg, $H$ is height in cm, and $A$ is age in years)*

* **Total Daily Energy Expenditure (TDEE):** Derived by applying physical activity level scalars ($\alpha \in [1.2, 1.9]$) to BMR.

* **Energetic Caloric Equivalence:** Assumes $1 \text{ kg body mass} \approx 7,700 \text{ kcal}$. Daily target adjustments are determined by target weight delta ($\Delta W$) over target weeks ($t$):

  $$\text{Daily Adjustment} = \frac{\Delta W \times 7700}{7 \times t}$$
