$('#sentbtn').click(function() {
  var entered = $('#text').val()
  if(btoa(entered) == localStorage.getItem('loesung')) {
  $('#start').hide()
  $('#sent').show()
  $('#solving_sent').attr("value", entered)
  } else {
    toastr["info"](localStorage.getItem('tipp'), "Tipp")

    toastr.options = {
      "closeButton": false,
      "debug": false,
      "newestOnTop": false,
      "progressBar": false,
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
  window.location.reload()
})
$('#backtothemesbtn').click(function () {
  window.location.href = "index.html"
})
