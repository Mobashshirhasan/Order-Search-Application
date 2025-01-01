# Order-Search-Application
A simple desktop application built with Python and Tkinter that allows users to search through order details and print the results. The application provides a user-friendly interface for searching order records stored in a text file and printing the search results.

<h1>Features</h1>

Search through order records using case-insensitive queries
Real-time display of search results
Print functionality with browser-based preview
Scrollable text area for viewing results
Modern UI with icon-based print button

<h1>Prerequisites</h1>
Before running this application, make sure you have the following installed:

Python 3.x
PIL (Python Imaging Library) / Pillow

bashCopypip install Pillow
<h1>Required Files</h1>

OrderDetail.txt - Text file containing order records
print_icon.png - Icon image for the print button

<h1>Installation</h1>

Clone this repository:

bashCopygit clone https://github.com/yourusername/order-search.git
cd order-search

Install required dependencies:

bashCopypip install -r requirements.txt
<h1>Usage</h1>

Run the application:

bashCopypython order_search.py

Enter your search query in the search box
Click the "Search" button or press Enter to search
View results in the scrollable text area
Click the print icon to print the current results

<h1>File Structure</h1>
Copyorder-search/
│
├── order_search.py        # Main application file
├── OrderDetail.txt        # Order records database
├── print_icon.png        # Print button icon
├── requirements.txt      # Python dependencies
└── README.md            # This file
How It Works

<h1>Search Functionality:</h1>

The application reads order records from OrderDetail.txt
Uses regular expressions for case-insensitive search
Displays matching results in real-time


<h1>Print Feature:</h1>

Creates a temporary HTML file with formatted results
Opens the default web browser for printing
Provides a print preview before printing



<h1>Error Handling</h1>
The application includes error handling for:

Missing order detail file
Print operation failures
Empty search results

<h1>Contributing</h1>

Fork the repository
Create a new branch for your feature
Commit your changes
Push to the branch
Create a new Pull Request

<h1>License</h1>
This project is licensed under the MIT License - see the LICENSE file for details.
Support
For support, please open an issue in the GitHub repository or contact [your-email@example.com].
Acknowledgments

Thanks to the Tkinter community for the excellent GUI framework
Icons provided by [source of your icons]
