# SeleniumBrowserAutomationPractice
The code will log in to the specified website using the provided credentials and then print the page title to confirm a successful login. The browser will remain open for manual inspection until you press Enter. Afterward, the browser will close.
Place the chromedriver executable in a directory (e.g., /chromedriver).
Make sure the version of ChromeDriver matches your installed version of Google Chrome.
Library Import:

The script imports the necessary modules from Selenium to handle web automation tasks.

Login Credentials:

Your login credentials (username and password) are defined at the beginning of the script.

Setup WebDriver:

The path to the ChromeDriver executable is specified, and Chrome WebDriver is initialized with optional configurations.

Navigating to Login Page:

The script opens the specified website login page using the get method.

Waiting for Elements:

The script uses explicit waits to ensure that elements (like username and password fields) are visible and clickable before interacting with them.

Entering Credentials:

The username and password are entered into their respective fields, and the login button is clicked.

Verifying Login:

After clicking the login button, the script waits for the page title to confirm successful login and prints the title.

Manual Inspection:

The browser remains open until the user presses Enter, allowing for manual inspection of the page.

Closing the Browser:

Finally, the browser is closed using driver.quit().

