function getParameterByName(name, url) {
  if (!url) url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
    results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}
if(getParameterByName('thema') == 'trigonometrie') {
  $('#exerciseimg').attr('src', 'assets/img/Fadenpendel_alembert.svg.png')
}
$.ajax({
  method: 'GET',
  url: 'http://randommathserver.labcode.de/' + getParameterByName('thema')
}).done(function (data) {
  console.log(data)
  var obj = JSON.parse(data)
  localStorage.setItem('loesung', btoa(obj.Loesung))
  localStorage.setItem('tipp', obj.Tipp)
  localStorage.setItem('aufgabe', obj.Aufgabe)
  localStorage.setItem('schritte', obj.Schritte)
  localStorage.setItem('rechenweg', obj.Tipp)
  $('#aufgabe').text(localStorage.getItem('aufgabe'))
  $('#rechenweg').text(localStorage.getItem('rechenweg'))
  if(localStorage.getItem('schritte') == 'undefined'){
    $('#stepsolvingbtn').addClass('disabled')
  }
})