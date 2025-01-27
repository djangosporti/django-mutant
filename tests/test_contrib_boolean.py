from __future__ import unicode_literals

import sys

import south
from django.db import connection
from django.utils.translation import ugettext_lazy as _

from mutant.contrib.boolean.models import (
    BooleanFieldDefinition, NullBooleanFieldDefinition,
)
from mutant.test.testcases import FieldDefinitionTestMixin

from .utils import BaseModelDefinitionTestCase

# TODO: Remove when support for Python 2.6 is dropped
if sys.version_info >= (2, 7):
    from unittest import skipIf
else:
    from django.utils.unittest import skipIf


class BooleanFieldDefinitionTestMixin(FieldDefinitionTestMixin):
    field_definition_category = _('Boolean')

    @skipIf(
        connection.settings_dict['ENGINE'] == 'django.db.backends.sqlite3' and
        south.__version__ in ('0.8.1', '0.8.2', '0.8.3', '0.8.4', '1.0', '1.0.1'),
        "This version of South doesn't escape added column default value correctly on SQLite3."
    )
    def test_create_with_default(self):
        super(BooleanFieldDefinitionTestMixin, self).test_create_with_default()


class BooleanFieldDefinitionTest(BooleanFieldDefinitionTestMixin,
                                 BaseModelDefinitionTestCase):
    field_definition_cls = BooleanFieldDefinition
    field_definition_init_kwargs = {'default': True}
    field_values = (False, True)


class NullBooleanFieldDefinitionTest(BooleanFieldDefinitionTestMixin,
                                     BaseModelDefinitionTestCase):
    field_definition_cls = NullBooleanFieldDefinition
    field_values = (True, None)
