while True:
    try:
        original_servings = float(input("Enter the number of servings the recipe is originally for: "))
        desired_servings = float(input("Enter the number of servings you wish to make: "))
        break  
    except ValueError:
        print("Invalid input! Please enter valid numbers.")


try:
    adjustment = desired_servings / original_servings
except ZeroDivisionError:
    print("Error: Original servings cannot be zero.")

except Exception as e:
    print("An error occurred during quantity calculation:", e)
    adjustment_factor = None

try:
    if adjustment is not None:
        print("Adjusted quantities: "+ str(adjustment))
        pass  
except Exception as e:
    print("An error occurred during serving adjustment:", e)
finally:
    print("Enjoy your cooking!")