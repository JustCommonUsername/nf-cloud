# std imports
from typing import Dict, Any

# 3rd party imports
from peewee import (
    BigAutoField,
    CharField,
    TextField,
    BooleanField
)
from playhouse.postgres_ext import JSONField

# internal import
from nf_cloud_backend import db_wrapper as db

class Workflow(db.Model):
    id = BigAutoField(primary_key=True)
    name = CharField(max_length=512, null=False)
    description = TextField(null=False)
    definition = JSONField()
    is_validated = BooleanField(null=False, default=False)
    is_published = BooleanField(null=False, default=False)

    class Meta:
        db_table = "workflows"


    def to_dict(self) -> Dict[str, any]:
        """
        Returns dictionary representations

        Returns
        -------
        Dict[str, any]
            Dictionary representation
        """
        return {
            "id": self.id,
            "name": self.name,
            "definition": self.definition,
            "description": self.description,
            "is_published": self.is_published,
            "is_validated": self.is_validated
        }