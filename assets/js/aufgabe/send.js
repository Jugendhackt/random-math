$('#sentbtn').click(function() {
  var entered = $('#text').val()
  console.log(localStorage.getItem('loesung'))
  console.log(entered == localStorage.getItem('loesung'))
  if(entered == localStorage.getItem('loesung')) {
  $('#start').hide()
  //NOT COOL >
  $('#sent').show()
  // < TO DO THIS
  $('#solving_sent').attr("value", entered)
  } else {
    toastr["info"](localStorage.getItem('tipp'), "Tipp")

    toastr.options = {
      "closeButton": false,
      "debug": false,
      "newestOnTop": false,
      "progressBar": true,
      "positionClass": "toast-top-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "25000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
    }
  }
})
$('#nextexercisebtn').click(function () {
  $("#sent").hide()
  $("#start").show()
})
$('#backtothemesbtn').click(function () {
  window.location.href = "index.html"
})
