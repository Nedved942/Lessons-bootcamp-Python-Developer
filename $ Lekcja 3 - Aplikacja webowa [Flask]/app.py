from flask import Flask, render_template, flash, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "tajny klucz"  # app.config jest to słownik przechowujący wszystkie ustawienia naszej
# aplikacji (dane potrzebne do konfiguracji aplikacji). Początkowa wartość "SECRET.KEY" jest ustawiona na None.


@app.route("/")
def index():
    moja_zmienna = "Wiadomość"
    flash(f"Wyświetlam {moja_zmienna}.")  # Funkcja flaskowa wyświetlająca komunikat na stronie. Potrzebuje ona klucza
    # prywatnego (sekretnego), który jest zdefiniowany powyżej (potrzeba ją ustawić na dowolną wartość)
    # potrzeba także zdefiniować odpowiedni kod w HTML
    if moja_zmienna:
        return redirect("/info")  # Pozwala na wywołanie funkcjonalności z innego endpointu
    return render_template("index.html")


@app.route("/info")
def info():
    return "Hello World! :)"


@app.route("/history/<start>/<end>")  # Oznaczamy, że link /history/ ma mieć dwa parametry
def history(start, end):  # Parametry z url zostaną tutaj przekazane
    return f"Start: {start}; End: {end}"
