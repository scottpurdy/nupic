/* ---------------------------------------------------------------------
 *  Copyright (C) 2009-2011 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

#include <nta/utils/Log.hpp>
#include <nta/algorithms/SegmentUpdate.hpp>
#include <nta/algorithms/Cells4.hpp>

using namespace nta::algorithms::Cells4;


SegmentUpdate::SegmentUpdate()
  : _sequenceSegment(false),
    _cellIdx((UInt) -1),
    _segIdx((UInt) -1),
    _timeStamp((UInt) -1),
    _synapses(),
    _phase1Flag(false),
    _weaklyPredicting(false)
{}

SegmentUpdate::SegmentUpdate(UInt cellIdx, UInt segIdx,
                             bool sequenceSegment, UInt timeStamp,
                             const std::vector<UInt>& synapses,
                             bool phase1Flag,
                             bool weaklyPredicting,
                             Cells4* cells)
  : _sequenceSegment(sequenceSegment),
    _cellIdx(cellIdx),
    _segIdx(segIdx),
    _timeStamp(timeStamp),
    _synapses(synapses),
    _phase1Flag(phase1Flag),
    _weaklyPredicting(weaklyPredicting)
{
  NTA_ASSERT(invariants(cells));
}


//--------------------------------------------------------------------------------
SegmentUpdate::SegmentUpdate(const SegmentUpdate& o)
{
  _cellIdx = o._cellIdx;
  _segIdx = o._segIdx;
  _sequenceSegment = o._sequenceSegment;
  _synapses = o._synapses;
  _timeStamp = o._timeStamp;
  _phase1Flag = o._phase1Flag;
  _weaklyPredicting = o._weaklyPredicting;
  NTA_ASSERT(invariants());
}





bool SegmentUpdate::invariants(Cells4* cells) const
{
  bool ok = true;

  if (cells) {

    ok &= _cellIdx < cells->nCells();
    if (_segIdx != (UInt) -1)
      ok &= _segIdx < cells->__nSegmentsOnCell(_cellIdx);

    if (!_synapses.empty()) {
      for (UInt i = 0; i != _synapses.size(); ++i)
        ok &= _synapses[i] < cells->nCells();
      ok &= is_sorted(_synapses, true, true);
    }
  }

  return ok;
}
