# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: AMPT_PPb_5020GeV_MinimumBias_cfi --fileout AMPT_PbPb_5020GeV_MinimumBias.root --conditions auto:run2_mc -s GEN,SIM --datatier GEN-SIM --eventcontent RAWSIM --scenario HeavyIons
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision$'),
    annotation = cms.untracked.string('AMPT PPb 5020 GeV Minimum Bias'),
    name = cms.untracked.string('$Source$')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('AMPT_PbPb_5020GeV_MinimumBias.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.generator = cms.EDFilter("AMPTGeneratorFilter",
    alpha = cms.double(0.47140452),
    amptmode = cms.int32(1),
    bMax = cms.double(30),
    bMin = cms.double(0),
    comEnergy = cms.double(5020.0),
    deuteronfactor = cms.int32(5),
    deuteronmode = cms.int32(0),
    deuteronxsec = cms.int32(1),
    diquarkembedding = cms.int32(0),
    diquarkpx = cms.double(7.0),
    diquarkpy = cms.double(0.0),
    diquarkx = cms.double(0.0),
    diquarky = cms.double(0.0),
    doInitialAndFinalRadiation = cms.int32(3),
    dpcoal = cms.double(1000000.0),
    drcoal = cms.double(1000000.0),
    dt = cms.double(0.2),
    firstEvent = cms.untracked.uint32(1),
    firstRun = cms.untracked.uint32(1),
    frame = cms.string('CMS'),
    iap = cms.int32(208),
    iat = cms.int32(208),
    izp = cms.int32(82),
    izpc = cms.int32(0),
    izt = cms.int32(82),
    ks0decay = cms.bool(False),
    ktkick = cms.int32(1),
    maxmiss = cms.int32(1000),
    minijetpt = cms.double(-7.0),
    mu = cms.double(3.2264),
    ntmax = cms.int32(1000),
    phidecay = cms.bool(True),
    popcornmode = cms.bool(True),
    popcornpar = cms.double(1.0),
    proj = cms.string('A'),
    pthard = cms.double(2.0),
    quenchingmode = cms.bool(False),
    quenchingpar = cms.double(2.0),
    rotateEventPlane = cms.bool(True),
    shadowingmode = cms.bool(True),
    stringFragA = cms.double(2.2),
    stringFragB = cms.double(0.5),
    targ = cms.string('A')
)





# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen_hi)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

