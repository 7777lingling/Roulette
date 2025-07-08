from flask import Flask, render_template, request, redirect, url_for
import webbrowser
import threading
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

        # 處理輸入的號碼範圍
        try:
            min_number = int(min_number)
            max_number = int(max_number)
            numbers = [str(i) for i in range(min_number, max_number + 1)]
        except ValueError:
            return "請提供有效的號碼範圍"

        # 排除不要的號碼
        exclude_numbers = exclude_numbers.split(',') if exclude_numbers else []
        numbers = [n for n in numbers if n not in exclude_numbers]

        # 去重
        if remove_duplicates:
            numbers = list(set(numbers))

        # 檢查是否有有效的號碼參與抽籤
        if not numbers:
            return "沒有有效的號碼參與抽籤！"

        # 模擬轉盤選擇號碼
        result = random.choice(numbers)
        
        # 傳遞中獎號碼到結果頁面
        return redirect(url_for('result', result=result))

    return render_template('number_roulette.html')

@app.route('/result')
def result():
    result = request.args.get('result')
    return render_template('result.html', result=result)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()  # 延遲 1 秒後打開瀏覽器
    app.run(debug=True)
