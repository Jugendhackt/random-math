$('#sentbtn').click(function() {
  var entered = $('#text').val()
  if(entered == localStorage.getItem('loesung')) {
  $('#start').hide()
  //NOT COOL >
  $('#sent').show()
  // < TO DO THIS
  $('#solving_sent').attr("value", entered)
  } else {
    localStorage.setItem('step', 0)
    $('#stepsolving_schrittid').text(localStorage.getItem('step')+1)
    $('#start').hide()
    $('#stepsolving').show()
    $('#stepsolving_wrong').show()
  }
})
$('#nextexercisebtn').click(function () {
  $("#sent").hide()
  $("#start").show()
})
$('#backtothemesbtn').click(function () {
  window.location.href = "index.html"
})
