const $ = window.jQuery;
let language = '';
window.onload = (event) => {
  helloTraslator();
};

function helloTraslator () {
  $('INPUT#btn_translate').click(async function () {
    language = $('INPUT#language_code').val();
    const response = await fetch('https://fourtonfish.com/hellosalut/?lang=' + language);
    const traslation = await response.json();
    $('DIV#hello').empty();
    $('DIV#hello').append(traslation.hello);
  });
}
