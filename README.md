# student-transfer-reports
Creates reports on where 9th graders went to school the year before.

##Products##

For reports on where 9th graders matriculated from for each high school and reports on where 9th graders matriculated to for each previous school:

	(1) Make sure Inbound9thGradeStudentCourseRecommendations.csv is located in the same
		folder as is student-transfer-reports.py

	(2) Navigate to that folder in shell and enter

			python3 student-transfer-reports.py

	(3) A file called 'reports' will be created. In /reports you should find the following files

			(a) /current, which contains
					(i) /csv_reports
					(ii) /txt_reports

			(b) /previous, which similarly contains
					(i) /csv_reports
					(ii) /txt_reports

		'current' contains reports for current schools (i.e. high schools) on which school 
		freshman attended the prior year (which can be middle schools or high schools in the 
		case that a student repeats freshman year). Reports are sorted into .csv and .txt files,
		as in the above filepath.

		'previous' contains reports on where students matriculated to from each middle school
		(or, in the case of students repeating freshman year, high schools), and these reports
		are sorted in the same manner as is 'current'.

		Filenames for each report are the same as the school name* taken from the 'STUDENT_CURRENT_SCHOOL' column of Inbound9thGradeStudentCourseRecommendations.csv for
		high schools and from the 'STUDENT_NEXT_YEAR_SCHOOL_NAME' column for previous schools.
		(It's unclear why the dataset refers to previous schools as 'next_year_schools', but 
		it does) with the extension .csv or .txt depending on which folder it's found in.
			
			* There is an exception to this rule: any "/" found in the school name was replaced
				with " | " in the filename to avoid confusion with filepaths


For treemaps that graphically illustrate student flow for a given school:

	(1) Follow the directions above to generate reports for each school

	(2) Run draw_school.py in iPython 3

	(3) Set a variable filepath for the .csv report of the school you want to illustrate

			e.g. the filepath for Dyett Arts High School is

					./reports/current/csv_reports/DYETT ARTS HS.csv

			So if you want to illustrate Dyett's student flow, you would enter

					filepath = './reports/current/csv_reports/DYETT ARTS HS.csv'

	(4) You now have the option of displaying the image directly or saving it to a .png file

			(a) To display it directly, enter the command

					draw(filepath)

			(b) To save the image to a .png file,

					(i) Pick a filename for your image, which MUST end in .png 
						and save that filename to a variable output_filename

							output_filename = 'your_desired_filename_here.png'

					(ii) Run the following command

							draw(filepath, output_filename)

For a diagram with a rectangle in the middle labelled with the school you want to visualize
and lines extending to rectangles labelled with schools the students of the school you are
drawing matriculate to/from (lines are proportional in width to the number of students matriculating between the two schools/rectangles):

	(0) Note that this script isn't of spectacular quality; this part of the project was 
		abandoned in favor of the treemap feature, as treemaps were determined to be better
		(i.e. both cleaner and more readable) representations of the data. Consequently, 
		there are still unresolved issues like text overflowing from the boxes, and the 
		output images seem a little bit crammed just by virtue of the way data is represented.
		As such, this isn't the recommended way to visualize the data.

	(1) Follow the directions above to generate reports for each school

	(2) Run graph-generator.py in iPython 3

	(3) Set a variable filepath for the .csv report of the school you want to illustrate
		(more detailed intructions in Step (3) of the directions above)

	(4) You now have the option of displaying the image directly or saving it to a .png file

			(a) To display it directly, enter the command

					draw_graph(filepath)

			(b) To save the image to a .png file,

					(i) Pick a filename for your image, which MUST end in .png 
						and save that filename to a variable output_filename

							output_filename = 'your_desired_filename_here.png'

					(ii) Run the following command

							save_graph(filepath, output_filename)

The draw() function from draw_school.py and the save_graph() function from graph-generator.py can, of course, be imported into other python scripts using the commands

	from draw_school import draw

	from graph-generator import save_graph

allowing you to write code to generate and save graphics to represent student flow for many schools at once.

