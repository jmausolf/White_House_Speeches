# White House Speeches

This script was used to collect the speeches and remarks of President Obama during his administration. 

Disclaimer: Since the White House frequently changes the HTML layout of their speeches<sup>1</sup>, this script will need updating to be implemented on the current administration.

## Output

This package utilizes both Python and Shell scripts to create a unique text file for every speech and remark from the White House:

https://www.whitehouse.gov/briefing-room/speeches-and-remarks

This generates, logs, and sorts the unique URLs for every speech and remark by different parties, chiefly, the President, Vice President, First Lady, Second Lady, as well as other members of the executive staff. After collecting URLS, the package runs a parser on these URLs, extracting the content to individual text files, labeled by date, and sorted into folders by speaker (President, Vice President, First Lady, Second Lady, Other). URLs that result in parsing errors will be saved to a separate .CSV file for review. Once collected, the text can be analyzed using a method of your preference, such as a Python-based script to extract keywords and phrases [tutorial here](http://jmausolf.github.io/code/Analyzing_Text_in_Python/).


## Dependencies

To run this package, you will need several dependencies. 

1. This package was written on and assumes you are running a Mac system, not Linux.
2. This package requires an Anaconda Distribution of Python, either 2.7+ or 3.5+
	* see https://www.continuum.io/downloads
3. This package runs a Python library [Selenium](http://selenium-python.readthedocs.io) which must be installed.
4. The Selenium script will utilize the Firefox browser.

## To Run

1. Git clone this repository:
	```git clone https://github.com/jmausolf/White_House_Speeches```

2. Navigate to the `Shell_Command` folder in this repository using Terminal (Command Prompt) and run

	- ```bash 2015_Current_Sub.sh```

The script will work to collect White House Speeches and Remarks. During the last run of the script, the White House used a JavaScript page scrolling utility, such that new speeches links would load once a user scrolled to the bottom of the page. Selenium automates this process, and the script will launch Firefox Browser windows. Do not close these windows until the script completes. They may be safely minimized while running.

---

<sup>1</sup> The White House HTML structure changed more three times during the development of the script under the Obama administration between 2015 and 2016.
