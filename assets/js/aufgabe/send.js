$('#sentbtn').click(function() {
var entered = $('#text').val()

  $('#start').hide()
  //NOT COOL >
  $('#sent').show()
  // < TO DO THIS
  $('#solving_sent').attr("value", entered)
})
