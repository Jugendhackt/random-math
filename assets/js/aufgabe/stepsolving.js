$('#stepsolvingbtn').click(function () {
  localStorage.setItem('step', 0)
  $('#stepsolving_schrittid').text(localStorage.getItem('step')+1)
  $('#start').hide()
  $('#stepsolving').show()
})

$('#next_stepbtn').click(function () {
  $('#stepright').hide()
  $('#stepsolving').show()
})

$('#nextstepbtn').click(function () {
  $('#stepsolution').hide()
  $('#stepsolving').show()
})

$('#send_stepbtn').click(function () {
  if(1 == 2) {
    $('#stepsolving').hide()
    $('#stepright').show()
  } else {
    if(localStorage.getItem('step') == '1') {
      toastr["info"]("Der Tipp", "Tipp")

      toastr.options = {
        "closeButton": true,
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
    else if(localStorage.getItem('step') == '2') {
      $('#stepsolving').hide()
      $('#stepsolution').show()
    }
    }
  localStorage.setItem('step', parseInt(localStorage.getItem('step'))+1)
  $('#stepsolving_schrittid').val($('#stepsolving_schrittid').val()+1)
  $('#stepsolving_wrong').show()

})
