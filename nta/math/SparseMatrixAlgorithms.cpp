/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2009 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

/** @file 
 * External algorithms for operating on a sparse matrix.
 */

#include <nta/math/SparseMatrix.hpp>
#include <nta/math/SparseMatrixAlgorithms.hpp>

/**
 * This file contains the declarations for the two static tables that we compute
 * to speed-up log sum and log diff.
 */

namespace nta {

  // The two tables used when approximating logSum and logDiff.
  std::vector<LogSumApprox::value_type> LogSumApprox::table;
  std::vector<LogDiffApprox::value_type> LogDiffApprox::table;

} // end namespace nta

