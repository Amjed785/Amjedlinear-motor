#! Preflu2D 11.2
newProject()


lastInstance = ParameterGeom(name='PI',
              expression='acos(-1)')

lastInstance = ParameterGeom(name='POLES : number of poles',
              expression='8')

lastInstance = ParameterGeom(name='SLOTS : number of the slots',
              expression='9')

lastInstance = ParameterGeom(name='AIRGAP : width of the airgap',
              expression='1')

lastInstance = ParameterGeom(name='H_MAGNET_BACK : height of the magnet back',
              expression='12')

lastInstance = ParameterGeom(name='H_MAGNET : height of the magnets',
              expression='5')

lastInstance = ParameterGeom(name='W_MAGNET : width of the magnets',
              expression='19')

lastInstance = ParameterGeom(name='MAGNET_DISTANCE : width of the magnets spacing',
              expression='8')

lastInstance = ParameterGeom(name='POLE_PITCH : width of the magnets spacing',
              expression='(W_MAGNET+MAGNET_DISTANCE)')

lastInstance = ParameterGeom(name='LENGTH : width of the magnets spacing',
              expression='(POLES*POLE_PITCH)')

lastInstance = ParameterGeom(name='H_SLOT : slot height',
              expression='25')

lastInstance = ParameterGeom(name='W_SLOT : slot width',
              expression='13')

lastInstance = ParameterGeom(name='W_TOOTH : tooth width',
              expression='11')

lastInstance = ParameterGeom(name='SLOT_PITCH : width of the magnets spacing',
              expression='(W_SLOT+W_TOOTH)')

lastInstance = ParameterGeom(name='H_STATOR_BACK : height of the stator back',
              expression='12')

lastInstance = ParameterGeom(name='LAYER : number of conccentrated winding layers',
              expression='2')

lastInstance = ParameterGeom(name='mu_r : relative permeability',
              expression='1.05')

lastInstance = ParameterGeom(name='Br : remanent flux density',
              expression='1.23')






lastInstance = CoordSysCartesian(name='MAGNET_BACK : magnet mack iron bottom coordinate system',
                  parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
                                             angleUnit=AngleUnit['DEGREE']),
                  origin=['0',
                          '0'],
                  rotationAngles=RotationAngles(angleZ='0'))


lastInstance = CoordSysCartesian(name='MAGNET',
                  parentCoordSys=Local(coordSys=CoordSys['XY1']),
                  origin=['0',
                          'H_MAGNET_BACK'],
                  rotationAngles=RotationAngles(angleZ='0'),
                  visibility=Visibility['VISIBLE'])

lastInstance = CoordSysCartesian(name='MAGNET_S',
                  parentCoordSys=Local(coordSys=CoordSys['XY1']),
                  origin=['0',
                          'H_MAGNET_BACK'],
                  rotationAngles=RotationAngles(angleZ='180'),
                  visibility=Visibility['VISIBLE'])



lastInstance = CoordSysCartesian(name='AIRGAP_1 : airgap_1 bottom coordinate system',
                  parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
                                             angleUnit=AngleUnit['DEGREE']),
                  origin=['0',
                          'H_MAGNET_BACK+H_MAGNET'],
                  rotationAngles=RotationAngles(angleZ='0'))


lastInstance = CoordSysCartesian(name='AIRGAP_2 : airgap_2 bottom coordinate system',
                  parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
                                             angleUnit=AngleUnit['DEGREE']),
                  origin=['0',
                          'H_MAGNET_BACK+H_MAGNET+0.9*AIRGAP'],
                  rotationAngles=RotationAngles(angleZ='0'))


lastInstance = CoordSysCartesian(name='SLOTS : slot bottom coordinate system',
                  parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
                                             angleUnit=AngleUnit['DEGREE']),
                  origin=['0',
                          'H_MAGNET_BACK+H_MAGNET+AIRGAP'],
                  rotationAngles=RotationAngles(angleZ='0'))


lastInstance = CoordSysCartesian(name='STATOR_BACK : stator back iron bottom coordinate system',
                  parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
                                             angleUnit=AngleUnit['DEGREE']),
                  origin=['0',
                          'H_MAGNET_BACK+H_MAGNET+AIRGAP+H_SLOT'],
                  rotationAngles=RotationAngles(angleZ='0'))



lastInstance = PeriodicityTranslationX(physicalType=PeriodicityCyclicType(),
                        lengthPosition=['(SLOTS*(W_TOOTH+W_SLOT))',
                                        '0'])




lastInstance = MeshPoint(name='VERY_LARGE_MESH : large mesh size',
          lengthUnit=LengthUnit['MILLIMETER'],
          value='9',
          color=Color['Cyan'])

lastInstance = MeshPoint(name='LARGE_MESH : large mesh size',
          lengthUnit=LengthUnit['MILLIMETER'],
          value='7',
          color=Color['Cyan'])


lastInstance = MeshPoint(name='MEDIUM_MESH : medium mesh size',
          lengthUnit=LengthUnit['MILLIMETER'],
          value='3',
          color=Color['Cyan'])


lastInstance = MeshPoint(name='SMALL_MESH : small mesh size',
          lengthUnit=LengthUnit['MILLIMETER'],
          value='0.5',
          color=Color['Cyan'])








lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET_BACK'],
                 uvw=['0',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET_BACK'],
                 uvw=['LENGTH',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['0',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['W_MAGNET+POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['2*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['2*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['3*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['3*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['4*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['4*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['5*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['5*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['6*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['6*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['7*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['7*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET'],
                 uvw=['LENGTH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['0',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['W_MAGNET+POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['2*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['2*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['3*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['3*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['4*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['4*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['5*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['5*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['6*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['6*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['7*POLE_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['7*POLE_PITCH+W_MAGNET',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_1'],
                 uvw=['LENGTH',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_2'],
                 uvw=['0',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['AIRGAP_2'],
                 uvw=['LENGTH',
                      '0'],
                 nature=Nature['STANDARD'])










lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['0',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['2*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['2*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['2*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['3*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['3*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['3*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['4*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['4*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['4*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['5*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['5*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['5*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['6*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['6*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['6*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['7*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['7*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['7*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['8*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['8*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['8*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['SLOTS'],
                 uvw=['LENGTH',
                      '0'],
                 nature=Nature['STANDARD'])





lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['0',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['2*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['2*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['2*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['3*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['3*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['3*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['4*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['4*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['4*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['5*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['5*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['5*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['6*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['6*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['6*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['7*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['7*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['7*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['8*SLOT_PITCH',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['8*SLOT_PITCH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['8*SLOT_PITCH+W_TOOTH+W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['LENGTH',
                      '0'],
                 nature=Nature['STANDARD'])




lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['0',
                      'H_STATOR_BACK'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['LENGTH',
                      'H_STATOR_BACK'],
                 nature=Nature['STANDARD'])





lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET_BACK'],
                 uvw=['0',
                      '-2*(H_magnet_back)'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MAGNET_BACK'],
                 uvw=['LENGTH',
                      '-2*(H_magnet_back)'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['0',
                      '(2*H_magnet_back+H_STATOR_BACK)'],
                 nature=Nature['STANDARD'])


lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['STATOR_BACK'],
                 uvw=['LENGTH',
                      '(2*H_magnet_back+H_STATOR_BACK)'],
                 nature=Nature['STANDARD'])









lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[1],
                      Point[2]],
            nature=Nature['STANDARD'])



lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[3],
                      Point[4]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[4],
                      Point[5]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[5],
                      Point[6]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[6],
                      Point[7]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[7],
                      Point[8]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[8],
                      Point[9]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[9],
                      Point[10]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[10],
                      Point[11]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[11],
                      Point[12]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[12],
                      Point[13]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[13],
                      Point[14]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[14],
                      Point[15]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[15],
                      Point[16]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[16],
                      Point[17]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[17],
                      Point[18]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[18],
                      Point[19]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[20],
                      Point[21]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[21],
                      Point[22]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[22],
                      Point[23]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[23],
                      Point[24]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[24],
                      Point[25]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[25],
                      Point[26]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[26],
                      Point[27]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[27],
                      Point[28]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[28],
                      Point[29]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[29],
                      Point[30]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[30],
                      Point[31]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[31],
                      Point[32]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[32],
                      Point[33]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[33],
                      Point[34]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[34],
                      Point[35]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[35],
                      Point[36]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[37],
                      Point[38]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[39],
                      Point[40]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[40],
                      Point[41]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[41],
                      Point[42]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[42],
                      Point[43]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[43],
                      Point[44]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[44],
                      Point[45]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[45],
                      Point[46]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[46],
                      Point[47]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[47],
                      Point[48]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[48],
                      Point[49]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[49],
                      Point[50]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[50],
                      Point[51]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[51],
                      Point[52]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[52],
                      Point[53]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[53],
                      Point[54]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[54],
                      Point[55]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[55],
                      Point[56]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[56],
                      Point[57]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[57],
                      Point[58]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[58],
                      Point[59]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[59],
                      Point[60]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[60],
                      Point[61]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[61],
                      Point[62]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[62],
                      Point[63]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[63],
                      Point[64]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[64],
                      Point[65]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[65],
                      Point[66]],
            nature=Nature['STANDARD'])





lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[67],
                      Point[68]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[68],
                      Point[69]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[69],
                      Point[70]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[70],
                      Point[71]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[71],
                      Point[72]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[72],
                      Point[73]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[73],
                      Point[74]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[74],
                      Point[75]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[75],
                      Point[76]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[76],
                      Point[77]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[77],
                      Point[78]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[78],
                      Point[79]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[79],
                      Point[80]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[80],
                      Point[81]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[81],
                      Point[82]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[82],
                      Point[83]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[83],
                      Point[84]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[84],
                      Point[85]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[85],
                      Point[86]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[86],
                      Point[87]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[87],
                      Point[88]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[88],
                      Point[89]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[89],
                      Point[90]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[90],
                      Point[91]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[91],
                      Point[92]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[92],
                      Point[93]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[93],
                      Point[94]],
            nature=Nature['STANDARD'])



lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[95],
                      Point[96]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[97],
                      Point[98]],
            nature=Nature['STANDARD'])



lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[99],
                      Point[100]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[97],
                      Point[1]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[1],
                      Point[3]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[3],
                      Point[20]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[20],
                      Point[37]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[37],
                      Point[39]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[39],
                      Point[67]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[67],
                      Point[95]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[95],
                      Point[99]],
            nature=Nature['STANDARD'])
            
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[98],
                      Point[2]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[2],
                      Point[19]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[19],
                      Point[36]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[36],
                      Point[38]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[38],
                      Point[66]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[66],
                      Point[94]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[94],
                      Point[96]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[96],
                      Point[100]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[65],
                      Point[93]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[64],
                      Point[92]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[63],
                      Point[91]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[62],
                      Point[90]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[61],
                      Point[89]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[60],
                      Point[88]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[59],
                      Point[87]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[58],
                      Point[86]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[57],
                      Point[85]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[56],
                      Point[84]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[55],
                      Point[83]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[54],
                      Point[82]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[53],
                      Point[81]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[52],
                      Point[80]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[51],
                      Point[79]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[50],
                      Point[78]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[49],
                      Point[77]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[48],
                      Point[76]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[47],
                      Point[75]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[46],
                      Point[74]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[45],
                      Point[73]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[44],
                      Point[72]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[43],
                      Point[71]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[42],
                      Point[70]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[41],
                      Point[69]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[40],
                      Point[68]],
            nature=Nature['STANDARD'])


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[18],
                      Point[35]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[17],
                      Point[34]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[16],
                      Point[33]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[15],
                      Point[32]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[14],
                      Point[31]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[13],
                      Point[30]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[12],
                      Point[29]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[11],
                      Point[28]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[10],
                      Point[27]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[9],
                      Point[26]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[8],
                      Point[25]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[7],
                      Point[24]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[6],
                      Point[23]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[5],
                      Point[22]],
            nature=Nature['STANDARD'])
            

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[4],
                      Point[21]],
            nature=Nature['STANDARD'])
            






lastInstance = TransfTranslationVector(name='SIDE_LINK',
                        coordSys=CoordSys['MAGNET_BACK'],
                        vector=['LENGTH',
                                '0'])

lastInstance = MeshLineLinked(name='SIDE_LINK_line',
               color=Color['Red'],
               linked=Transf['SIDE_LINK'])

Line[100,101,102,103,104,105,106,107].assignMeshLine(meshLine=MeshLine['SIDE_LINK_line'])


PointCoordinates[99,100,98,97].assignMeshPoint(meshPoint=MeshPoint['VERY_LARGE_MESH'])

PointCoordinates[95,96,2,1].assignMeshPoint(meshPoint=MeshPoint['LARGE_MESH'])

PointCoordinates[67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3].assignMeshPoint(meshPoint=MeshPoint['MEDIUM_MESH'])

PointCoordinates[20,39,37,40,41,21,42,22,43,44,23,45,24,46,47,48,25,49,26,50,51,27,52,28,53,54,29,55,30,56,57,58,31,32,59,60,61,33,62,34,63,64,35,65,36,38,66].assignMeshPoint(meshPoint=MeshPoint['SMALL_MESH'])



buildFaces()


meshLines()

meshFaces()


saveProjectAs('E:/Flux_dir/PMLSM/PML_1.FLU')

