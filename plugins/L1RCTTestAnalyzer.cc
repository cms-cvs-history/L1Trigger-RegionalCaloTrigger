// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/L1CaloTrigger/interface/L1CaloCollections.h"

#include "L1Trigger/RegionalCaloTrigger/interface/L1RCTTestAnalyzer.h"

using std::string;
using std::cout;
using std::endl;

//
// constructors and destructor
//
L1RCTTestAnalyzer::L1RCTTestAnalyzer(const edm::ParameterSet& iConfig) :
  showEmCands(iConfig.getUntrackedParameter<bool>("showEmCands")),
  showRegionSums(iConfig.getUntrackedParameter<bool>("showRegionSums")),
  ecalDigisLabel(iConfig.getParameter<edm::InputTag>("ecalDigisLabel")),
  hcalDigisLabel(iConfig.getParameter<edm::InputTag>("hcalDigisLabel")),
  rctDigisLabel(iConfig.getParameter<edm::InputTag>("rctDigisLabel"))
{
   //now do what ever initialization is needed

  edm::Service<TFileService> fs;
  h_emRank = fs->make<TH1F>( "emRank", "emRank", 64, 0., 64. );
  h_emRankOutOfTime = fs->make<TH1F>( "emRankOutOfTime", "emRankOutOfTime",
				      64, 0., 64. );
  h_emIeta = fs->make<TH1F>( "emIeta", "emIeta", 22, 0., 22. );
  h_emIphi = fs->make<TH1F>( "emIphi", "emIphi", 18, 0., 18. );
  h_emIso = fs->make<TH1F>( "emIso", "emIso", 2, 0., 2. );
  h_emRankInIetaIphi = fs->make<TH2F>( "emRank2D", "emRank2D", 22, 0., 22.,
				       18, 0., 18. );
  h_emIsoInIetaIphi = fs->make<TH2F>( "emIso2D", "emIso2D", 22, 0., 22.,
				      18, 0., 18. );
  h_emNonIsoInIetaIphi = fs->make<TH2F>( "emNonIso2D", "emNonIso2D", 22, 0., 
					 22., 18, 0., 18. );
  h_emCandTimeSample = fs->make<TH1F>( "emCandTimeSample", "emCandTimeSample",
				       5, -2., 2.);

  h_regionSum = fs->make<TH1F>( "regionSum", "regionSum", 100, 0., 100. );
  h_regionIeta = fs->make<TH1F>( "regionIeta", "regionIeta", 22, 0., 22. );
  h_regionIphi = fs->make<TH1F>( "regionIphi", "regionIphi", 18, 0., 18. );
  h_regionMip = fs->make<TH1F>( "regionMip", "regionMipBit", 2, 0., 2. );
  h_regionSumInIetaIphi = fs->make<TH2F>( "regionSum2D", "regionSum2D", 22, 
					  0., 22., 18, 0., 18. );
  h_regionFGInIetaIphi = fs->make<TH2F>( "regionFG2D", "regionFG2D", 22, 0.,
					 22., 18, 0., 18. );

  h_towerMip = fs->make<TH1F>( "towerMip", "towerMipBit", 2, 0., 2. );

  h_ecalTimeSample = fs->make<TH1F>( "ecalTimeSample", "ecalTimeSample",
				     10, 0., 10. );
  h_hcalTimeSample = fs->make<TH1F>( "hcalTimeSample", "hcalTimeSample",
				     10, 0., 10. );

  // get names of modules, producing object collections
}


L1RCTTestAnalyzer::~L1RCTTestAnalyzer()
{

   // do anything here that needs to be done at destruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
L1RCTTestAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif

#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif

   // as in L1GctTestAnalyzer.cc
   Handle<L1CaloEmCollection> rctEmCands;
   Handle<L1CaloRegionCollection> rctRegions;
   Handle<EcalTrigPrimDigiCollection> ecalColl;
   Handle<HcalTrigPrimDigiCollection> hcalColl;

   L1CaloEmCollection::const_iterator em;
   L1CaloRegionCollection::const_iterator rgn;
   EcalTrigPrimDigiCollection::const_iterator ecal;
   HcalTrigPrimDigiCollection::const_iterator hcal;

   iEvent.getByLabel(rctDigisLabel, rctEmCands);
   iEvent.getByLabel(rctDigisLabel, rctRegions);
   iEvent.getByLabel(ecalDigisLabel, ecalColl);
   iEvent.getByLabel(hcalDigisLabel, hcalColl);

   for (ecal=ecalColl->begin(); ecal!=ecalColl->end(); ecal++)
     {
       for (unsigned short sample = 0; sample < (*ecal).size(); sample++)
	 {
	   h_ecalTimeSample->Fill(sample);
	 }
     }

   for (hcal=hcalColl->begin(); hcal!=hcalColl->end(); hcal++)
     {
       h_towerMip->Fill( (*hcal).SOI_fineGrain() );
       for (unsigned short sample = 0; sample < (*hcal).size(); sample++)
	 {
	   h_hcalTimeSample->Fill(sample);
	 }
     }

   if(showEmCands)
     {
       cout << endl << "L1 RCT EmCand objects" << endl;
     }
   for (em=rctEmCands->begin(); em!=rctEmCands->end(); em++){
     //  cout << "(Analyzer)\n" << (*em) << endl;
     h_emCandTimeSample->Fill((*em).bx());
     if ((*em).bx() == 0)
       {
	 unsigned short n_emcands = 0;
	 //cout << endl << "rank: " << (*em).rank() ;
	 
	 if ((*em).rank() > 0)
	   {
	     h_emRank->Fill( (*em).rank() );
	     h_emIeta->Fill( (*em).regionId().ieta() );
	     h_emIphi->Fill( (*em).regionId().iphi() );
	     h_emIso->Fill( (*em).isolated() );
	     h_emRankInIetaIphi->Fill( (*em).regionId().ieta(), 
				       (*em).regionId().iphi(),
				       (*em).rank() );
	     if ((*em).isolated())
	       {
		 h_emIsoInIetaIphi->Fill( (*em).regionId().ieta(),
					  (*em).regionId().iphi() );
	       }
	     else
	       {
		 h_emNonIsoInIetaIphi->Fill( (*em).regionId().ieta(),
					     (*em).regionId().iphi() );
	       }
	   }
	 
	 if (showEmCands)
	   {
	     if ((*em).rank() > 0)
	       {
		 cout << endl << "rank: " << (*em).rank();
		 unsigned short rgnPhi = 999;
		 unsigned short rgn = (unsigned short) (*em).rctRegion();
		 unsigned short card = (unsigned short) (*em).rctCard();
		 unsigned short crate = (unsigned short) (*em).rctCrate();
		 
		 if (card == 6)
		   {
		     rgnPhi = rgn;
		   }
		 else if (card < 6)
		   {
		     rgnPhi = (card % 2);
		   }
		 else 
		   {
		     cout << "rgnPhi not assigned (still " << rgnPhi << ") -- Weird card number! " << card ;
		   }
		 unsigned short phi_bin = ((crate % 9) * 2) + rgnPhi;
		 short eta_bin = (card/2) * 2 + 1;
		 if (card < 6)
		   {
		     eta_bin = eta_bin + rgn;
		   }
		 if (crate < 9)
		   {
		     eta_bin = -eta_bin;
		   }
		 n_emcands++;
		 cout << /* "rank: " << (*em).rank() << */ "  eta_bin: " << eta_bin << "  phi_bin: " << phi_bin << ".  crate: " << crate << "  card: " << card << "  region: " << rgn << ".  isolated: " << (*em).isolated();
	       }
	   }
       }
     else
       {
	 h_emRankOutOfTime->Fill( (*em).rank() );
       }
   }
   if(showEmCands)
     {
       cout << endl;
     }

   if(showRegionSums)
     {
       cout << "Regions" << endl;
     }
   for (rgn=rctRegions->begin(); rgn!=rctRegions->end(); rgn++)
     {
       if ((*rgn).bx() == 0)
	 {
	   if(showRegionSums)
	     {
	       cout << /* "(Analyzer)\n" << */ (*rgn) << endl;
	     }
	   if ( (*rgn).et() > 0 )
	     {
	       h_regionSum->Fill( (*rgn).et() );
	       h_regionIeta->Fill( (*rgn).gctEta() );
	       h_regionIphi->Fill( (*rgn).gctPhi() );
	       h_regionSumInIetaIphi->Fill( (*rgn).gctEta(), (*rgn).gctPhi(),
					    (*rgn).et() );
	       h_regionFGInIetaIphi->Fill( (*rgn).gctEta(), (*rgn).gctPhi(),
					   (*rgn).fineGrain() );
	     }
	   h_regionMip->Fill( (*rgn).mip() );
	 }
     }
   if(showRegionSums)
     {
       cout << endl;
     }

}
