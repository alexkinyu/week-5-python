def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)  # Calculate the discount amount
        final_price = price - discount_amount  # Subtract discount from the original price
        return final_price
    else:
        return price  # Return the original price if discount is less than 20%

# Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Call the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Print the final price
print(f"The final price is: ${final_price:.2f}")
