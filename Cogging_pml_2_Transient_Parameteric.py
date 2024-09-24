#! Preflu2D 11.2
loadProject('PML_1_Parameteric.FLU')

lastInstance = ApplicationMagneticTransient2D(domain2D=Domain2DPlane(lengthUnit=LengthUnit['MILLIMETER'],
                                                      depth='100'),
                               coilCoefficient=CoilCoefficientAutomatic(),
                               transientInitialization=TransientInitializationZeroInitialSolution())

Application[2].transientInitialization=TransientInitializationStaticComputation()


importMaterial(fileName='D:/Instaled_programs/Cedrat/Materials/FLUX_111_MATERI.DAT', materialNames=['FLU_M270_35A         :'])
importMaterial(fileName='D:/Instaled_programs/Cedrat/Materials/FLUX_111_MATERI.DAT', materialNames=['FLU_M600_50A         :'])
lastInstance = Material(name='Infinite_Permeability',
         propertyBH=PropertyBhLinear(mur='1000000'))

importMaterial(fileName='D:/Instaled_programs/Cedrat/Materials/FLUX_111_MATERI.DAT', materialNames=['FLU_NDFE30           :'])
startMacroTransaction()
Material['FLU_NDFE30'].propertyBH=PropertyBhMagnetOneDirection(br='1.23',
                                                               mur='1.05')

Material['FLU_NDFE30'].propertyJE=None

Material['FLU_NDFE30'].name='FLU_NDFE30_N'

endMacroTransaction()

importMaterial(fileName='D:/Instaled_programs/Cedrat/Materials/FLUX_111_MATERI.DAT', materialNames=['FLU_NDFE30           :'])

startMacroTransaction()
Material['FLU_NDFE30'].propertyBH=PropertyBhMagnetOneDirection(br='-1.23',
                                                               mur='1.05')
Material['FLU_NDFE30'].propertyJE=None
Material['FLU_NDFE30'].name='FLU_NDFE30_S'

endMacroTransaction()


lastInstance = MechanicalSetTranslation1Axis(name='MOVING',
                              kinematics=LinearImposedSpeed(velocity='.001',
                                                            initialPosition='0',
                                                            internalCharacteristics=LinearLoadCoefficients(mass='0',
                                                                                                           friction=LinearFrictionCoefficients(constantFriction='0',
                                                                                                                                               viscousCoefficient='0',
                                                                                                                                               squareSpeedCoefficient='0')),
                                                            externalCharacteristics=LinearLoadCoefficients(mass='0',
                                                                                                           friction=LinearFrictionCoefficients(constantFriction='0',
                                                                                                                                               viscousCoefficient='0',
                                                                                                                                               squareSpeedCoefficient='0'))),
                              translationAxis=TranslationXAxis(coordSys=CoordSys['XY1']))

lastInstance = MechanicalSetFixed(name='FIX')





lastInstance = RegionFace(name='MAGNET_BACK_IRON : magnet back iron (non-linear steel)',
           magneticAC2D=MagneticAC2DFaceMagnetic(material=Material['Infinite_Permeability']),
           color=Color['Cyan'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['MOVING'])


lastInstance = RegionFace(name='STATOR_BACK_IRON : stator back iron (non-linear steel)',
           magneticAC2D=MagneticAC2DFaceMagnetic(material=Material['Infinite_Permeability']),
           color=Color['Cyan'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['FIX'])

lastInstance = RegionFace(name='STATOR_TEETH : stator back iron (non-linear steel)',
           magneticAC2D=MagneticAC2DFaceMagnetic(material=Material['Infinite_Permeability']),
           color=Color['Cyan'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['FIX'])

lastInstance = RegionFace(name='MAGNET_N : PM N_pole',
           magneticAC2D=MagneticAC2DFaceMagnetic(material=Material['FLU_NDFE30_N']),
           color=Color['Cyan'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['MOVING'])


lastInstance = RegionFace(name='MAGNET_S : PM S_pole',
           magneticAC2D=MagneticAC2DFaceMagnetic(material=Material['FLU_NDFE30_S']),
           color=Color['Cyan'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['MOVING'])


lastInstance = RegionFace(name='PM_SPACER : pm distance',
           magneticAC2D=MagneticAC2DFaceVacuum(),
           color=Color['Yellow'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['MOVING'])


lastInstance = RegionFace(name='MOVING_BOX : moving_inf',
           magneticAC2D=MagneticAC2DFaceVacuum(),
           color=Color['Yellow'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['MOVING'])


lastInstance = RegionFace(name='FIXED_BOX : fixed_inf',
           magneticAC2D=MagneticAC2DFaceVacuum(),
           color=Color['Yellow'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['FIX'])

lastInstance = RegionFace(name='airgap_PM : moving airgap',
           magneticAC2D=MagneticAC2DFaceVacuum(),
           color=Color['Yellow'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['MOVING'])


lastInstance = RegionFace(name='airgap_STATOR : FIXED airgap',
           magneticAC2D=MagneticAC2DFaceVacuum(),
           color=Color['Yellow'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['FIX'])

lastInstance = RegionFace(name='STATOR_SLOTS : FIXED airgap',
           magneticAC2D=MagneticAC2DFaceVacuum(),
           color=Color['Yellow'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['FIX'])





assignRegionToFaces(face=[Face[49]],
                    region=RegionFace['FIXED_BOX'])

assignRegionToFaces(face=[Face[2]],
                    region=RegionFace['MOVING_BOX'])

assignRegionToFaces(face=[Face[1]],
                    region=RegionFace['MAGNET_BACK_IRON'])

assignRegionToFaces(face=[Face[22],
                          Face[25],
                          Face[28],
                          Face[31],
                          Face[34],
                          Face[37],
                          Face[40],
                          Face[43],
                          Face[46]],
                    region=RegionFace['STATOR_TEETH'])

assignRegionToFaces(face=[Face[48]],
                    region=RegionFace['STATOR_BACK_IRON'])

assignRegionToFaces(face=[Face[3],
                          Face[7],
                          Face[11],
                          Face[15]],
                    region=RegionFace['MAGNET_N'])

assignRegionToFaces(face=[Face[5],
                          Face[9],
                          Face[13],
                          Face[17]],
                    region=RegionFace['MAGNET_S'])

assignRegionToFaces(face=[Face[4],
                          Face[6],
                          Face[8],
                          Face[10],
                          Face[12],
                          Face[14],
                          Face[16],
                          Face[18]],
                    region=RegionFace['PM_SPACER'])

assignRegionToFaces(face=[Face[19]],
                    region=RegionFace['AIRGAP_PM'])

assignRegionToFaces(face=[Face[20]],
                    region=RegionFace['AIRGAP_STATOR'])





assignRegionToFaces(face=[Face[21],
                          Face[26],
                          Face[27]],
                    region=RegionFace['STATOR_SLOTS'])

assignRegionToFaces(face=[Face[23],
                          Face[24],
                          Face[29]],
                    region=RegionFace['STATOR_SLOTS'])

assignRegionToFaces(face=[Face[30],
                          Face[35],
                          Face[36]],
                    region=RegionFace['STATOR_SLOTS'])

assignRegionToFaces(face=[Face[32],
                          Face[33],
                          Face[38]],
                    region=RegionFace['STATOR_SLOTS'])

assignRegionToFaces(face=[Face[39],
                          Face[44],
                          Face[45]],
                    region=RegionFace['STATOR_SLOTS'])

assignRegionToFaces(face=[Face[41],
                          Face[42],
                          Face[47]],
                    region=RegionFace['STATOR_SLOTS'])



RegionFace['AIRGAP_PM'].magneticTransient2D=MagneticTransient2DFaceVacuum()
RegionFace['AIRGAP_STATOR'].magneticTransient2D=MagneticTransient2DFaceVacuum()
RegionFace['FIXED_BOX'].magneticTransient2D=MagneticTransient2DFaceVacuum()
RegionFace['MAGNET_BACK_IRON'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['INFINITE_PERMEABILITY'])
RegionFace['STATOR_BACK_IRON'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['INFINITE_PERMEABILITY'])
RegionFace['STATOR_TEETH'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['INFINITE_PERMEABILITY'])
RegionFace['MAGNET_N'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['FLU_NDFE30_N'])
RegionFace['MAGNET_S'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['FLU_NDFE30_S'])
RegionFace['MOVING_BOX'].magneticTransient2D=MagneticTransient2DFaceVacuum()
RegionFace['PM_SPACER'].magneticTransient2D=MagneticTransient2DFaceVacuum()
RegionFace['STATOR_SLOTS'].magneticTransient2D=MagneticTransient2DFaceVacuum()

orientRegSurfMaterial(region=RegionFace['MAGNET_N'],coordSys=CoordSys['XY1'],orientation='Direction',angle='90')
orientRegSurfMaterial(region=RegionFace['MAGNET_S'],coordSys=CoordSys['XY1'],orientation='Direction',angle='90')


result = checkPhysic()

SolvingOptions['SOLVING_OPTIONS'].newtonRaphsonParameters=ParametersNewtonRaphson(precision=1.0E-4,
                                                                                  maximumIterationNumber=100,
                                                                                  relaxationFactorComputationMethod=ParametersNewtonRaphsonRelaxationFactorComputationMethodFujiwara())



Scenario(name='Scenario_1')
startMacroTransaction()
Scenario['Scenario_1'].addPilot(pilot=MultiValues(parameter=VariationParameter['LINPOS_MOVING'],
                                                  intervals=[IntervalStepNumber(minValue=0.0,
                                                                                maxValue=0.005,
                                                                                stepNumber=50)]))
endMacroTransaction()


Scenario['SCENARIO_1'].solve(projectName='Cogging_PML_transient_Parametric_solved')

