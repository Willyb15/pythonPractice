var form_name = _satellite.readCookie('dtm_form_name') || '';


var complete_page = $.grep(forms, function(i){ return window.location.pathname.indexOf(i.complete_path) > -1 });
if(complete_page.length > 0 && form_name){
   window.ssdl.trackEvent({
        'action': 'form_completed',
        'data': {
            'form_name': form_name
        }
    });
    _satellite.removeCookie('dtm_form_name');
    return true;
}


var forms = [
  {
    'name': 'mktoForm_1965',
    'complete_path': '/2018-DiceLP-5StrategiesCoolKid_PRMD-TY.html'
  },{
    'name': 'mktoForm_1947',
    'complete_path': '/2018-DiceLP-TechSalaryReport_PRMD.html'
  },{
    'name': 'mktoForm_1919',
    'complete_path': '/018-DiceLP-TimingIsEverything_PRMD.html'
  },{
    'name': 'mktoForm_2023',
    'complete_path': '/2018-DiceLP-WhatTechTalentWants_PRMD.html'
  },{
    'name': 'mktoForm_2024',
    'complete_path': '/2018-DiceLP-RaisingTheBarOnTechTalent_PRMD-TY.html'
  }
];

var track = false; 
var path = window.location.pathname
for(var i=0; i<forms.length;i++){
	if(forms[i].complete_path == path){
		track = true;
	}
}


