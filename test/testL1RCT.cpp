#include <vector>

#include "L1Trigger/RegionalCaloTrigger/interface/L1RCT.h"
#include "L1Trigger/RegionalCaloTrigger/interface/L1RCTLookupTables.h"
#include "CondFormats/L1TObjects/interface/L1RCTParameters.h"

int main(){
  // For testing use 1:1 LUT
  std::vector<double> eGammaECalScaleFactors(32, 1.0);
  std::vector<double> eGammaHCalScaleFactors(32, 1.0);
  std::vector<double> jetMETECalScaleFactors(32, 1.0);
  std::vector<double> jetMETHCalScaleFactors(32, 1.0);
  L1RCTParameters* rctParameters = 
    new L1RCTParameters(1.0,                       // eGammaLSB
			1.0,                       // jetMETLSB
			3.0,                       // eMinForFGCut
			40.0,                      // eMaxForFGCut
			0.5,                       // hOeCut
			1.0,                       // eMinForHoECut
			50.0,                      // eMaxForHoECut
			2.0,                       // eActivityCut
			3.0,                       // hActivityCut
			3.0,                       // eicIsolationThreshold
			false,                     // ignoreTowerHB
			false,                     // ignoreTowerHEplus
			false,                     // ignoreTowerHEminus
			eGammaECalScaleFactors,
			eGammaHCalScaleFactors,
			jetMETECalScaleFactors,
			jetMETHCalScaleFactors
			);
  L1RCTLookupTables* lut = new L1RCTLookupTables();
  lut->setRCTParameters(rctParameters);  // transcoder and etScale are not used
  L1RCT rct(lut);
  rct.randomInput();
  //rct.print();
  rct.processEvent();
  rct.printJSC();
}
