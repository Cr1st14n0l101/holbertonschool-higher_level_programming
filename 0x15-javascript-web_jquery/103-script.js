const $ = window.jQuery;
let language = '';
window.onload = (event) => {
  helloTraslatorOnClick();
  helloTraslatorOnEnter();
};

function helloTraslatorOnClick () {
  $('INPUT#btn_translate').click(async function () {
    language = $('INPUT#language_code').val();
    const response = await fetch('https://fourtonfish.com/hellosalut/?lang=' + language);
    const traslation = await response.json();
    $('DIV#hello').empty();
    $('DIV#hello').append(traslation.hello);
  });
}

function helloTraslatorOnEnter () {
  $('INPUT#language_code').keypress(async function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode == '13') {
      language = $('INPUT#language_code').val();
      const response = await fetch('https://fourtonfish.com/hellosalut/?lang=' + language);
      const traslation = await response.json();
      $('DIV#hello').empty();
      $('DIV#hello').append(traslation.hello);
    }
    event.stopPropagation();
  });
}
