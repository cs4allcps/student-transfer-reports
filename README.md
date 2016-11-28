# student-transfer-reports
Creates reports on where 9th graders went to school the year before.

# Products
For each school, there are 3 (really 2) representations of student flow data that we want to create, which are slightly different depending on whether the school is a high school or elementary school.
1. A simple list of schools freshmen were at the year before, with a count of how many students came from that source. (Some students may repeat the 9th grade, so a school can have itself as a source.)
  - This should be output as a .csv and as a simple text file.
  - For elementary/middle schools, this is a list of destinations for their students.
1. A diagram showing student flow visually.
  - A central rectangle for the school, and a cluster of rectangles for source schools
  - Arrows pointing from source schools to the central school
    - Arrow width proportional to number
    - Arrow length proportional to geographic distance between schools (not a priority feature)
  - Indicator for whether school has a CS program
    - If so, show courses in a condensed format (e.g. "ECS,APCSP" or "CSF")
  - May have to adjust cutoffs (e.g. if less than 3 students come from a school, or if there are more than N sources, group other sources as 'Other')
  
