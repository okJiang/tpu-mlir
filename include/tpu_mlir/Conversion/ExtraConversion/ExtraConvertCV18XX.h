//===----------------------------------------------------------------------===//
//
// Copyright (C) 2022 Sophgo Technologies Inc.  All rights reserved.
//
// TPU-MLIR is licensed under the 2-Clause BSD License except for the
// third-party components.
//
//===----------------------------------------------------------------------===//
#pragma once

#include "tpu_mlir/Dialect/Top/IR/TopOps.h"
#include "mlir/IR/PatternMatch.h"

#include "tpu_mlir/Support/Module.h"
#include <cstdint>

using namespace llvm;

namespace tpu_mlir {

namespace cv18xx {

class ConvertMaskedFillOp : public OpRewritePattern<top::MaskedFillOp> {
public:
  using OpRewritePattern::OpRewritePattern;
  LogicalResult matchAndRewrite(top::MaskedFillOp op,
                                PatternRewriter &rewriter) const override;
};

class ConvertWhereOp : public OpRewritePattern<top::WhereOp> {
public:
  using OpRewritePattern::OpRewritePattern;
  LogicalResult matchAndRewrite(top::WhereOp op,
                                PatternRewriter &rewriter) const override;
};

class ConvertGatherOp : public OpRewritePattern<top::GatherOp> {
public:
  using OpRewritePattern::OpRewritePattern;
  LogicalResult matchAndRewrite(top::GatherOp op,
                                PatternRewriter &rewriter) const override;
};

class ConvertAddConstOp : public OpRewritePattern<top::AddConstOp> {
public:
  using OpRewritePattern::OpRewritePattern;
  LogicalResult matchAndRewrite(top::AddConstOp op,
                                PatternRewriter &rewriter) const override;
};

void populateDoExtraConversionPatterns(RewritePatternSet *patterns);
}
}