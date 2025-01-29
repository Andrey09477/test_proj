from enum import Enum

# dataframe columns
class Column(Enum):
    ID = 'id'
    NAME = 'name'
    DESCRIPTION = 'description'
    KEY_SKILLS = 'key_skills'
    EXPERIENCE = 'experience'
    GRADE = 'grade'
    SALARY = 'salary'
    AVG_SALARY = 'avg_salary'
    SALARY_CURRENCY = 'salary_currency'
    SALARY_GROSS = 'salary_gross'
    SALARY_FROM = 'salary_from'
    SALARY_TO = 'salary_to'
    SCHEDULE = 'schedule'
    REGION = 'region'
    AREA = 'area'
    EMPLOYER = 'employer'

# selectable countries (name = 'search filter')
class Country(Enum):
    RUSSIA = 'Россия'
    BELARUS = 'Беларусь'
    KAZAKHSTAN = 'Казахстан'
    UZBEKISTAN = 'Узбекистан'
    KIRGIZSTAN = 'Кыргызстан'
    AZERBAIJAN = 'Азербайджан'
    GEORGIA = 'Грузия'

# wage tax rates of different countries
TAX_RATES = { Country.RUSSIA:0.13,
              Country.BELARUS:0.13,
              Country.KAZAKHSTAN:0.1,
              Country.UZBEKISTAN:0.12,
              Country.KIRGIZSTAN:0.1,
              Country.AZERBAIJAN:0.14,
              Country.GEORGIA:0.2,
            }

# selectable professions { 'name': 'search filter' }
ROLES = { 'Backend developer':'back end',
          'Frontend developer':'front end',
          'Fullstack developer':'full stack',
          'Embedded developer':'embedded',
          'iOS developer':'ios',
          'Android developer':'android',
          'Data analyst':'data analyst',
          'Data engineer':'data engineer',
          'Data scientist':'scientist',
          'QA engineer':'qa',
          'DevOps engineer':'dev ops',
          'System administrator':'sys admin',
          'Information security specialist':'info security',
        }
ROLE_NAMES = tuple(ROLES.keys())
ROLE_TAGS = tuple(ROLES.values())

# specialization
SPEC_NAME = "информационные технологии"

# basic professional grades
GRADES = ('entry', 'junior', 'middle', 'senior', 'principal', 'team lead', 'architect')

# parameters of downloading data via the site API
REQUESTS = { 'spec':'https://api.hh.ru/specializations',
             'regions':'https://api.hh.ru/areas',
             'jobs':'https://api.hh.ru/vacancies',
           }
JOBS_PER_PAGE = 100

ERR_MES = 'Incorrect value'