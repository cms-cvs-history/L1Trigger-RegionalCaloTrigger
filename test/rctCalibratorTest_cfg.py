import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("Configuration.StandardSequences.Services_cff")

process.load("FWCore.MessageService.MessageLogger_cfi")

#process.MessageLogger.desinations = cms.untracked.vstring( "cout" )
#process.MessageLogger.cout = cms.untracked.PSet( threshold = cms.untracked.string("DEBUG") )
#process.MessageLogger.debugModules = cms.untracked.vstring( "rctGenCalibrator" )

process.load("L1TriggerConfig.RCTConfigProducers.L1RCTConfig_cff")

process.load("L1TriggerConfig.L1ScalesProducers.L1CaloScalesConfig_cff")

process.load("L1TriggerConfig.L1ScalesProducers.L1CaloInputScalesConfig_cff")

process.load("L1TriggerConfig.L1GeometryProducers.l1CaloGeomConfig_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.load("FWCore.Framework.test.cmsExceptionsFatal_cff")

process.source = cms.Source("EmptySource")

#process.source = cms.Source("PoolSource",
#                            fileNames = cms.untracked.vstring("dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0000.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0001.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0002.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0003.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0004.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0005.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0006.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0007.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0008.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0009.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0010.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0011.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0012.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0013.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0014.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0015.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0016.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0017.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0018.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0019.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0020.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0021.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0022.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0023.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0024.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0025.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0026.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0027.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0028.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0029.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0030.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0031.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0032.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0033.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0034.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0035.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0036.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0037.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0038.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0039.root",
#                                                              "dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma/PGun2pi2gamma-0040.root"
#                                                              )
#                            )
    
process.load("L1Trigger.RegionalCaloTrigger.rctGenCalibrator_cfi")
process.rctGenCalibrator.RegionsInput = cms.InputTag("simRctDigis")
process.rctGenCalibrator.EcalTPGInput = cms.InputTag("simEcalTriggerPrimitiveDigis")
process.rctGenCalibrator.HcalTPGInput = cms.InputTag("simHcalTriggerPrimitiveDigis")
process.rctGenCalibrator.CalibrationInputs = cms.VInputTag("genParticles")
process.rctGenCalibrator.OutputFile = cms.string("RCTGenCalibrator")
process.rctGenCalibrator.debug = cms.untracked.int32(11)

#process.p0 = cms.Path(process.pgen)
#process.p1 = cms.Path(process.psim)
#process.p2 = cms.Path(process.pdigi)
process.p4 = cms.Path(process.rctGenCalibrator)
process.schedule = cms.Schedule(process.p4)



