# Order-Search-Application
A simple desktop application built with Python and Tkinter that allows users to search through order details and print the results. The application provides a user-friendly interface for searching order records stored in a text file and printing the search results.

<h2>Features</h2>

Search through order records using case-insensitive queries
Real-time display of search results
Print functionality with browser-based preview
Scrollable text area for viewing results
Modern UI with icon-based print button

<h2>Prerequisites</h2>
Before running this application, make sure you have the following installed:

Python 3.x
PIL (Python Imaging Library) / Pillow

bashCopypip install Pillow
<h2>Required Files</h2>

* OrderDetail.txt - Text file containing order records

* print_icon.png - Icon image for the print button

<h2>Installation</h2>

Clone this repository:

bashCopygit clone https://github.com/yourusername/order-search.git
cd order-search

Install required dependencies:

bashCopypip install -r requirements.txt
<h2>Usage</h2>

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

<h2>How It Works</h2>

<h3>Search Functionality:</h3>

The application reads order records from OrderDetail.txt
Uses regular expressions for case-insensitive search
Displays matching results in real-time


<h3>Print Feature:</h3>

Creates a temporary HTML file with formatted results
Opens the default web browser for printing
Provides a print preview before printing



<h2>Error Handling</h2>
<b>The application includes error handling for:</b>

Missing order detail file.<br>
Print operation failures.<br>
Empty search results

<h3>Contributing</h3>

Fork the repository
Create a new branch for your feature
Commit your changes
Push to the branch
Create a new Pull Request

For support, please open an issue in the GitHub repository or contact [your-email@example.com].
<h2>Acknowledgments</h2>

*Thanks to the Tkinter community for the excellent GUI framework.<br>
*Icons provided by [source of your icons]
