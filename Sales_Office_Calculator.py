from Import_JSON import fetch_json
from Import_JSON import extract_data


def calculate(product, quantity, bonus, cog, quality, terms, wages):
    print(f'        --Terms for {product}--')

    y = (bonus * quality) / 100
    print(f'Bonus percentage(%)     : {"{:.4f}".format(y)}')

    total_bonus = int(quantity * (terms * y))
    print(f'Total bonus             : {total_bonus}')

    total_cog = quantity * cog
    print(f'Total COGs              : {total_cog}')

    revenue = int((quantity * terms) + total_bonus)
    print(f'Revenue                 : {revenue}')

    net_profit = int(revenue - (total_cog + wages))
    print(f'Net profit              : {net_profit}')


print("Sales Office Calculator")

so1_url = "https://www.simcompanies.com/api/v2/companies/buildings/37000395/sales-orders/"
so1_data = fetch_json(so1_url)

print(so1_data)

calculate('SOR', 2, 2.9, 90000, 8, 100000, 30000)
