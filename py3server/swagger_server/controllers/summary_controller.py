import connexion
from swagger_server.models import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def linked_types():
    """
    linked_types
    Get a list of types and # of instances in the knowledge source, and a link to the API call for the list of equivalent terminology

    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'
