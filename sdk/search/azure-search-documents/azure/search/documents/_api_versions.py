# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ApiVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    #: this is the default version
    V2020_06_30 = "2020-06-30"
    V2023_10_01_PREVIEW = "2023-10-01-Preview"
    V2023_11_01 = "2023-11-01"


DEFAULT_VERSION = ApiVersion.V2023_10_01_PREVIEW
