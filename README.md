# Order-Search-Application
A simple desktop application built with Python and Tkinter that allows users to search through order details and print the results. The application provides a user-friendly interface for searching order records stored in a text file and printing the search results.

<h1>Features</h1>

Search through order records using case-insensitive queries
Real-time display of search results
Print functionality with browser-based preview
Scrollable text area for viewing results
Modern UI with icon-based print button

Prerequisites
Before running this application, make sure you have the following installed:

Python 3.x
PIL (Python Imaging Library) / Pillow

bashCopypip install Pillow
Required Files

OrderDetail.txt - Text file containing order records
print_icon.png - Icon image for the print button

Installation

Clone this repository:

bashCopygit clone https://github.com/yourusername/order-search.git
cd order-search

Install required dependencies:

bashCopypip install -r requirements.txt
Usage

Run the application:

bashCopypython order_search.py

Enter your search query in the search box
Click the "Search" button or press Enter to search
View results in the scrollable text area
Click the print icon to print the current results

File Structure
Copyorder-search/
│
├── order_search.py        # Main application file
├── OrderDetail.txt        # Order records database
├── print_icon.png        # Print button icon
├── requirements.txt      # Python dependencies
└── README.md            # This file
How It Works

Search Functionality:

The application reads order records from OrderDetail.txt
Uses regular expressions for case-insensitive search
Displays matching results in real-time


Print Feature:

Creates a temporary HTML file with formatted results
Opens the default web browser for printing
Provides a print preview before printing



Error Handling
The application includes error handling for:

Missing order detail file
Print operation failures
Empty search results

Contributing

Fork the repository
Create a new branch for your feature
Commit your changes
Push to the branch
Create a new Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Support
For support, please open an issue in the GitHub repository or contact [your-email@example.com].
Acknowledgments

Thanks to the Tkinter community for the excellent GUI framework
Icons provided by [source of your icons]
