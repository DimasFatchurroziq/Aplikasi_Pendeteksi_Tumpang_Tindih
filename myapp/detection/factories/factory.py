from detection.repositories.file_repository import FileRepository
from detection.repositories.rule_repository import RuleRepository
from detection.repositories.embedding_repository import EmbeddingRepository
from detection.repositories.comparison_repository import ComparisonRepository
# from detection.repositories.sementara_repository import SementaraRepository

from detection.services.embedding_service import EmbeddingService
from detection.services.file_service import FileService
from detection.services.rule_service import RuleService
from detection.services.comparison_service import ComparisonService
from detection.services.sementara_service import SementaraService

def get_file_service():
    repository = FileRepository()
    return FileService(repository)

def get_rule_service():
    repository = RuleRepository()
    return RuleService(repository)

def get_embedding_service():
    repository = EmbeddingRepository()
    return EmbeddingService(repository)

def get_comparison_service():
    repository = ComparisonRepository()
    return ComparisonService(repository)

def get_sementara_service():
    # repository = SementaraRepository()
    return SementaraService()