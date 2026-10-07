function doGet() {
  return HtmlService.createHtmlOutputFromFile('index')
    .setTitle('KFA HUB')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}
