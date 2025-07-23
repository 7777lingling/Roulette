from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/custom_mode')
def custom_mode():
    return render_template('custom_mode.html')

@app.route('/number_roulette', methods=['GET', 'POST'])
def number_roulette():
    if request.method == 'POST':
        min_number = request.form.get('min_number')
        max_number = request.form.get('max_number')
        exclude_numbers = request.form.get('exclude_numbers')
        remove_duplicates = 'remove_duplicates' in request.form

        try:
            min_number = int(min_number)
            max_number = int(max_number)
            numbers = [str(i) for i in range(min_number, max_number + 1)]
        except ValueError:
            return "請提供有效的號碼範圍"

        exclude_numbers = exclude_numbers.split(',') if exclude_numbers else []
        numbers = [n for n in numbers if n not in exclude_numbers]

        if remove_duplicates:
            numbers = list(set(numbers))

        if not numbers:
            return "沒有有效的號碼參與抽籤！"

        result = random.choice(numbers)
        return redirect(url_for('result', result=result))

    return render_template('number_roulette.html')

@app.route('/result')
def result():
    result = request.args.get('result')
    return render_template('result.html', result=result)

# ✅ 注意：不要寫 app.run()，wfastcgi 會自動載入 app
