def to_currency(amount):
    formatted_amount = "$" + format(amount,",.2f")
    return formatted_amount


def convert_to_monthly_values(yearly_rate, years):
    monthly_rate = yearly_rate /12 /100
    months = years * 12
    return monthly_rate, months