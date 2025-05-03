from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        card_number = request.form.get('card_number')
        expiry = request.form.get('expiry')
        cvv = request.form.get('cvv')

        if not card_number or not expiry or not cvv:
            flash("Please fill out all payment fields.")
            return redirect(url_for('payment'))

        # Placeholder: Here you would process payment logic
        flash("Payment processed successfully!")
        return redirect(url_for('home'))

    return render_template('payment.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash("All contact fields are required.")
            return redirect(url_for('contact'))

        # Placeholder: Here you could store message or send email
        flash("Thank you for contacting us!")
        return redirect(url_for('home'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
