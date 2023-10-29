# Python_project_submission_gkame
# The application movie_picker is created to suggest a movie suggestion to user based on the Genre selected by the user. 
# This application provides a list of Genres available in the website IMdb under the category "Popular movies" for the user to select his/her preference
# This is a selenium based application developed by scraping the IMdb website using Python. The application scrapes data from Movie Category and "Browse Movie by Genre" and reads all the Genres availble in category "Popular Movies in the Genre". This data is read by a pandas dataframe and is given as an excel file "movie_data.xlsx" for the user. The excel file consists of the URL linka for all the Genres which are displayed on the terminal. The automation will prompt the user for input a genre among the displayed. Once the user inputs the automation uses a module by name random to pick up a movie by scraping the "Top 50 movies under the Genre" from the website and displays a suggestion of movie for the user to watch.
# Instructions to run the application
  # 1. Initiate the tool movie_picker.exe It will take few minutes to load.
  # 2. When the driver loads the page the terminal will provide a prompt of successful page load
  # 3. The terminal also will load the list of Genre available from the website and asks the user for the input and once the user provides the input the application will suggest a movie to watch and closes the driver.
