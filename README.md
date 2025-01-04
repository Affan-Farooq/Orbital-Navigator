# International Space Station Tracker and Notifier
#### Video Demo: https://youtu.be/c1wH8O4hbJE
#### Description:
This program is designed to track the International Space Station (ISS) and notify you when it's<br>
overhead within a ±5-degree range of your current latitude and longitude. It only sends notifications<br>
when the ISS is overhead during the night (after sunset and before sunrise) to increase the likelihood<br>
of visibility.

#### Features:
<ul>
    <li>Tracks the current location of the ISS.</li>
    <li>Determines the user's current geolocation based on IP address.</li>
    <li>Checks whether the ISS is within a ±5-degree range of the user's location.</li>
    <li>Sends an email notification if the ISS is overhead during night hours.</li>
</ul>

#### Requirements:
<ul>
    <li>Python 3.x</li>
    <li>requests (External Library)</li>
    <li>apiip (External Library)</li>
    <li>python-dotenv (External Library)</li>
</ul>

#### Installation:
<ol>
    <li>Clone or download this repository to your local machine.</li>
    <li>Install the required dependencies: <pre style="max-width: 400px"><code>pip install -r requirements.txt</code></pre></li>
    <li>The `requirements.txt` file should contain: <pre style="max-width: 400px"><code>requests<br>apiip<br>python-dotenv</code></pre></li>
</ol>

#### Usage:
<ol>
    <li>Ensure you have set up your email credentials correctly in the `notify` function.</li>
    <li>Run the script: <pre style="max-width: 400px"><code>python iss_tracker_notifier.py</code></pre></li>
    <li>The program runs indefinitely, checking the ISS's location every 60 seconds.</li>
</ol>

#### Configuration:
<ul>
    <li>API Keys: Replace the placeholders in the get_geolocation and valid_time functions with your actual API keys.</li>
    <li>Email Credentials: Enter your email address and password in the notify function for the email notifications.<br>If using Gmail, you may need to set up an app-specific password.</li>
</ul>

#### Notes:
<ol>
    <li>The program uses your public IP address to estimate your geographical location.</li>
    <li>Email notifications require an SMTP server setup. The current configuration is for Gmail.</li>
    <li>Ensure your email and password are stored securely.</li>
    <li>The program checks the ISS location every 60 seconds. This interval can be adjusted as needed.</li>
</ol>

#### License:
This project is open source and available under the <a>MIT License</a>.
