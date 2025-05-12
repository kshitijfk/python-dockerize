from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    ronaldo_bio_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cristiano Ronaldo - Biography</title>
        <!-- Favicon fix to avoid 404 -->
        <link rel="icon" href="data:;base64,=">
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1f1c2c, #928dab);
                margin: 0;
                padding: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            .card {
                background: white;
                border-radius: 20px;
                padding: 20px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
                width: 350px;
                text-align: center;
                animation: fadeIn 1s ease-in;
            }
            .card img {
                width: 90%;
                border-radius: 15px;
                margin-bottom: 15px;
            }
            .card h1 {
                margin-top: 10px;
                font-size: 2em;
                color: #333;
            }
            .card p {
                color: #555;
                font-size: 0.95em;
                line-height: 1.5;
                margin: 8px 0;
            }
            .highlight {
                font-weight: bold;
                color: #1f1c2c;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="card">
            <!-- Static Ronaldo Image -->
            <img src="https://cdna.artstation.com/p/assets/images/images/061/068/222/large/bright-star-cristiano-ronaldo-edit.jpg?1679944422" alt="Cristiano Ronaldo">
            <h1>Cristiano Ronaldo</h1>
            <p><span class="highlight">Born:</span> February 5, 1985</p>
            <p><span class="highlight">Position:</span> Forward</p>
            <p><span class="highlight">Clubs:</span> Sporting CP, Manchester United, Real Madrid, Juventus, Al-Nassr</p>
            <p><span class="highlight">Achievements:</span> 5 Ballon d'Ors, 5 Champions Leagues, Portugal's top scorer</p>
            <p>Ronaldo is a symbol of determination and excellence. His legacy inspires athletes and fans all around the world.</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(ronaldo_bio_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
