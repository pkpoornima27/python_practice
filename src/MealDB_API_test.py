# #https://www.themealdb.com/api.php
# #https://www.themealdb.com/api/json/v1/1/filter.php?a=Indian
# #https://www.themealdb.com/api/json/v1/1/lookup.php?i=52965

import requests

# Step 1: Get all Indian meals
url = 'https://www.themealdb.com/api/json/v1/1/filter.php?a=Indian'
response = requests.get(url)
print("Main API Status:", response.status_code)

if response.status_code == 200:
    meals = response.json()["meals"]

    for meal in meals:
        meal_id = meal['idMeal']
        print("\n")
        print(f'meal id: {meal_id}')

        # Step 2: Lookup full meal details
        details_url = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}'
        response2 = requests.get(details_url)


        if response2.status_code == 200:
            idMeal = response2.json()['meals'][0]['idMeal']
            print(f'idMeal: {idMeal}')
            strMeal = response2.json()['meals'][0]['strMeal']
            print(f'strMeal: {strMeal}')
            strCategory = response2.json()['meals'][0]['strCategory']
            print(f'strCategory: {strCategory}')
            meal_instructions = response2.json()['meals'][0]['strInstructions']
            print(f'Meal Instructions: {meal_instructions}')
            strMealThumb = response2.json()['meals'][0]['strMealThumb']
            print(f"strMealThumb: {strMealThumb}")
            strYoutube = response2.json()['meals'][0]['strYoutube']
            print(f"strYoutube: {strYoutube}")



        else:
            print("Error fetching details for meal ID:", meal_id)
else:
    print("Failed to fetch meals list.")
