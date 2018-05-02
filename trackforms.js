var track_forms = [
    // form names
    'registrationForm',
    'dicePostAJob', //This won't bind, it needs to be included by devs
    // class names
    'home-contact',
    'mktoForm'
];

$('form').each(function(key,item){
  if($(item).attr('data-trackform')){
    _satellite.setCookie('dtm_form_name', $(item).attr('data-trackform'));
    return false;
  }
  
  var data_trackform = '';
  var form_name = $(item).attr('name');
  if(form_name && track_forms.indexOf(form_name) > -1){
    data_trackform = form_name;
  }
  else{
    $(track_forms).each(function(key2,item2){
      if($(item).hasClass(item2)){
        data_trackform = item2;
        if (item2 == 'mktoForm') {
          data_trackform = $(item).attr('id');
        }
      }
    });
  }
  if(data_trackform){
    $('form').eq(key).attr('data-trackform', data_trackform);
    _satellite.setCookie('dtm_form_name', data_trackform);
  }
});

return true;

$('body').on('focus', '#mktoForm_1965 input', function(){console.log('pulse');})

document.getElementById('#mktoForm_1965').setAttribute('data-trackform', "mktoForm_lengo")





var formsCollection = document.getElementsByTagName("form");
for(var i=0;i<formsCollection.length;i++)
{
  console.log(formsCollection[i].name);
}

var pageForms = document.forms;
var marketoForm = pageForms[0].id
document.getElementById(marketoForm).setAttribute('data-trackform', marketoForm)






