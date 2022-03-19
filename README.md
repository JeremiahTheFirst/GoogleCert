# GoogleCert
Just some scripts created to pass the final project(s) for the Google Automation Certificate

Namely: 
auto_email_report_cars.py - loads car sales data from a json file and analyzes it to identify cars generating the most revenue, most sales, and which year had the most sales
upload_feedback.py - takes feedback found in text files and then posts it to a website/API

change_image.py - converts .tiff files to .jpeg and resizes them (for use with webpage listing products)
supplier_image_upload.py - using the images converted in change_image.py, uploads them to a website
run.py - takes text files listing product details, splits the details into specific fields and then posts to a website
reports.py - sets up a baseline report template
emails.py - sets up a baseline email template and sending process
report_email.py - generates a PDF report using reports.py and emails it to a user using emails.py
health_check.py - checks to ensure CPU usage is below 80%, disk usage is above 20%, available memory is over 500 MB, and localhost resolves to 127.0.0.1, emailing a warning to a user if any of the conditions are tripped (usage: cron job to keep checks running).
