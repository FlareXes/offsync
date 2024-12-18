<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Manager</title>
    <style>
        :root {
            --background: #FAFAFA;
            --text: #000000;
            --border: #000000;
            --input-bg: #FFFFFF;
            --button-bg: #000000;
            --button-text: #FFFFFF;
        }

        .dark {
            --background: #000000;
            --text: #FAFAFA;
            --border: #FAFAFA;
            --input-bg: #000000;
            /* Changed from #333333 to #000000 */
            --button-bg: #FAFAFA;
            --button-text: #000000;
        }

        .dark input {
            background-color: #000000;
            color: #FAFAFA;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--background);
            color: var(--text);
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        .container {
            width: 100%;
            max-width: 800px;
            padding: 2rem;
        }

        h2 {
            text-align: center;
            margin-bottom: 1.5rem;
        }

        .form-group {
            margin-bottom: 1rem;
        }

        .form-row {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .form-row>div {
            flex: 1;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
        }

        .input-group {
            display: flex;
        }

        input {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid var(--border);
            border-radius: 4px;
            background-color: var(--input-bg);
            color: var(--text);
            font-size: 1rem;
        }

        input:focus {
            outline: none;
            box-shadow: 0 0 0 2px var(--border);
        }

        button {
            padding: 0.5rem 1rem;
            background-color: var(--button-bg);
            color: var(--button-text);
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
            transition: opacity 0.3s ease;
        }

        button:hover {
            opacity: 0.8;
        }

        .copy-button {
            margin-left: 0.5rem;
        }

        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 1rem 0.5rem;
            margin-top: 1rem;
        }

        th,
        td {
            border: none;
            padding: 0.5rem;
            text-align: left;
            background-color: transparent;
        }

        th {
            font-weight: bold;
        }

        td {}

        #darkModeToggle {
            position: fixed;
            top: 1rem;
            right: 1rem;
            font-size: 1.5rem;
            background: none;
            border: none;
            color: var(--text);
            cursor: pointer;
        }
    </style>
</head>

<body>
    <button id="darkModeToggle" aria-label="Toggle dark mode">🌓</button>

    <div class="container">
        <h2>Password Manager</h2>
        <div class="form-row">
            <div class="form-group">
                <label for="secretKey">Secret Key</label>
                <div class="input-group">
                    <input type="password" id="secretKey" placeholder="Enter secret key" required>
                </div>
            </div>
            <div class="form-group">
                <label for="generatedPassword">Generated Password</label>
                <div class="input-group">
                    <input type="text" id="generatedPassword" readonly>
                    <button type="button" class="copy-button"
                        onclick="copyToClipboard('generatedPassword')">Copy</button>
                </div>
            </div>
        </div>
        <button onclick="addRow()" style="margin-bottom: 1rem;">Add Row</button>
        <table>
            <thead>
                <tr>
                    <th>Site</th>
                    <th>Username</th>
                    <th>Length</th>
                    <th>Counter</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody id="passwordTable">
                <!-- Table rows will be dynamically added here -->



                {{if .Profiles}}

                {{range .Profiles}}
                <tr>
                    <td><input name="site" type="text" value="{{.Site}}" placeholder="Enter site name" readonly></td>
                    <td><input name="username" type="text" value="{{.Username}}" placeholder="Enter username" readonly>
                    </td>
                    <td><input name="length" type="number" value="{{.Counter}}" min="1" readonly></td>
                    <td><input name="counter" type="number" value="{{.Length}}" min="1" readonly></td>
                    <td>
                        <button onclick="generateForRow(this)">Generate</button>
                    </td>
                </tr>
                {{end}}
                {{end}}


            </tbody>
        </table>

    </div>

    <script>
        function generatePassword(site, username, length, counter) {
            const profile = {
                Site: site,
                Username: username,
                Length: length,
                Counter: counter
            }

            console.log(profile);


            fetch("/api", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(profile)
            })
                .then(response => response.json())
                .then(profile => {
                    // Display the result from the server
                    document.getElementById("result").innerText = "Result: " + profile.result;
                })
                .catch(error => console.error('Error:', error));
        }


        function copyToClipboard(elementId) {
            const element = document.getElementById(elementId);
            element.select();
            element.setSelectionRange(0, 99999);
            document.execCommand('copy');
            alert('Copied to clipboard: ' + element.value);
        }

        function addRow() {
            const table = document.getElementById('passwordTable');
            const newRow = table.insertRow(0);
            newRow.innerHTML = `
                <td><input name="site" type="text" placeholder="Enter site name" readonly></td>
                <td><input name="username" type="text" placeholder="Enter username" readonly></td>
                <td><input name="length" type="number" value="12" min="1" readonly></td>
                <td><input name="counter" type="number" value="1" min="1" readonly></td>
                <td>
                    <button onclick="generateForRow(this)">Generate</button>
                </td>
            `;
        }

        function generateForRow(button) {
            const row = button.closest('tr');
            const site = row.cells[0].querySelector('input').value;
            const username = row.cells[1].querySelector('input').value;
            const length = parseInt(row.cells[2].querySelector('input').value);
            const counter = parseInt(row.cells[3].querySelector('input').value);

            console.log("->", site, username, length, counter);

            generatePassword(site, username, length, counter);
        }

        function toggleEdit(button) {
            const row = button.closest('tr');
            const inputs = row.querySelectorAll('input');
            const isEditing = button.textContent === 'Edit';

            inputs.forEach(input => {
                input.readOnly = !isEditing;
            });

            button.textContent = isEditing ? 'Save' : 'Edit';

            if (!isEditing) {
                endpoint = window.location.href + "/submit"
                console.log(endpoint);

                const rowData = {};
                inputs.forEach(input => {
                    rowData[input.name] = input.value;
                    console.log(input.name, input.value);

                });

                console.log(JSON.stringify(rowData));


                fetch('/profiles/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(rowData),
                })
                    .then(response => response.json())
                    .then(data => {
                        alert(`Row saved! Server response: ${JSON.stringify(data)}`);
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                        alert('Error saving row. Please try again.');
                    });

            }
        }

        document.getElementById('darkModeToggle').addEventListener('click', function () {
            document.body.classList.toggle('dark');
            localStorage.setItem('darkMode', document.body.classList.contains('dark'));
        });

        // Check for saved theme preference
        if (localStorage.getItem('darkMode') === 'true') {
            document.body.classList.add('dark');
        }

        // Add initial row
        addRow();
    </script>
</body>

</html>