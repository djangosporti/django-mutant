from __future__ import unicode_literals

SECRET_KEY = 'secret'

INSTALLED_APPS = [
    'django.contrib.auth',  # This is needed because of django bug
    'django.contrib.contenttypes',
    'south',
    'polymodels',
    'mutant',
    'mutant.contrib.boolean',
    'mutant.contrib.temporal',
    'mutant.contrib.file',
    'mutant.contrib.numeric',
    'mutant.contrib.text',
    'mutant.contrib.web',
    'mutant.contrib.related',
]

TEST_RUNNER = 'tests.runners.MutantTestSuiteRunner'
