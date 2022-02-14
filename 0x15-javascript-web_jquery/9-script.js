const $ = window.jQuery;
helloInFrench();

async function helloInFrench () {
  const response = await fetch('https://fourtonfish.com/hellosalut/?lang=fr');
  const result = await response.json();
  const traslation = result;
  $('DIV#hello').append(traslation.hello);
}
