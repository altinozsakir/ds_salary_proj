import pandas as pd 
import glassdoor_scraper as gs 

proj_path = '/home/altinoz/projects/ds_salary_proj/'



df = gs.get_jobs('data scientist',15,False,proj_path + 'chromedriver',15)

df