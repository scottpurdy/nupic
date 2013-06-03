/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2010 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
*/

/** @file
 * UniformLinkPolicy unit tests
 */

#ifndef NTA_UNIFORM_LINK_POLICY_TEST_HPP
#define NTA_UNIFORM_LINK_POLICY_TEST_HPP

//----------------------------------------------------------------------

#include <nta/test/Tester.hpp>
#include <nta/ntypes/Dimensions.hpp>
#include <nta/types/Fraction.hpp>

//----------------------------------------------------------------------

namespace nta {

  struct UniformLinkPolicyTest : public Tester
  {
    virtual ~UniformLinkPolicyTest() {}
    virtual void RunTests();

  private:

    enum LinkSide
    {
      srcLinkSide,
      destLinkSide
    };

    struct CoordBounds
    {
      Coordinate coord;
      size_t dimension;
      std::pair<Fraction, Fraction> bounds;

      CoordBounds(Coordinate c, size_t dim, std::pair<Fraction, Fraction> b) :
        coord(c),
        dimension(dim),
        bounds(b)
      {
      }
    };

    Coordinate makeCoordinate(size_t x, size_t y);

    bool setAndCheckDimensions(LinkSide setLinkSide,
                               Dimensions setDimensions,
                               Dimensions checkDimensions,
                               std::string linkParams,
                               size_t elementCount = 1);

    bool setDimensionsAndCheckBounds(LinkSide setLinkSide,
                                     Dimensions setDimensions,
                                     std::vector<CoordBounds> checkBoundsVec,
                                     std::string linkParams,
                                     size_t elementCount = 1);
  };
}

#endif // NTA_UNIFORM_LINK_POLICY_TEST_HPP
