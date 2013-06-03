# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

import os

from PIL import Image

from nupic.image import imageExtensions


imageDir = os.path.join(os.path.dirname(__file__), 'images')
allImageFiles = [f for f in os.listdir(imageDir)
                 if os.path.splitext(f)[1].lower() in imageExtensions
                 or os.path.splitext(f)[1].lower() == '.ico']
allImageNames = [os.path.splitext(f)[0] for f in allImageFiles]

def getNTAImage(name):
  """Return the path to an image resource."""

  if name in allImageNames:
    return os.path.join(imageDir, allImageFiles[allImageNames.index(name)])
  else:
    return ""

def createDropTargetImage(width, height):
  """Load and prepare a drop target image for the specified size."""

  labelImage = Image.open(getNTAImage('drag_target'))
  dropImage = Image.new('RGBA', (width, height), (128, 128, 128, 255))
  dropImageInterior = Image.new('LA', (width - 5, height - 5), (128, 0))
  dropImage.paste(dropImageInterior, (3, 3))
  dropImage.paste(labelImage, ((width - labelImage.size[0]) / 2,
                               (height - labelImage.size[1]) / 2))
  return dropImage