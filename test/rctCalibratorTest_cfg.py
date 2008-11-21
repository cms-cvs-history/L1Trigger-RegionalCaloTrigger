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
    input = cms.untracked.int32(10)
)

#process.load("FWCore.Framework.test.cmsExceptionsFatal_cff")

#process.source = cms.Source("EmptySource")

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring("dcap://cmsdcap.hep.wisc.edu:22125/pnfs/hep.wisc.edu/store/user/lgray/PGun2pi2gamma-merge_cfg/merge_cfg-PGun2pi2gamma-1729.root",
                                                              )
                            )
    
process.load("L1Trigger.RegionalCaloTrigger.rctGenCalibrator_cfi")
process.rctGenCalibrator.RegionsInput = cms.InputTag("simRctDigis")
process.rctGenCalibrator.EcalTPGInput = cms.InputTag("simEcalTriggerPrimitiveDigis")
process.rctGenCalibrator.HcalTPGInput = cms.InputTag("simHcalTriggerPrimitiveDigis")
process.rctGenCalibrator.CalibrationInputs = cms.VInputTag("genParticles")
process.rctGenCalibrator.OutputFile = cms.string("RCTGenCalibrator")
process.rctGenCalibrator.debug = cms.untracked.int32(0)
process.rctGenCalibrator.FarmoutMode = cms.untracked.bool(True)

#process.p0 = cms.Path(process.pgen)
#process.p1 = cms.Path(process.psim)
#process.p2 = cms.Path(process.pdigi)
process.p4 = cms.Path(process.rctGenCalibrator)
process.schedule = cms.Schedule(process.p4)



