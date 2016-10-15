$('#sentbtn').click(function() {
var entered = $('#text').val()

  $('#start').hide()
  //NOT COOL >
  $('#sent').show()
  // < TO DO THIS
  $('#solving_sent').attr("value", entered)
})
$('#nextexercisebtn').click(function () {
  $("#sent").hide()
  $("#start").show()
})
$('#backtothemesbtn').click(function () {
  window.location.href = "index.html"
})
