# ----------------------------------------------------------------------
#  Copyright (C) 2012 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Simple OPF client."""

from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.frameworks.opf.opfbasicenvironment import BasicDatasetReader
from nupic.frameworks.opf.predictionmetricsmanager import MetricsManager


class Client(object):
  """ Simple OPF client. """

  def __init__(self, modelConfig, inferenceArgs, metricSpecs, sourceSpec,
               sinkSpec=None):
    """Initialization.

    Args:
      modelConfig: The model config dict.
      metricSpecs: A sequence of MetricSpec instances.
      sourceSpec: Path to the source CSV file.
      sinkSpec: Path to the sink CSV file.
    """
    self.model = ModelFactory.create(modelConfig)
    self.model.enableInference(inferenceArgs)
    self.metricsManager = MetricsManager(metricSpecs, self.model.getFieldInfo(),
                                         self.model.getInferenceType())
    self.sink = None
    if sinkSpec is not None:
      # TODO: make this work - sinkSpec not yet supported.
      raise NotImplementedError('The sinkSpec is not yet implemented.')
      #self.sink = BasicPredictionLogger(
      #    self.model.getFieldInfo(), sinkSpec, 'myOutput',
      #    self.model.getInferenceType())
      #self.sink.setLoggedMetrics(
      #    self.metricsManager.getMetricLabels())
    self.datasetReader = BasicDatasetReader(sourceSpec)

  def __iter__(self):
    return self

  def _processRecord(self, inputRecord):
    
    modelResult = self.model.run(inputRecord)
    modelResult.metrics = self.metricsManager.update(modelResult)
    if self.sink:
      self.sink.writeRecord(modelResult)
    return modelResult

  def next(self):
    record = self.datasetReader.next()
    return self._processRecord(record)
    
  def skipNRecords(self, n):
    for i in range(n):
      self.datasetReader.next()
  def nextTruthPrediction(self, field):
    record = self.datasetReader.next()
    prediction=self._processRecord(record).inferences['prediction'][0]
    truth=record[field]
    return truth, prediction
    

  def run(self):
    result = None
    while True:
      try:
        result = self.next()
        #print result
      except StopIteration:
        break
    return result
