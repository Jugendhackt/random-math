function getParameterByName(name, url) {
  if (!url) url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
    results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}

$.ajax({
  method: 'GET',
  url: 'http://localhost:61535/' + getParameterByName('thema')
}).done(function (data) {
  var obj = JSON.parse(data)
  localStorage.setItem('loesung', obj.Loesung)
  localStorage.setItem('tipp', obj.Tipp)
  localStorage.setItem('aufgabe', obj.Aufgabe)
})