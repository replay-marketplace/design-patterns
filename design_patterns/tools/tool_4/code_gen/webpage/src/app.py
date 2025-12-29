from flask import Flask, render_template_string, jsonify
import random
import time

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXUS // SYSTEMS</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&family=Orbitron:wght@400;700;900&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        :root {
            --primary: #00ff88;
            --secondary: #00d4ff;
            --accent: #ff0080;
            --dark: #0a0a0f;
            --darker: #050508;
            --text: #e0e0e0;
        }
        
        body {
            font-family: 'JetBrains Mono', monospace;
            background: var(--darker);
            color: var(--text);
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        .matrix-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.1;
        }
        
        .grid-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(rgba(0, 255, 136, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 255, 136, 0.03) 1px, transparent 1px);
            background-size: 50px 50px;
            z-index: -1;
        }
        
        .scanline {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                transparent 50%,
                rgba(0, 0, 0, 0.1) 50%
            );
            background-size: 100% 4px;
            z-index: 1000;
            pointer-events: none;
            opacity: 0.3;
        }
        
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(5, 5, 8, 0.9);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(0, 255, 136, 0.2);
            z-index: 100;
        }
        
        .logo {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.5rem;
            font-weight: 900;
            color: var(--primary);
            text-shadow: 0 0 20px var(--primary);
            letter-spacing: 3px;
        }
        
        .logo span {
            color: var(--accent);
        }
        
        .nav-links {
            display: flex;
            gap: 40px;
            list-style: none;
        }
        
        .nav-links a {
            color: var(--text);
            text-decoration: none;
            font-size: 0.85rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            transition: all 0.3s;
            position: relative;
        }
        
        .nav-links a:hover {
            color: var(--primary);
            text-shadow: 0 0 10px var(--primary);
        }
        
        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--primary);
            transition: width 0.3s;
        }
        
        .nav-links a:hover::after {
            width: 100%;
        }
        
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 100px 50px;
            position: relative;
        }
        
        .hero-content {
            text-align: center;
            max-width: 900px;
        }
        
        .glitch {
            font-family: 'Orbitron', sans-serif;
            font-size: 4rem;
            font-weight: 900;
            color: var(--primary);
            text-shadow: 
                0 0 10px var(--primary),
                0 0 20px var(--primary),
                0 0 40px var(--primary);
            animation: glitch 2s infinite;
            position: relative;
        }
        
        @keyframes glitch {
            0%, 90%, 100% { transform: translate(0); }
            92% { transform: translate(-2px, 2px); }
            94% { transform: translate(2px, -2px); }
            96% { transform: translate(-2px, -2px); }
            98% { transform: translate(2px, 2px); }
        }
        
        .subtitle {
            font-size: 1.2rem;
            color: var(--secondary);
            margin-top: 20px;
            letter-spacing: 5px;
            text-transform: uppercase;
        }
        
        .terminal-text {
            font-size: 1rem;
            color: var(--text);
            margin-top: 40px;
            padding: 30px;
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(0, 255, 136, 0.3);
            border-radius: 5px;
            text-align: left;
            position: relative;
        }
        
        .terminal-text::before {
            content: '> SYSTEM INITIALIZED';
            position: absolute;
            top: -12px;
            left: 20px;
            background: var(--darker);
            padding: 0 10px;
            color: var(--primary);
            font-size: 0.8rem;
        }
        
        .typing {
            overflow: hidden;
            white-space: nowrap;
            animation: typing 3s steps(50);
        }
        
        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }
        
        .cta-button {
            display: inline-block;
            margin-top: 40px;
            padding: 15px 50px;
            font-family: 'Orbitron', sans-serif;
            font-size: 1rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: var(--dark);
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border: none;
            border-radius: 0;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transition: all 0.3s;
            text-decoration: none;
        }
        
        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 
                0 10px 30px rgba(0, 255, 136, 0.3),
                0 0 50px rgba(0, 255, 136, 0.2);
        }
        
        .cta-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s;
        }
        
        .cta-button:hover::before {
            left: 100%;
        }
        
        .stats-section {
            padding: 100px 50px;
            background: linear-gradient(180deg, var(--darker) 0%, var(--dark) 100%);
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .stat-card {
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(0, 255, 136, 0.2);
            padding: 40px;
            text-align: center;
            position: relative;
            overflow: hidden;
            transition: all 0.3s;
        }
        
        .stat-card:hover {
            border-color: var(--primary);
            transform: translateY(-5px);
            box-shadow: 0 10px 40px rgba(0, 255, 136, 0.1);
        }
        
        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
        }
        
        .stat-number {
            font-family: 'Orbitron', sans-serif;
            font-size: 3rem;
            font-weight: 900;
            color: var(--primary);
            text-shadow: 0 0 20px var(--primary);
        }
        
        .stat-label {
            font-size: 0.85rem;
            color: var(--text);
            margin-top: 10px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        .features-section {
            padding: 100px 50px;
        }
        
        .section-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.5rem;
            text-align: center;
            color: var(--primary);
            margin-bottom: 60px;
            text-shadow: 0 0 30px var(--primary);
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 40px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .feature-card {
            background: linear-gradient(135deg, rgba(0, 255, 136, 0.05), rgba(0, 212, 255, 0.05));
            border: 1px solid rgba(0, 255, 136, 0.1);
            padding: 40px;
            position: relative;
            transition: all 0.3s;
        }
        
        .feature-card:hover {
            border-color: var(--secondary);
            background: linear-gradient(135deg, rgba(0, 255, 136, 0.1), rgba(0, 212, 255, 0.1));
        }
        
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 20px;
        }
        
        .feature-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.3rem;
            color: var(--secondary);
            margin-bottom: 15px;
        }
        
        .feature-desc {
            font-size: 0.9rem;
            line-height: 1.8;
            color: rgba(224, 224, 224, 0.7);
        }
        
        .console-section {
            padding: 100px 50px;
            background: var(--dark);
        }
        
        .console {
            max-width: 900px;
            margin: 0 auto;
            background: #0d0d12;
            border: 1px solid rgba(0, 255, 136, 0.3);
            border-radius: 8px;
            overflow: hidden;
        }
        
        .console-header {
            background: rgba(0, 255, 136, 0.1);
            padding: 15px 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .console-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }
        
        .console-dot.red { background: #ff5f56; }
        .console-dot.yellow { background: #ffbd2e; }
        .console-dot.green { background: #27ca40; }
        
        .console-body {
            padding: 30px;
            font-size: 0.9rem;
            line-height: 2;
        }
        
        .console-line {
            color: var(--text);
        }
        
        .console-line .prompt {
            color: var(--primary);
        }
        
        .console-line .command {
            color: var(--secondary);
        }
        
        .console-line .output {
            color: rgba(224, 224, 224, 0.6);
        }
        
        .cursor {
            display: inline-block;
            width: 10px;
            height: 18px;
            background: var(--primary);
            animation: blink 1s infinite;
            vertical-align: middle;
        }
        
        @keyframes blink {
            0%, 50% { opacity: 1; }
            51%, 100% { opacity: 0; }
        }
        
        footer {
            padding: 50px;
            text-align: center;
            border-top: 1px solid rgba(0, 255, 136, 0.1);
        }
        
        footer p {
            color: rgba(224, 224, 224, 0.5);
            font-size: 0.85rem;
        }
        
        .status-indicator {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-top: 20px;
            padding: 10px 20px;
            background: rgba(0, 255, 136, 0.1);
            border: 1px solid rgba(0, 255, 136, 0.3);
            border-radius: 20px;
        }
        
        .status-dot {
            width: 8px;
            height: 8px;
            background: var(--primary);
            border-radius: 50%;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; box-shadow: 0 0 10px var(--primary); }
            50% { opacity: 0.5; box-shadow: 0 0 5px var(--primary); }
        }
        
        @media (max-width: 1024px) {
            .stats-grid { grid-template-columns: repeat(2, 1fr); }
            .features-grid { grid-template-columns: repeat(2, 1fr); }
        }
        
        @media (max-width: 768px) {
            .glitch { font-size: 2.5rem; }
            .stats-grid { grid-template-columns: 1fr; }
            .features-grid { grid-template-columns: 1fr; }
            nav { padding: 20px; }
            .nav-links { display: none; }
        }
    </style>
</head>
<body>
    <div class="scanline"></div>
    <div class="grid-overlay"></div>
    
    <nav>
        <div class="logo">NEXUS<span>//</span>SYS</div>
        <ul class="nav-links">
            <li><a href="#">Protocol</a></li>
            <li><a href="#">Network</a></li>
            <li><a href="#">Nodes</a></li>
            <li><a href="#">Terminal</a></li>
        </ul>
    </nav>
    
    <section class="hero">
        <div class="hero-content">
            <h1 class="glitch">NEXUS SYSTEMS</h1>
            <p class="subtitle">Next Generation Infrastructure</p>
            <div class="terminal-text">
                <p class="typing"><span style="color: var(--primary);">$</span> Initializing quantum-encrypted neural network...</p>
                <p><span style="color: var(--primary);">$</span> Status: <span style="color: var(--secondary);">OPERATIONAL</span></p>
                <p><span style="color: var(--primary);">$</span> Nodes online: <span style="color: var(--accent);">{{ node_count }}</span></p>
                <p><span style="color: var(--primary);">$</span> Latency: <span style="color: var(--secondary);">0.003ms</span></p>
            </div>
            <a href="#" class="cta-button">Initialize Connection</a>
            <div class="status-indicator">
                <span class="status-dot"></span>
                <span>All Systems Operational</span>
            </div>
        </div>
    </section>
    
    <section class="stats-section">
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number" id="stat1">99.99</div>
                <div class="stat-label">% Uptime</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="stat2">2.4M</div>
                <div class="stat-label">Requests/sec</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="stat3">< 1ms</div>
                <div class="stat-label">Latency</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="stat4">256</div>
                <div class="stat-label">Bit Encryption</div>
            </div>
        </div>
    </section>
    
    <section class="features-section">
        <h2 class="section-title">&lt;/CAPABILITIES&gt;</h2>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3 class="feature-title">Quantum Processing</h3>
                <p class="feature-desc">Harness the power of quantum computing for unprecedented processing speeds and cryptographic security.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔐</div>
                <h3 class="feature-title">Zero-Trust Security</h3>
                <p class="feature-desc">Military-grade encryption with continuous verification. Every request authenticated, every connection secured.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🌐</div>
                <h3 class="feature-title">Global Mesh Network</h3>
                <p class="feature-desc">Distributed infrastructure spanning 50+ regions. Automatic failover and intelligent load balancing.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🧠</div>
                <h3 class="feature-title">Neural Analytics</h3>
                <p class="feature-desc">AI-powered insights and predictive analysis. Real-time threat detection and autonomous response.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚙️</div>
                <h3 class="feature-title">Auto-Scaling</h3>
                <p class="feature-desc">Infinite scalability with zero configuration. Resources adapt to demand in milliseconds.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📡</div>
                <h3 class="feature-title">Edge Computing</h3>
                <p class="feature-desc">Process data at the edge for minimal latency. Bring computation closer to your users.</p>
            </div>
        </div>
    </section>
    
    <section class="console-section">
        <h2 class="section-title">&lt;/TERMINAL&gt;</h2>
        <div class="console">
            <div class="console-header">
                <span class="console-dot red"></span>
                <span class="console-dot yellow"></span>
                <span class="console-dot green"></span>
                <span style="margin-left: 20px; color: var(--text); font-size: 0.8rem;">nexus@system:~</span>
            </div>
            <div class="console-body">
                <div class="console-line"><span class="prompt">nexus@system:~$</span> <span class="command">nexus init --quantum</span></div>
                <div class="console-line"><span class="output">[OK] Quantum core initialized</span></div>
                <div class="console-line"><span class="output">[OK] Neural network connected</span></div>
                <div class="console-line"><span class="output">[OK] Encryption layer active</span></div>
                <div class="console-line"><span class="prompt">nexus@system:~$</span> <span class="command">nexus status</span></div>
                <div class="console-line"><span class="output">System Status: OPTIMAL</span></div>
                <div class="console-line"><span class="output">Active Nodes: {{ node_count }}</span></div>
                <div class="console-line"><span class="output">Threat Level: MINIMAL</span></div>
                <div class="console-line"><span class="prompt">nexus@system:~$</span> <span class="cursor"></span></div>
            </div>
        </div>
    </section>
    
    <footer>
        <p>&copy; 2024 NEXUS SYSTEMS // ALL RIGHTS RESERVED</p>
        <p style="margin-top: 10px; color: var(--primary);">[ CLASSIFIED // LEVEL 5 CLEARANCE REQUIRED ]</p>
    </footer>
    
    <script>
        // Animate numbers on scroll
        const observerOptions = {
            threshold: 0.5
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateStats();
                }
            });
        }, observerOptions);
        
        document.querySelectorAll('.stat-card').forEach(card => {
            observer.observe(card);
        });
        
        function animateStats() {
            // Simple animation effect
            const stats = document.querySelectorAll('.stat-number');
            stats.forEach(stat => {
                stat.style.opacity = '0';
                setTimeout(() => {
                    stat.style.transition = 'opacity 0.5s';
                    stat.style.opacity = '1';
                }, 100);
            });
        }
        
        // Random glitch effect
        setInterval(() => {
            const glitch = document.querySelector('.glitch');
            glitch.style.textShadow = `
                ${Math.random() * 10 - 5}px ${Math.random() * 10 - 5}px 0 rgba(255, 0, 128, 0.7),
                ${Math.random() * 10 - 5}px ${Math.random() * 10 - 5}px 0 rgba(0, 255, 136, 0.7),
                ${Math.random() * 10 - 5}px ${Math.random() * 10 - 5}px 0 rgba(0, 212, 255, 0.7)
            `;
            setTimeout(() => {
                glitch.style.textShadow = '0 0 10px var(--primary), 0 0 20px var(--primary), 0 0 40px var(--primary)';
            }, 100);
        }, 3000);
    </script>
</body>
</html>
'''
    
    @app.route('/')
    def index():
        """Render the main landing page."""
        return render_template_string(HTML_TEMPLATE, node_count=random.randint(1000, 9999))
    
    @app.route('/api/status')
    def api_status():
        """Return system status as JSON."""
        return jsonify({
            'status': 'operational',
            'uptime': 99.99,
            'timestamp': int(time.time()),
            'version': '2.4.1'
        })
    
    @app.route('/api/stats')
    def api_stats():
        """Return system statistics as JSON."""
        return jsonify({
            'nodes_online': random.randint(1000, 9999),
            'requests_per_second': random.randint(2000000, 3000000),
            'latency_ms': round(random.uniform(0.001, 0.005), 4),
            'encryption_bits': 256,
            'threat_level': 'minimal'
        })
    
    return app


def index():
    """Standalone index function for module-level import."""
    app = create_app()
    with app.app_context():
        with app.test_request_context():
            return app.view_functions['index']()


def api_status():
    """Standalone api_status function for module-level import."""
    app = create_app()
    with app.app_context():
        with app.test_request_context():
            return app.view_functions['api_status']()


def api_stats():
    """Standalone api_stats function for module-level import."""
    app = create_app()
    with app.app_context():
        with app.test_request_context():
            return app.view_functions['api_stats']()


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
