# Django RestAPi example

We've included a tiny Django web app which is a wiki(-ish) of UK companies and their employees. There's currently no front end views, and everything is getting created, updated and deleted through the admin.

We want you to extend this app by implementing the following:

- Create an API end point which allows authenticated users (no need to handle API keys, just assume they're logged in) to pass in the id of a company to monitor.
- Create an API end point which allows authenticated users to see which companies they're currently monitoring.
- Create an unauthenticated API end point which returns some top level stats (pick a few of these):

    * The 10 most recently founded companies
    * Average employee count
    * Breakdown of number of companies founded per quarter for the last five years
    * User who has created the most companies
    * User with the greatest total number of employees at all companies they have created
    * Average deal amount raised by country (i.e. deals for companies in those countries)
    * Any other ideas you think may be interesting

- Create a frontend interface to this API, displaying and visualising these stats. You can build this however you like - see the `company_stats.html` template for a very basic prototype.

Feel free to use an API framework if you like or just follow the style of our simple `company_stats` endpoint.

Also feel free to make any other changes or improvements that you think are necessary.

Could you also please use either Mercurial (which we use at Beauhurst) or Git so we can see your workflow.

We'd like you to spend around 2-3 hours on this, so appreciate you won't be able to get through everything, please come prepared to talk through your end result, workflow and anything you learnt in the process.

## Installation

1. Clone the repo
2. Set up a virtual env or equivalent to isolate your environment: `mkvirtualenv -p python3 beauhurst_assessment`
3. Install the requirements: `python -m pip install -r requirements.txt`
4. `./manage.py migrate`
5. `./manage.py loaddata beauhurst_assessment/fixtures.json` or `./manage.py populate_database`
6. `./manage.py createsuperuser`
7. `./manage.py runserver 0.0.0.0:8000`

## Testing

If testing is your thing, then 👍 we've set this repo up so you can use Django's builtin `unittest` or `pytest`, and we've set up `factory_boy` to help with some of the boilerplate to get you started.

## References

- https://virtualenvwrapper.readthedocs.io
- https://docs.djangoproject.com/en/1.11/topics/testing/
- https://docs.pytest.org
- https://pytest-django.readthedocs.io
- https://faker.readthedocs.io
- http://flake8.pycqa.org
