# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


class BaseRenderer:
    Prefix = """
from pynvjitlink.patch import patch_numba_linker
patch_numba_linker()
"""

    Imports: set[str] = set()
    """Empty set to be filled later. One element stands for one line of import."""

    MemoryShimWriterTemplate = """
c_ext_shim_source = CUSource(\"""{shim_funcs}\""")
"""

    includes_template = "#include <{header_path}>"
    """Template for including a header file."""

    Includes: list[str] = []
    """includes to add in c extension shims."""

    def __init__(self, decl):
        self._decl = decl

    def _render_typing(self):
        pass

    def _render_data_model(self):
        pass

    def _render_lowering(self):
        pass

    def _render_decl_device(self):
        pass

    def _render_shim_function(self, decl):
        pass

    def _render_python_api(self):
        pass

    def render(self, path):
        pass
