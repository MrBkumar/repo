import json
import os
import uuid

from django.contrib.admin.utils import NestedObjects
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.text import capfirst
from django.urls.exceptions import NoReverseMatch
from django.utils.timezone import localtime

# -----------------------------------------------------------------------------
import string
import random
from datetime import datetime

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year


def refer_code_generator(num, str1, str2, size=6):
    return f"{str1[:2]}y{currentYear}m{currentMonth}{str2[:2]}c{num}".upper()


def membership_card_generator(num):
    count = num + 1000
    return f"qmc{count}".upper()


def get_upload_to_uuid(self, filename):
    """Rename uploaded file to a unique name."""
    basename = os.path.basename(filename)
    ext = os.path.splitext(basename)[1].lower()
    new_name = uuid.uuid4().hex
    return os.path.join(self.upload_to, new_name + ext)


def get_deleted_objects(objs):
    """Based on `django/contrib/admin/utils.py`"""
    collector = NestedObjects(using="default")
    collector.collect(objs)

    def format_callback(obj):
        opts = obj._meta
        # Display a link to the admin page.
        try:
            return format_html(
                '{}: <a href="{}">{}</a>',
                capfirst(opts.verbose_name),
                # TODO: Is this going to be stable if we use something other than PK, no
                reverse(admin_urlname(opts, "update"), kwargs={"pk": obj.pk}),
                obj,
            )
        except NoReverseMatch:
            pass

        no_edit_link = "%s: %s" % (capfirst(opts.verbose_name), force_text(obj))
        return no_edit_link

    to_delete = collector.nested(format_callback)
    protected = [format_callback(obj) for obj in collector.protected]
    model_count = {
        model._meta.verbose_name_plural: len(objs)
        for model, objs in collector.model_objs.items()
    }

    return to_delete, model_count, protected


def admin_urlname(value, arg):
    """Given model opts (model._meta) and a url name, return a named pattern.
    URLs should be named as: customadmin:app_label:model_name-list"""
    if type(value) != str:
        if value.app_label == "auth":
            pattern = "customadmin:%s:%s-%s" % (value.app_label, value.model_name, arg)
        else:
            pattern = "%s:%s-%s" % ("customadmin", value.model_name, arg)
    else:
        pattern = "%s:%s-%s" % ("customadmin", value, arg)
    return pattern


def human_datetime(dt):
    """Return local time in a human friendly format for consitency."""
    return localtime(dt).strftime("%A, %B %d at %-I:%M %p")
