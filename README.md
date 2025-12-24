# DPDC Balance Checker

**DPDC Balance Checker** is a Python-based tool that allows users to fetch and view electricity balance and account information from the Dhaka Power Distribution Company (DPDC) Smart Meter system. It uses DPDC’s API endpoints to retrieve customer usage data securely.

## License

This project is for educational purposes and personal use.

## Notes

* Some API endpoints may require session cookies or updated tokens; the script demonstrates basic usage.
* Front-end constants may change if DPDC updates their app; always check the latest `environment.js`.

## Online Usage
Go to the website () and enter your `customer id` to view your meter balance.

## Local Running Guide
``` shell
git clone https://github.com/mdarif551578/DPDC-balance-checker.git
```
``` shell
cd ./DPDC-balance-checker
```
``` shell
python -m pip install -r requirements.txt
```
``` shell
python -m uvicorn main:app --reload
```





# Additional Notes

## How to Find `AUTH_UI_CLIENT_SECRET_KEYCLOCK` in `environment.js`

This guide will show you how to locate a constant in the DPDC `environment.js` file (or similar front-end JS files) using browser developer tools or a local copy of the file.

## Step 1: Open the Web  (https://amiapp.dpdc.org.bd/)

1. Open the DPDC Smart Meter web application in your browser (Chrome, Firefox, Edge, etc.).
2. Wait for the app to fully load.

## Step 2: Open Developer Tools

1. Press **F12** on your keyboard, or right-click anywhere on the page and select **Inspect**.
2. This will open the **Developer Tools** window.

## Step 3: Go to the Sources Tab

1. In Developer Tools, click on the **Sources** tab.
2. Look for a folder structure on the left side (this is where the app’s JavaScript files are stored).
3. Navigate to `static/js/` (or a similar folder structure).
4. Locate the file named `environment.js`.

> **Tip:** Some apps bundle their JS, so you might need to expand folder trees to see the file.

## Step 4: Open and Search the File

1. Click on `environment.js` to open it in the Sources tab.
2. Press **Ctrl+F** (or Cmd+F on Mac) to open the search box.
3. Type the constant name you are looking for:

   ```
   AUTH_UI_CLIENT_SECRET_KEYCLOCK
   ```
4. The editor should highlight the line where the constant is defined, e.g.:

   ```javascript
   const AUTH_UI_CLIENT_SECRET_KEYCLOCK = "0yFsAl4nN9jX1GGkgOrvpUxDarf2DT40";
   ```

## Step 5: Use that in the `CLIENT_SECRET` config.










