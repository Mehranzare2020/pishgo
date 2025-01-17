from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_lucky_number(name):
    jammal_values = {
        'ا': 1, 'ب': 2, 'پ': 3, 'ت': 400, 'ث': 500,
        'ج': 3, 'چ': 4, 'ح': 8, 'خ': 600, 'د': 4,
        'ذ': 700, 'ر': 200, 'ز': 7, 'ژ': 8, 'س': 60,
        'ش': 300, 'ص': 90, 'ض': 800, 'ط': 9, 'ظ': 900,
        'ع': 70, 'غ': 1000, 'ف': 80, 'ق': 100, 'ک': 20,
        'گ': 3, 'ل': 30, 'م': 40, 'ن': 50, 'و': 6,
        'ه': 5, 'ی': 10
    }

    total_value = sum(jammal_values[char] for char in name if char in jammal_values)
    reduced_value = total_value
    while reduced_value > 9:
        reduced_value = sum(int(digit) for digit in str(reduced_value))

    return total_value, reduced_value

def calculate_lucky_day(reduced_value):
    days = {
        1: 'یکشنبه', 2: 'دوشنبه', 3: 'سه‌شنبه', 4: 'چهارشنبه',
        5: 'پنج‌شنبه', 6: 'جمعه', 7: 'شنبه'
    }
    return days[reduced_value if reduced_value <= 7 else reduced_value % 7]

def calculate_lucky_color(reduced_value):
    colors = {
        1: 'قرمز', 2: 'نارنجی', 3: 'زرد', 4: 'سبز',
        5: 'آبی', 6: 'نیلی', 7: 'بنفش', 8: 'صورتی', 9: 'طلایی'
    }
    return colors[reduced_value]

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            total_value, reduced_value = calculate_lucky_number(name)
            lucky_day = calculate_lucky_day(reduced_value)
            lucky_color = calculate_lucky_color(reduced_value)
            result = {
                'name': name,
                'total_value': total_value,
                'reduced_value': reduced_value,
                'lucky_day': lucky_day,
                'lucky_color': lucky_color
            }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
