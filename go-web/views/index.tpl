<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Generator</title>
    <style>
        *::before,
        *::after {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --background: #FAFAFA;
            --text: #000000;
            --border: #000000;
        }

        .dark {
            --background: #000000;
            --text: #FAFAFA;
            --border: #FAFAFA;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--background);
            color: var(--text);
            transition: background-color 0.3s ease, color 0.3s ease;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .container {
            width: 100%;
            max-width: 400px;
            padding: 2rem;
            border: 1px solid var(--border);
            border-radius: 8px;
        }

        h2 {
            margin-bottom: 1.5rem;
            font-size: 1.5rem;
        }

        .form-group {
            margin-bottom: 1rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
        }

        input {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid var(--border);
            background-color: var(--background);
            color: var(--text);
            border-radius: 4px;
            font-size: 1rem;
        }

        input:focus {
            outline: none;
            box-shadow: 0 0 0 2px var(--border);
        }

        .row {
            display: flex;
            gap: 10%;
        }

        .col {
            flex: 1;
        }

        button {
            width: 105%;
            padding: 0.75rem;
            background-color: var(--text);
            color: var(--background);
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            transition: opacity 0.3s ease;
        }

        button:hover {
            opacity: 0.9;
        }

        .theme-toggle {
            position: fixed;
            top: 1rem;
            right: 1rem;
            background: none;
            border: none;
            color: var(--text);
            font-size: 1.5rem;
            cursor: pointer;
            z-index: 1000;
        }
    </style>
</head>

<body>
    <button id="themeToggle" class="theme-toggle" aria-label="Toggle dark mode">🌓</button>

    <div class="container">
        <h2>Password Generator</h2>
        <form id="passwordForm" method="post" action="/submit">
            <div class="form-group">
                <label for="site">Site</label>
                <input type="text" id="site" name="site" placeholder="Enter site name" value="{{.Site}}" required>
            </div>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" placeholder="Enter username" value="{{.Username}}" required>
            </div>
            <div class="row">
                <div class="col">
                    <div class="form-group">
                        <label for="length">Length</label>
                        <input type="number" id="length" name="length" value="16" placeholder="Length" min="1" required>
                    </div>
                </div>
                <div class="col">
                    <div class="form-group">
                        <label for="counter">Counter</label>
                        <input type="number" id="counter" name="counter" value="1" placeholder="Counter" min="1" required>
                    </div>
                </div>
            </div>
            <button type="submit" id="generateButton">Generate & Copy</button>
        </form>
    </div>
<!-- 
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const themeToggle = document.getElementById('themeToggle');
            const generateButton = document.getElementById('generateButton');

            function setTheme(isDark) {
                document.body.classList.toggle('dark', isDark);
                localStorage.setItem('darkMode', isDark);
                themeToggle.setAttribute('aria-label', isDark ? 'Toggle light mode' : 'Toggle dark mode');
                themeToggle.textContent = isDark ? '☀️' : '🌓';
            }

            themeToggle.addEventListener('click', function () {
                const isDark = !document.body.classList.contains('dark');
                setTheme(isDark);
            });

            generateButton.addEventListener('click', function () {
                const site = document.getElementById('site').value;
                const username = document.getElementById('username').value;
                const length = document.getElementById('length').value;
                const counter = document.getElementById('counter').value;

                // This is a placeholder for the actual password generation logic
                const generatedPassword = `${site}-${username}-${length}-${counter}`;

                // Copy to clipboard
                navigator.clipboard.writeText(generatedPassword).then(function () {
                    alert('Password generated and copied to clipboard!');
                }, function (err) {
                    console.error('Could not copy text: ', err);
                });
            });

            // Check for saved theme preference or prefer-color-scheme
            const savedTheme = localStorage.getItem('darkMode');
            const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

            if (savedTheme === 'true' || (savedTheme === null && prefersDark)) {
                setTheme(true);
            }
        });
    </script> -->
</body>

</html>