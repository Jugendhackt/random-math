$('.themachooser').click(function (e) {
  var thema = e.currentTarget.id
  localStorage.clear()
  window.location.href = 'aufgabe.html?thema='+thema
})