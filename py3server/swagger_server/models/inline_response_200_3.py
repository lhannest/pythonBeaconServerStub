# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.statements_object import StatementsObject
from swagger_server.models.statements_predicate import StatementsPredicate
from swagger_server.models.statements_subject import StatementsSubject
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse2003(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, subject: StatementsSubject=None, predicate: StatementsPredicate=None, object: StatementsObject=None):
        """
        InlineResponse2003 - a model defined in Swagger

        :param id: The id of this InlineResponse2003.
        :type id: str
        :param subject: The subject of this InlineResponse2003.
        :type subject: StatementsSubject
        :param predicate: The predicate of this InlineResponse2003.
        :type predicate: StatementsPredicate
        :param object: The object of this InlineResponse2003.
        :type object: StatementsObject
        """
        self.swagger_types = {
            'id': str,
            'subject': StatementsSubject,
            'predicate': StatementsPredicate,
            'object': StatementsObject
        }

        self.attribute_map = {
            'id': 'id',
            'subject': 'subject',
            'predicate': 'predicate',
            'object': 'object'
        }

        self._id = id
        self._subject = subject
        self._predicate = predicate
        self._object = object

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2003':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_3 of this InlineResponse2003.
        :rtype: InlineResponse2003
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this InlineResponse2003.
        CURIE-encoded identifier for statement (can be used to retrieve associated evidence)

        :return: The id of this InlineResponse2003.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this InlineResponse2003.
        CURIE-encoded identifier for statement (can be used to retrieve associated evidence)

        :param id: The id of this InlineResponse2003.
        :type id: str
        """

        self._id = id

    @property
    def subject(self) -> StatementsSubject:
        """
        Gets the subject of this InlineResponse2003.

        :return: The subject of this InlineResponse2003.
        :rtype: StatementsSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject: StatementsSubject):
        """
        Sets the subject of this InlineResponse2003.

        :param subject: The subject of this InlineResponse2003.
        :type subject: StatementsSubject
        """

        self._subject = subject

    @property
    def predicate(self) -> StatementsPredicate:
        """
        Gets the predicate of this InlineResponse2003.

        :return: The predicate of this InlineResponse2003.
        :rtype: StatementsPredicate
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate: StatementsPredicate):
        """
        Sets the predicate of this InlineResponse2003.

        :param predicate: The predicate of this InlineResponse2003.
        :type predicate: StatementsPredicate
        """

        self._predicate = predicate

    @property
    def object(self) -> StatementsObject:
        """
        Gets the object of this InlineResponse2003.

        :return: The object of this InlineResponse2003.
        :rtype: StatementsObject
        """
        return self._object

    @object.setter
    def object(self, object: StatementsObject):
        """
        Sets the object of this InlineResponse2003.

        :param object: The object of this InlineResponse2003.
        :type object: StatementsObject
        """

        self._object = object
