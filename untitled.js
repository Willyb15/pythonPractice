var forms = [
  {
    'name': 'mktoForm_1339',
    'complete_path': '/Dice_General-ContactUs-TY-D.html'
  },{
    'name': 'mktoForm_1891',
    'complete_path': '/2017-contact-us_ty.html'
  },{
    'name': 'mktoForm_1907',
    'complete_path': '/2017-homepagebanner-ty.html'
  },{
    'name': 'mktoForm_recruitpkg',
    'complete_path': '/premium-recruitment-package-ty'
  },{
    'name': 'mktoForm_recruitpkgB',
    'complete_path': '/premium-recruitment-package-b-ty'
  },{
    'name': 'mktoForm_1282',
    'complete_path': '/2016-05-18-Dice_RecruitmentPackage_CU_TY_D.html'
  },{
    'name': 'mktoForm_openweb',
    'complete_path': '/products/open-web-ty'
  },{
    'name': 'mktoForm_prempost',
    'complete_path': '/products/premium-post-ty'
  },{
    'name': 'mktoForm_sourcing',
    'complete_path': '/products/sourcing-concierge-ty'
  },{
    'name': 'mktoForm_sourcingB',
    'complete_path': '/products/sourcing-concierge-b-ty'
  },{
    'name': 'mktoForm_THC',
    'complete_path': '/products/targeted-hiring-ty'
  },{
    'name': 'mktoForm_lengo',
    'complete_path': '/products/lengo-ty'
  },{
    'name': 'mktoForm_branding',
    'complete_path': '/products/branding-opportunities-ty'
  },{
    'name': 'mktoForm_assessments',
    'complete_path': '/products/hackerearth-ty'
  },{
    'name': 'mktoForm_hackathons',
    'complete_path': '/products/hackathons-ty'
  },{
    'name': 'mktoForm_talentsolutions',
    'complete_path': '/talent-solutions-center-ty'
  },{
    'name': 'mktoForm_1972',
    'complete_path': '/mktoForm_1972-ty'
  },{
    'name': 'mktoForm_1973',
    'complete_path': '/mktoForm_1973-ty'
  },{
  	'name': 'mktoForm_1965',
    'complete_path': '2018-DiceLP-5StrategiesCoolKid_PRMD-TY.html'
  }
];

var page_forms = [];
$('form[data-trackform]').each(function(key,item){
  page_forms = $.grep(forms, function(i){ return i.name == $(item).attr('data-trackform') });
});


if(page_forms.length > 0)
  return false;


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

var lower_form_name = form_name.toLowerCase() + "-ty";
var lower_path_name = window.location.pathname.toLowerCase();
if(lower_path_name.indexOf(lower_form_name) > -1 && form_name){
     window.ssdl.trackEvent({
        'action': 'form_completed',
        'data': {
            'form_name': form_name
        }
    });
    _satellite.removeCookie('dtm_form_name');
    return true;
}


$('form[data-trackform]').on('submit', function(){
  window.ssdl.trackEvent({
        'action': 'form_completed',
        'data': {
            'form_name': $(this).attr('data-trackform')
        }
   });
  
});

return true;