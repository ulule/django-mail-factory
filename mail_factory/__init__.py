# -*- coding: utf-8 -*-
"""Django Mail Manager"""

pkg_resources = __import__('pkg_resources')
distribution = pkg_resources.get_distribution('mail_factory')

#: Module version, as defined in PEP-0396.
__version__ = distribution.version

from mail_factory.factory import MailFactory

factory = MailFactory()