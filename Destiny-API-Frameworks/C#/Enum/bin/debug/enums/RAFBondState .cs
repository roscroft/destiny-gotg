namespace JsonToEnum.Export { 
 	public enum  RAFBondState  
 	{ 
 		 None = 0, 
 		 AwaitingNewPlayerDestinyMembership = 1, 
 		 AwaitingNewPlayerVerification = 2, 
 		 NewPlayerVerified = 3, 
 		 BondLockedIn = 100, 
 		 BondRemoved = -100, 
 		 FailedNewPlayerAlreadyReferred = -3, 
 		 FailedNewPlayerIsVeteranPlayer = -2, 
 		 FailedNewPlayerIsNotNew = -1 
 	} 
 } 