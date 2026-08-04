import os
import json
import logging
from abc import ABC, abstractmethod
from typing import Optional
from backend.models.audit import AuditContext
from backend.config import AUDIT_STORE_DIR

logger = logging.getLogger("MerchSage.AuditStore")

class AuditStore(ABC):
    @abstractmethod
    def save_context(self, context: AuditContext) -> None:
        pass

    @abstractmethod
    def load_context(self, audit_id: str) -> Optional[AuditContext]:
        pass

class LocalJsonAuditStore(AuditStore):
    def __init__(self):
        self.directory = AUDIT_STORE_DIR

    def save_context(self, context: AuditContext) -> None:
        file_path = os.path.join(self.directory, f"{context.audit_id}.json")
        try:
            with open(file_path, "w") as f:
                f.write(context.model_dump_json(indent=2))
            logger.info(f"Successfully saved audit context to {file_path}")
        except Exception as e:
            logger.error(f"Failed to save audit context to file: {e}")
            raise e

    def load_context(self, audit_id: str) -> Optional[AuditContext]:
        file_path = os.path.join(self.directory, f"{audit_id}.json")
        if not os.path.exists(file_path):
            logger.warning(f"Audit file not found: {file_path}")
            return None
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            return AuditContext(**data)
        except Exception as e:
            logger.error(f"Failed to load audit context from file: {e}")
            return None
