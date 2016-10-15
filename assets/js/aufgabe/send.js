$('#sent').click(function() {
var entered = $('#text').val()
  $('#start').hide()
  $('#sent').show()
  $('#solving_sent').attr("value", entered)
})
