var $zoho = $zoho || {}; 
$zoho.salesiq = $zoho.salesiq || { widgetcode: "siq48cc1989a099fad37347fb2522a5854d3033f86ee9a42a38a67f111506587723", values: {}, ready: function () {
    var spanName = document.querySelector("[itemprop='name']").textContent;
    $zoho.salesiq.visitor.name(spanName);
    var spanMail = document.querySelector("[itemprop='email']");
    $zoho.salesiq.visitor.name(spanMail);
} };
var d = document; s = d.createElement("script");
s.type = "text/javascript";
s.id = "zsiqscript";
s.defer = true;

s.src = "https://salesiq.zohopublic.eu/widget";
t = d.getElementsByTagName("script")[0];
t.parentNode.insertBefore(s, t);

