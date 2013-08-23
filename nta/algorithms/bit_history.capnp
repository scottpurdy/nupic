@0xe8becc7abce77c80

struct BitHistory {

  version @0 :UInt16;

  id @1 :Text;

  stats @2 :List(Float32);

  lastTotalUpdate @3 :UInt32;

  learnIteration @4 :UInt64;

}

struct HistoryList {

  histories @0 :List(BitHistory);

}
