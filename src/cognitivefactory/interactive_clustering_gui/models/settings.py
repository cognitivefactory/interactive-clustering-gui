# -*- coding: utf-8 -*-

"""
* Name:         cognitivefactory.interactive_clustering_gui.models.settings
* Description:  Definition of algorithm settings models required for application runs.
* Author:       Erwan Schild
* Created:      16/12/2021
* Licence:      CeCILL-C License v1.0 (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import enum
from typing import Any, Dict, Optional, Union

from pydantic import BaseModel, root_validator, validator

# ==============================================================================
# ENUMERATION OF IC GUI MODELIZATIONS
# ==============================================================================


class ICGUISettings(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available Settings for Interactive Clustering GUI."""

    PREPROCESSING: str = "preprocessing"
    VECTORIZATION: str = "vectorization"
    SAMPLING: str = "sampling"
    CLUSTERING: str = "clustering"

    @classmethod
    def contains(cls, value: Any) -> bool:
        """Test if value is in this enumeration.

        Args:
            value (Any): A value.

        Returns:
            bool: `True` if the value is in the enumeration.
        """
        return value in cls._value2member_map_


# ==============================================================================
# BASE MODEL FOR PREPROCESSING SETTINGS
# ==============================================================================


class PreprocessingSpacyLanguageModel(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available spacy language model name."""

    FR_CORE_NEWS_MD: str = "fr_core_news_md"


class PreprocessingSettingsModel(BaseModel):
    """The body model for preprocessing settings."""

    # Parameters.
    apply_stopwords_deletion: bool
    apply_parsing_filter: bool
    apply_lemmatization: bool
    spacy_language_model: PreprocessingSpacyLanguageModel

    # Export method.
    def to_dict(self) -> Dict[str, Any]:
        """Export the model as a dictionary

        Returns:
            Dict[str, Any]: A dictionary that contains paramaters and their values.
        """
        return {
            "apply_stopwords_deletion": self.apply_stopwords_deletion,
            "apply_parsing_filter": self.apply_parsing_filter,
            "apply_lemmatization": self.apply_lemmatization,
            "spacy_language_model": self.spacy_language_model.value,
        }

    # Config for schema.
    class Config:  # noqa: WPS431 (nested class)
        """Configuration for body model of preprocessing settings."""

        schema_extra = {
            "example": {
                "apply_stopwords_deletion": False,
                "apply_parsing_filter": False,
                "apply_lemmatization": False,
                "spacy_language_model": PreprocessingSpacyLanguageModel.FR_CORE_NEWS_MD,
            }
        }


def default_PreprocessingSettingsModel() -> PreprocessingSettingsModel:
    """Create a PreprocessingSettingsModel instance with default values.

    Returns:
        PreprocessingSettingsModel: A PreprocessingSettingsModel instance with default values.
    """
    return PreprocessingSettingsModel(
        apply_stopwords_deletion=False,
        apply_parsing_filter=False,
        apply_lemmatization=False,
        spacy_language_model=PreprocessingSpacyLanguageModel.FR_CORE_NEWS_MD,
    )


# ==============================================================================
# BASE MODEL FOR VECTORIZATION SETTINGS
# ==============================================================================


class VectorizerType(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available vectorizer type."""

    TFIDF: str = "tfidf"
    SPACY: str = "spacy"


class VectorizationSpacyLanguageModel(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available spacy language model name."""

    FR_CORE_NEWS_MD: str = "fr_core_news_md"


class VectorizationSettingsModel(BaseModel):
    """The body model for vectorization settings."""

    # Parameters.
    vectorizer_type: VectorizerType
    spacy_language_model: Optional[VectorizationSpacyLanguageModel]
    random_seed: int

    @validator("random_seed")
    @classmethod
    def validate_random_seed(cls, value: int) -> int:
        """The validation of random_seed settings.

        Args:
            value (int): The value of random_seed setting.

        Raises:
            ValueError: if `random_seed` is incorrectly set.

        Returns:
            int: The value of random_seed setting.
        """
        if value < 0:
            raise ValueError("`random_seed` must be greater than or equal to 0.")
        return value

    @root_validator
    @classmethod
    def validate_vectorization_settings(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """The validation of vectorization settings.

        Args:
            values (Dict[str, Any]): The values of vectorization settings.

        Raises:
            ValueError: if `vectorizer_type` and `spacy_language_model` are incompatible.

        Returns:
            Dict[str, Any]: The validated values of vectorization settings.
        """

        # Case of no vectorizer.
        if "vectorizer_type" not in values.keys():
            raise ValueError("The parameter `vectorizer_type` is required.")

        # Case of tfidf vectorizer.
        if values["vectorizer_type"] == VectorizerType.TFIDF:
            if ("spacy_language_model" in values.keys()) and (values["spacy_language_model"] is not None):
                raise ValueError("No spacy language model is required when vectorizer is `tfidf`.")
            values["spacy_language_model"] = None

        # Case of spacy vectorizer.
        if values["vectorizer_type"] == VectorizerType.SPACY:
            if ("spacy_language_model" not in values.keys()) or (values["spacy_language_model"] is None):
                raise ValueError("A spacy language model is required when vectorizer is `spacy`.")

        # Return validated values of vectorization settings.
        return values

    # Export method.
    def to_dict(self) -> Dict[str, Any]:
        """Export the model as a dictionary

        Returns:
            Dict[str, Any]: A dictionary that contains paramaters and their values.
        """
        return {
            "vectorizer_type": self.vectorizer_type.value,
            "spacy_language_model": self.spacy_language_model.value
            if (self.spacy_language_model is not None)
            else None,
            "random_seed": self.random_seed,
        }

    # Config for schema.
    class Config:  # noqa: WPS431 (nested class)
        """Configuration for body model of vectorization settings."""

        schema_extra = {
            "example": {
                "vectorizer_type": (VectorizerType.TFIDF + "|" + VectorizerType.SPACY),
                "random_seed": 42,
                "!!!SPECIFIC: 'vectorizer_type'=='spacy'": {
                    "spacy_language_model": VectorizationSpacyLanguageModel.FR_CORE_NEWS_MD,
                },
            }
        }


def default_VectorizationSettingsModel() -> VectorizationSettingsModel:
    """Create a VectorizationSettingsModel instance with default values.

    Returns:
        VectorizationSettingsModel: A VectorizationSettingsModel instance with default values.
    """
    return VectorizationSettingsModel(
        vectorizer_type=VectorizerType.TFIDF,
        spacy_language_model=None,
        random_seed=42,
    )


# ==============================================================================
# BASE MODEL FOR SAMPLING SETTINGS
# ==============================================================================


class SamplingAlgorithm(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available sampling algorithms."""

    RANDOM: str = "random"
    RANDOM_IN_SAME_CLUSTER: str = "random_in_same_cluster"
    FARTHEST_IN_SAME_CLUSTER: str = "farthest_in_same_cluster"
    CLOSEST_IN_DIFFERENT_CLUSTERS: str = "closest_in_different_clusters"
    CUSTOM: str = "custom"


class ClusterRestriction(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available cluster restrictions for custom sampling algorithm."""

    SAME_CLUSTER: str = "same_cluster"
    DIFFERENT_CLUSTERS: str = "different_clusters"


class DistanceRestriction(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available distance restrictions for custom sampling algorithm."""

    CLOSEST_NEIGHBORS: str = "closest_neighbors"
    FARTHEST_NEIGHBORS: str = "farthest_neighbors"


class CustomSamplingInitSettingsModel(BaseModel):
    """The body submodel for custom sampling initialization settings."""

    # Parameters.
    clusters_restriction: ClusterRestriction
    distance_restriction: DistanceRestriction
    without_inferred_constraints: bool

    # Export method.
    def to_dict(self) -> Dict[str, Any]:
        """Export the model as a dictionary

        Returns:
            Dict[str, Any]: A dictionary that contains paramaters and their values.
        """
        return {
            "clusters_restriction": self.clusters_restriction.value,
            "distance_restriction": self.distance_restriction.value,
            "without_inferred_constraints": self.without_inferred_constraints,
        }


class SamplingSettingsModel(BaseModel):
    """Abstract body model for sampling settings."""

    # Parameters.
    algorithm: SamplingAlgorithm
    random_seed: int
    nb_to_select: int
    init_kargs: Optional[CustomSamplingInitSettingsModel]

    @validator("random_seed")
    @classmethod
    def validate_random_seed(cls, value: int) -> int:
        """The validation of random_seed settings.

        Args:
            value (int): The value of random_seed setting.

        Raises:
            ValueError: if `random_seed` is incorrectly set.

        Returns:
            int: The value of random_seed setting.
        """
        if value < 0:
            raise ValueError("`random_seed` must be greater than or equal to 0.")
        return value

    @validator("nb_to_select")
    @classmethod
    def validate_nb_to_select(cls, value: int) -> int:
        """The validation of nb_to_select settings.

        Args:
            value (int): The value of nb_to_select setting.

        Raises:
            ValueError: if `nb_to_select` is incorrectly set.

        Returns:
            int: The value of nb_to_select setting.
        """
        if value < 1:
            raise ValueError("`nb_to_select` must be greater than or equal to 1.")
        return value

    @root_validator
    @classmethod
    def validate_sampling_settings(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """The validation of sampling settings.

        Args:
            values (Dict[str, Any]): The values of sampling settings.

        Raises:
            ValueError: if `algorithm` and `init_kargs` are incompatible.

        Returns:
            Dict[str, Any]: The validated values of sampling settings.
        """

        # Case of no sampling algorithm.
        if "algorithm" not in values.keys():
            raise ValueError("The parameter `algorithm` is required.")

        # Case of custom sampling algorithm.
        if values["algorithm"] == SamplingAlgorithm.CUSTOM:
            if ("init_kargs" not in values.keys()) or (values["init_kargs"] is None):
                raise ValueError(
                    "A dictionary of initialization (`init_kargs`) is required when algorithm is `custom`."
                )

        # Case of predefinite sampling algorithms.
        else:
            if ("init_kargs" in values.keys()) and (values["init_kargs"] is not None):
                raise ValueError(
                    "No dictionary of initialization (`init_kargs`) is required when algorithm is different from `custom`."
                )
            values["init_kargs"] = None

        # Return validated values of sampling settings.
        return values

    # Export method.
    def to_dict(self) -> Dict[str, Any]:
        """Export the model as a dictionary

        Returns:
            Dict[str, Any]: A dictionary that contains paramaters and their values.
        """
        return {
            "algorithm": self.algorithm.value,
            "random_seed": self.random_seed,
            "nb_to_select": self.nb_to_select,
            "init_kargs": self.init_kargs.to_dict() if (self.init_kargs is not None) else None,
        }

    # Config for schema.
    class Config:  # noqa: WPS431 (nested class)
        """Configuration for body model of sampling settings."""

        schema_extra = {
            "example": {
                "algorithm": (
                    SamplingAlgorithm.RANDOM
                    + "|"
                    + SamplingAlgorithm.RANDOM_IN_SAME_CLUSTER
                    + "|"
                    + SamplingAlgorithm.CLOSEST_IN_DIFFERENT_CLUSTERS
                    + "|"
                    + SamplingAlgorithm.FARTHEST_IN_SAME_CLUSTER
                    + "|"
                    + SamplingAlgorithm.CUSTOM
                ),
                "random_seed": 42,
                "nb_to_select": 25,
                "!!!SPECIFIC: 'algorithm'=='custom'": {
                    "init_kargs": {
                        "clusters_restriction": (
                            ClusterRestriction.SAME_CLUSTER + "|" + ClusterRestriction.DIFFERENT_CLUSTERS
                        ),
                        "distance_restriction": (
                            DistanceRestriction.CLOSEST_NEIGHBORS + "|" + DistanceRestriction.FARTHEST_NEIGHBORS
                        ),
                        "without_inferred_constraints": True,
                    },
                },
            }
        }


def default_SamplingSettingsModel() -> SamplingSettingsModel:
    """Create a SamplingSettingsModel instance with default values.

    Returns:
        SamplingSettingsModel: A SamplingSettingsModel instance with default values.
    """
    return SamplingSettingsModel(
        algorithm=SamplingAlgorithm.CLOSEST_IN_DIFFERENT_CLUSTERS,
        random_seed=42,
        nb_to_select=25,
        init_kargs=None,
    )


# ==============================================================================
# BASE MODEL FOR CLUSTERING SETTINGS
# ==============================================================================


class ClusteringAlgorithmEnum(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available clustering algorithms."""

    KMEANS: str = "kmeans"
    HIERARCHICAL: str = "hierarchical"
    SPECTRAL: str = "spectral"


class KmeansModelEnum(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available kmeans models."""

    COP: str = "COP"


class KmeansInitSettingsModel(BaseModel):
    """The body submodel for kmeans instantiation settings."""

    # Parameters.
    model: KmeansModelEnum
    max_iteration: int
    tolerance: float

    @validator("max_iteration")
    @classmethod
    def validate_max_iteration(cls, value: int) -> int:
        """The validation of max_iteration settings.

        Args:
            value (int): The value of max_iteration setting.

        Raises:
            ValueError: if `max_iteration` is incorrectly set.

        Returns:
            int: The value of max_iteration setting.
        """
        if value < 1:
            raise ValueError("`max_iteration` must be greater than or equal to 1.")
        return value

    @validator("tolerance")
    @classmethod
    def validate_tolerance(cls, value: float) -> float:
        """The validation of tolerance settings.

        Args:
            value (float): The value of tolerance setting.

        Raises:
            ValueError: if `tolerance` is incorrectly set.

        Returns:
            float: The value of tolerance setting.
        """
        if value < 0:
            raise ValueError("The `tolerance` must be greater than 0.0.")
        return value

    # Export method.
    def to_dict(self) -> Dict[str, Any]:
        """Export the model as a dictionary

        Returns:
            Dict[str, Any]: A dictionary that contains paramaters and their values.
        """
        return {
            "model": self.model.value,
            "max_iteration": self.max_iteration,
            "tolerance": self.tolerance,
        }


def default_KmeansInitSettingsModel() -> KmeansInitSettingsModel:
    """Create a KmeansInitSettingsModel instance with default values.

    Returns:
        KmeansInitSettingsModel: A KmeansInitSettingsModel instance with default values.
    """
    return KmeansInitSettingsModel(
        model=KmeansModelEnum.COP,
        max_iteration=150,
        tolerance=0.0001,
    )


class HierarchicalLinkageEnum(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available hierarchical linkages."""

    AVERAGE: str = "average"
    COMPLETE: str = "complete"
    SINGLE: str = "single"
    WARD: str = "ward"


class HierarchicalInitSettingsModel(BaseModel):
    """The body submodel for hierarchical instantiation settings."""

    # Parameters.
    linkage: HierarchicalLinkageEnum

    # Export method.
    def to_dict(self) -> Dict[str, Any]:
        """Export the model as a dictionary

        Returns:
            Dict[str, Any]: A dictionary that contains paramaters and their values.
        """
        return {
            "linkage": self.linkage.value,
        }


# NEVER USE: KMeans is used as default clustering algorithm.
#### def default_HierarchicalInitSettingsModel() -> HierarchicalInitSettingsModel:
####    """Create a HierarchicalInitSettingsModel instance with default values.
####
####    Returns:
####        HierarchicalInitSettingsModel: A HierarchicalInitSettingsModel instance with default values.
####    """
####    return HierarchicalInitSettingsModel(
####        linkage=HierarchicalLinkageEnum.WARD,
####    )


class SpectralModelEnum(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available spectral models."""

    SPEC: str = "SPEC"


class SpectralInitSettingsModel(BaseModel):
    """The body submodel for spectral instantiation settings."""

    # Parameters.
    model: SpectralModelEnum = SpectralModelEnum.SPEC
    nb_components: Optional[int] = None

    @validator("nb_components")
    @classmethod
    def validate_nb_components(cls, value: Optional[int]) -> Optional[int]:
        """The validation of nb_components settings.

        Args:
            value (Optional[int]): The value of nb_components setting.

        Raises:
            ValueError: if `nb_components` is incorrectly set.

        Returns:
            Optional[int]: The value of nb_components setting.
        """
        if (value is not None) and (value < 2):
            raise ValueError("`nb_components` must be `None` or greater than or equal to 2.")
        return value

    # Export method.
    def to_dict(self) -> Dict[str, Any]:
        """Export the model as a dictionary

        Returns:
            Dict[str, Any]: A dictionary that contains paramaters and their values.
        """
        return {
            "model": self.model.value,
            "nb_components": self.nb_components,
        }


# NEVER USE: KMeans is used as default clustering algorithm.
#### def default_SpectralInitSettingsModel() -> SpectralInitSettingsModel:
####    """Create a SpectralInitSettingsModel instance with default values.
####
####    Returns:
####        SpectralInitSettingsModel: A SpectralInitSettingsModel instance with default values.
####    """
####    return SpectralInitSettingsModel(
####        model=SpectralModelEnum.SPEC,
####        nb_components=None,
####    )


class ClusteringSettingsModel(BaseModel):
    """The body model for clustering settings."""

    # Parameters.
    algorithm: ClusteringAlgorithmEnum
    random_seed: int
    nb_clusters: int
    init_kargs: Union[None, KmeansInitSettingsModel, HierarchicalInitSettingsModel, SpectralInitSettingsModel]

    @validator("random_seed")
    @classmethod
    def validate_random_seed(cls, value: int) -> int:
        """The validation of random_seed settings.

        Args:
            value (int): The value of random_seed setting.

        Raises:
            ValueError: if `random_seed` is incorrectly set.

        Returns:
            int: The value of random_seed setting.
        """
        if value < 0:
            raise ValueError("`random_seed` must be greater than or equal to 0.")
        return value

    @validator("nb_clusters")
    @classmethod
    def validate_nb_clusters(cls, value: int) -> int:
        """The validation of nb_clusters settings.

        Args:
            value (int): The value of nb_clusters setting.

        Raises:
            ValueError: if `nb_clusters` is incorrectly set.

        Returns:
            int: The value of nb_clusters setting.
        """
        if value < 2:
            raise ValueError("`nb_clusters` must be greater than or equal to 2.")
        return value

    @root_validator
    @classmethod
    def validate_clustering_settings(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """The validation of clustering settings.

        Args:
            values (Dict[str, Any]): The values of clustering settings.

        Raises:
            ValueError: if `algorithm` and `init_kargs` are incompatible.

        Returns:
            Dict[str, Any]: The validated values of clustering settings.
        """

        # Case of no clustering algorithm.
        if "algorithm" not in values.keys():
            raise ValueError("The parameter `algorithm` is required.")

        # Case of kmeans clustering algorithm.
        if values["algorithm"] == ClusteringAlgorithmEnum.KMEANS:
            # Case of no init parameters.
            if ("init_kargs" not in values.keys()) or (values["init_kargs"] is None):
                raise ValueError(
                    "A dictionary of initialization (`init_kargs`) is required when algorithm is `kmeans`."
                )
            # Case of wrong type init parameters.
            if not isinstance(values["init_kargs"], KmeansInitSettingsModel):
                raise ValueError(
                    "The dictionary of initialization (`init_kargs`) is incompatible with algorithm `kmeans`."
                )

        # Case of hierarchical clustering algorithm.
        if values["algorithm"] == ClusteringAlgorithmEnum.HIERARCHICAL:
            # Case of no init parameters.
            if ("init_kargs" not in values.keys()) or (values["init_kargs"] is None):
                raise ValueError(
                    "A dictionary of initialization (`init_kargs`) is required when algorithm is `hierarchical`."
                )
            # Case of wrong type init parameters.
            if not isinstance(values["init_kargs"], HierarchicalInitSettingsModel):
                raise ValueError(
                    "The dictionary of initialization (`init_kargs`) is incompatible with algorithm `hierarchical`."
                )

        # Case of spectral clustering algorithm.
        if values["algorithm"] == ClusteringAlgorithmEnum.SPECTRAL:
            # Case of no init parameters.
            if ("init_kargs" not in values.keys()) or (values["init_kargs"] is None):
                raise ValueError(
                    "A dictionary of initialization (`init_kargs`) is required when algorithm is `spectral`."
                )
            # Case of wrong type init parameters.
            if not isinstance(values["init_kargs"], SpectralInitSettingsModel):
                raise ValueError(
                    "The dictionary of initialization (`init_kargs`) is incompatible with algorithm `spectral`."
                )

        # Return validated values of sampling settings.
        return values

    # Export method.
    def to_dict(self) -> Dict[str, Any]:
        """Export the model as a dictionary

        Returns:
            Dict[str, Any]: A dictionary that contains paramaters and their values.
        """
        return {
            "algorithm": self.algorithm.value,
            "random_seed": self.random_seed,
            "nb_clusters": self.nb_clusters,
            "init_kargs": self.init_kargs.to_dict() if (self.init_kargs is not None) else {},
        }

    # Config for schema.
    class Config:  # noqa: WPS431 (nested class)
        """Configuration for body model of clustering settings."""

        schema_extra = {
            "example": {
                "algorithm": (
                    ClusteringAlgorithmEnum.KMEANS
                    + "|"
                    + ClusteringAlgorithmEnum.HIERARCHICAL
                    + "|"
                    + ClusteringAlgorithmEnum.SPECTRAL
                ),
                "random_seed": 42,
                "nb_clusters": 2,
                "init_kargs": {
                    "!!!SPECIFIC: 'algorithm'=='kmeans'": {
                        "model": KmeansModelEnum.COP,
                        "max_iteration": 150,
                        "tolerance": 0.0001,
                    },
                    "!!!SPECIFIC: 'algorithm'=='hierarchical'": {
                        "linkage": (
                            HierarchicalLinkageEnum.WARD
                            + "|"
                            + HierarchicalLinkageEnum.AVERAGE
                            + "|"
                            + HierarchicalLinkageEnum.COMPLETE
                            + "|"
                            + HierarchicalLinkageEnum.SINGLE
                        ),
                    },
                    "!!!SPECIFIC: 'algorithm'=='spectral'": {
                        "model": SpectralModelEnum.SPEC,
                        "nb_components": None,
                    },
                },
            }
        }


def default_ClusteringSettingsModel() -> ClusteringSettingsModel:
    """Create a ClusteringSettingsModel instance with default values.

    Returns:
        ClusteringSettingsModel: A ClusteringSettingsModel instance with default values.
    """
    return ClusteringSettingsModel(
        algorithm=ClusteringAlgorithmEnum.KMEANS,
        random_seed=42,
        nb_clusters=2,
        init_kargs=default_KmeansInitSettingsModel(),
    )
