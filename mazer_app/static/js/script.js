var hidden = true;

$('#solution').on('click', function(event) {
  if (hidden) {
    hidden = false;
    $(this).val('Hide solution');
    $('.path').addClass('highlight').removeClass('corridor');
  } else {
    hidden = true;
    $(this).val('Show solution');
    $('.path').addClass('corridor').removeClass('highlight');
  }
});

$('form').on('submit', function(event) {
  var fontSize = $('#maze').css('fontSize');
  fontSize = parseInt(fontSize.split('px')[0]/2);
  if (!hidden) {
    hidden = true;
    $('#solution').val('Show solution');
  }
  $.ajax({
    url: '/gen',
    data: {
      seed: $('#seed').val(),
      width: $('#width').val(),
      height: $('#height').val(),
      size: fontSize
    },
    type: 'POST'
    })
  .done(function(data) {
    if ($('#maze').has('svg')) {
      $('#maze svg').remove();
    }
    $('#maze').append(data);
  });
  event.preventDefault();
  event.stopPropagation();
});
