@0xb85e1e011c121de1

struct SpatialPooler {
  columns @0 :List(Column);
  numInputBits @1 :UInt32;
}

struct Column {
  inputBitPool @0 :List(UInt16);
  inputBitWeights @1 :List(Float32);
}
