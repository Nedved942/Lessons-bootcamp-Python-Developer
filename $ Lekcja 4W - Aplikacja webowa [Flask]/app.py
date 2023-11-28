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


history_data = []


# Podpinamy 3 routingi do tego samego widoku, każdy z nich przyjmuje inne parametry
@app.route("/history/")
@app.route("/history/<int:start>/")
@app.route("/history/<int:start>/<int:end>/")
def history_view(start=0, end=len(history_data)):  # Parametry z url zostaną tutaj przekazane
    # Powyżej bazowa definicja argumentów
    return render_template("history.html", history_data=history_data[start:end])
