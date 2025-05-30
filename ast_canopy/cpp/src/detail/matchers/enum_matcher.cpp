// clang-format off
// SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// clang-format on

#include "matchers.hpp"

namespace ast_canopy {

namespace detail {

EnumCallback::EnumCallback(traverse_ast_payload *payload) : payload(payload) {
  payload->decls->enums.clear();
}

void EnumCallback::run(const MatchFinder::MatchResult &Result) {
  const EnumDecl *ED = Result.Nodes.getNodeAs<clang::EnumDecl>("enum");
  std::string file_name = source_filename_from_decl(ED);

  if (std::any_of(payload->files_to_retain->begin(),
                  payload->files_to_retain->end(),
                  [&file_name](const std::string &file_to_retain) {
                    return file_name == file_to_retain;
                  }))

  {

    payload->decls->enums.push_back(Enum(ED));
  }
}

} // namespace detail

} // namespace ast_canopy
