#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from soma import aims

extensions = [ ( '.ima', '.dim' ), ( '.nii', ), ( '.img', '.hdr' ),
  ( '.vimg', '.vhdr', '.vinfo' ) ]

if len( sys.argv ) != 2 or sys.argv[1] in ( '-h', '--help' ):
  print 'usage:', sys.argv[0], '<directory>'
  print 'Recursively replaces .ima/.dim, .nii, .img/.hdr and other ' \
    'uncompressed formats images by .nii.gz compressed volumes'
  sys.exit(1)

directory = sys.argv[1]

dirs = [ directory ]

while len( dirs ) != 0:
  directory = dirs.pop()
  for f in os.listdir( directory ):
    fp = os.path.join( directory, f )
    if os.path.isdir( fp ):
      dirs.append( fp )
    else:
      exts = [ fp.endswith( ext[0] ) for ext in extensions ]
      if filter( None, exts ):
        iext = exts.index( True )
        b = fp[ :len(fp)-len(extensions[iext][0]) ]
        ofp = b + '.nii.gz'
        print 'replace', fp, 'by', ofp
        rmfiles = [ b + ext for ext in extensions[iext] ]
        rmfiles.append( rmfiles[0] + '.minf' )
        rmfiles = [ x for x in rmfiles if os.path.exists( x ) ]
        if os.path.exists( ofp ):
          print 'already exists.'
        else:
          vol = aims.read( fp )
          aims.write( vol, ofp )
        for x in rmfiles:
          os.unlink( x )

