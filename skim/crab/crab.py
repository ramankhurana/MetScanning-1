from CRABClient.UserUtilities import config, getUsernameFromSiteDB
#submit with 'python crab.py'
#Don't write to my directory (schoef), though

config = config()
config.General.requestName = 'June20_4fbInvV1'  #'ZeroBias1_Run2015A-PromptReco-v1_RECO'
config.General.workArea =  'Run2016B/' # 'private4TSkim_24Jul2015_update'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../python/skim.py'
config.JobType.outputFiles = ['tuple.root']
config.Data.inputDataset = '/StreamExpress/Run2016B-Hotline-Express-v1/ALCARECO' 
config.Data.inputDBS = 'global'
config.Data.lumiMask =  'Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
#config.Data.runRange = '272818'
config.Data.publication = False

#config.Data.ignoreLocality = True                                                                                                                                                                       
#config.Site.whitelist = ['T1_US_FNAL'] 

#config.Data.outLFNDirBase = '' 
#config.Data.publishDataName = ''

config.Data.outLFNDirBase = '/store/user/khurana/METHotline/Json2fbInv_V2/' #/store/user/%s/' % (getUsernameFromSiteDB())  #'/store/group/phys_jetmet/beranek/private4TSkim_24Jul2015_update/'
config.Site.storageSite = 'T2_US_Wisconsin'


datasets=[
#'/StreamExpress/Run2016B-Hotline-Express-v2/ALCARECO',
'/MET/Run2016B-HighMET-PromptReco-v2/RECO',
#'/MET/Run2016B-PromptReco-v2/RECO',
#'/JetHT/Run2016B-PromptReco-v2/RECO',
#'/DoubleMuon/Run2016B-PromptReco-v2/RECO'
]

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for dataset in datasets:
        config.Data.inputDataset = dataset
        config.General.requestName = dataset.rstrip('/').lstrip('/').replace('/','_')
#        print config.General.requestName
        crabCommand('submit', config = config)

