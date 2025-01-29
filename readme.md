# Labour market research project

My labour market research project is targeted to analysis of work conditions and qualification requirements within IT industry and consists of the following basic parts:
- obtaining initial data from a user
- parsing the career site (www.hh.ru) via public API (api.hh.ru):
  - data acquisition (job names, required skills and experience, salaries, work schedule, regions, employers etc.)
  - loading to a dataset
- normalizing acquired data and saving as a CSV-file
- data analysis:
  - reading a CSV-file
  - preliminary processing via NLP
  - determining professional grades (via machine learning in particular)
- data visualization (most in-demand skills relating to IT professions; salaries, number and percentage of jobs relating to IT professions, grades, required experience, work schedule, employers etc.)

The code can be called from a console with ```python3 -m main``` or embedded to another program.
