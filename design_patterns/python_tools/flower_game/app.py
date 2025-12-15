from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flower Game</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            overflow: hidden;
            position: relative;
        }
        #score {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.9);
            padding: 15px 30px;
            border-radius: 25px;
            font-size: 24px;
            font-weight: bold;
            color: #333;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            z-index: 1000;
        }
        .flower {
            position: absolute;
            font-size: 50px;
            cursor: pointer;
            user-select: none;
            transition: transform 0.2s ease, opacity 0.2s ease;
            animation: appear 0.3s ease;
        }
        .flower:hover {
            transform: scale(1.2);
        }
        .flower:active {
            transform: scale(0.9);
        }
        @keyframes appear {
            from {
                transform: scale(0);
                opacity: 0;
            }
            to {
                transform: scale(1);
                opacity: 1;
            }
        }
    </style>
</head>
<body>
    <div id="score">Score: <span id="scoreValue">0</span></div>
    <div id="gameArea"></div>
    <script>
        let score = 0;
        const gameArea = document.getElementById('gameArea');
        const scoreValue = document.getElementById('scoreValue');
        const flowerSize = 50;
        const padding = 30;
        
        function spawnFlower() {
            const flower = document.createElement('div');
            flower.className = 'flower';
            flower.textContent = '🌸';
            flower.style.left = (padding + Math.random() * (window.innerWidth - flowerSize - padding * 2)) + 'px';
            flower.style.top = (padding + Math.random() * (window.innerHeight - flowerSize - padding * 2)) + 'px';
            
            flower.addEventListener('click', function() {
                flower.style.opacity = '0';
                flower.style.transform = 'scale(0)';
                setTimeout(() => flower.remove(), 200);
                score++;
                scoreValue.textContent = score;
            });
            
            gameArea.appendChild(flower);
        }
        
        function startGame() {
            spawnFlower();
            setInterval(() => {
                spawnFlower();
            }, 2000 + Math.random() * 1000);
        }
        
        startGame();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=6000)

