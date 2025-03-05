from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store user data and recipes in memory
user_data = {}  # Dictionary to store user preferences
recipes = []  # List to store recipes

# Home Page (GET)
@app.route('/')
def home():
    return render_template('home.html')

# Preferences Page (GET + POST)
@app.route('/preferences', methods=['GET', 'POST'])
def preferences():
    if request.method == 'POST':
        user_data['diet'] = request.form.get('diet')
        user_data['cuisine'] = request.form.get('cuisine')
        user_data['meals'] = request.form.get('meals')
        return redirect(url_for('recipe_input'))
    return render_template('preferences.html')

# Recipe Input Page (GET + POST)
@app.route('/recipe_input', methods=['GET', 'POST'])
def recipe_input():
    if request.method == 'POST':
        # Get data from the form
        recipe_name = request.form.get('recipe_name')
        ingredients = request.form.get('ingredients')
        
        if recipe_name and ingredients:
            # Add the recipe to the list
            recipes.append({'name': recipe_name, 'ingredients': ingredients})
        
        # After adding the recipe, redirect to the recipe plan page
        return redirect(url_for('recipe_plan'))
    
    return render_template('recipe_input.html')

# Recipe Plan Page (GET)
@app.route('/recipe_plan')
def recipe_plan():
    return render_template('recipe_plan.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)
