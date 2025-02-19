def categorize_total_amount(amount):
    if amount < 20:
        return "Low"
    elif amount < 100:
        return "Medium"
    else:
        return "High"
    